# 📊 Matplotlib ile Web Entegrasyonu
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
import io
import uvicorn
import numpy as np

# Uygulamayı Oluştur
app = FastAPI()

def grafik_ciz():
    # 1. Matplotlib ile Grafik Oluştur
    plt.figure(figsize=(10, 6))
    
    # Veri
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y, color='purple', linewidth=3)
    plt.title("Web Üzerinde Python Grafiği (Sinüs Dalgası)")
    plt.grid(True)
    
    # 2. Resmi Dosyaya Kaydetmek Yerine HAFIZAYA (RAM) Kaydet
    # (Bu yöntem diski kirletmez, daha hızlıdır)
    resim_kutusu = io.BytesIO()
    plt.savefig(resim_kutusu, format='png')
    resim_kutusu.seek(0) # Kutunun başına sar (okumak için)
    
    return resim_kutusu

@app.get("/")
async def ana_sayfa():
    # 3. Web Sitesine Resmi Gönder
    resim = grafik_ciz()
    return StreamingResponse(resim, media_type="image/png")

if __name__ == "__main__":
    print("Sunucu başlatılıyor... http://127.0.0.1:8000 adresine gidin.")
    uvicorn.run(app, host="127.0.0.1", port=8000)
