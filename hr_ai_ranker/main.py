import os
import pandas as pd
from utils.reader import extract_text_from_pdf
from utils.processor import clean_data
from utils.analyzer import perform_analysis

def main():
    print("--- HR AI Ranker (CLI Sürümü) ---")
    
    # Dosya yolları
    job_desc_path = "data/job_desc.txt"
    resumes_dir = "data/resumes"
    
    try:
        # 1. İş tanımını yükle
        if not os.path.exists(job_desc_path):
            with open(job_desc_path, "w", encoding="utf-8") as f:
                f.write("Ornek is tanimi: Python, Machine Learning, NLP tecrubesi olan adaylar araniyor.")
            print(f"Uyarı: {job_desc_path} bulunamadı, örnek bir dosya oluşturuldu.")
            
        with open(job_desc_path, "r", encoding="utf-8") as f:
            job_desc_raw = f.read()
        
        job_desc_clean = clean_data(job_desc_raw)
        
        # 2. Resumes klasöründeki PDF'leri listele
        if not os.path.exists(resumes_dir):
            os.makedirs(resumes_dir)
            print(f"Uyarı: {resumes_dir} klasörü oluşturuldu. Lütfen içine PDF ekleyin.")
            return

        resume_files = [f for f in os.listdir(resumes_dir) if f.endswith(".pdf")]
        
        if not resume_files:
            print("Hata: 'data/resumes' içinde PDF dosyası bulunamadı.")
            return
            
        # 3. Her bir CV'yi işle
        resumes_processed = []
        for filename in resume_files:
            file_path = os.path.join(resumes_dir, filename)
            raw_text = extract_text_from_pdf(file_path)
            clean_text = clean_data(raw_text)
            resumes_processed.append({
                'filename': filename,
                'text': clean_text
            })
            
        # 4. Analiz yap
        results = perform_analysis(job_desc_clean, resumes_processed)
        
        # 5. Sonuçları göster
        df = pd.DataFrame(results)
        if not df.empty:
            df = df.sort_values(by="Skor", ascending=False)
            print("\n--- Aday Sıralaması ---")
            print(df.to_string(index=False))
        else:
            print("Analiz için geçerli veri bulunamadı.")
            
    except Exception as e:
        print(f"Sistem hatası: {e}")

if __name__ == "__main__":
    main()
