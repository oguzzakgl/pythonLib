from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
import io
import uvicorn
import numpy as np

# UygulamayÄ± OluÅŸtur
app = FastAPI()

def grafik_ciz():
    # 1. Matplotlib ile Grafik OluÅŸtur
    plt.figure(figsize=(10, 6))
    
    # Veri
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y, color='purple', linewidth=3)
    plt.title("Web Ãœzerinde Python GrafiÄŸi (SinÃ¼s DalgasÄ±)")
    plt.grid(True)
    
    # 2. Resmi Dosyaya Kaydetmek Yerine HAFIZAYA (RAM) Kaydet
    # (Bu yÃ¶ntem diski kirletmez, daha hÄ±zlÄ±dÄ±r)
    resim_kutusu = io.BytesIO()
    plt.savefig(resim_kutusu, format='png')
    resim_kutusu.seek(0) # Kutunun baÅŸÄ±na sar (okumak iÃ§in)
    
    return resim_kutusu

@app.get("/")
async def ana_sayfa():
    # 3. Web Sitesine Resmi GÃ¶nder
    resim = grafik_ciz()
    return StreamingResponse(resim, media_type="image/png")

if __name__ == "__main__":
    print("Sunucu baÅŸlatÄ±lÄ±yor... http://127.0.0.1:8000 adresine gidin.")
    uvicorn.run(app, host="127.0.0.1", port=8000)

# ÖZET: Oluşturulan grafikleri fiziksel bir dosyaya kaydetmek yerine RAM (bellek) üzerinden doğrudan bir web sunucusuna (FastAPI) nasıl aktaracağımızı ve dinamik görsel sunumunu öğreniyoruz.
