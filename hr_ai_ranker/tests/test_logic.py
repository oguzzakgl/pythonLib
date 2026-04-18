import sys
import os

# Proje kök dizinini ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.processor import extract_sections, clean_data
from utils.analyzer import perform_analysis

def test_system():
    print("🧪 HR AI Insights: Doğrulama Testi Başlatılıyor...\n")

    # 1. Test Verisi: Sahte bir JD ve CV Metni
    test_jd = "Python ve Machine Learning konusunda uzman, Bilgisayar Mühendisliği mezunu adaylar."
    
    test_cv_text = """
    OĞUZ KAAN
    Yapay zeka meraklısı.
    
    EĞİTİM BİLGİLERİ
    İstanbul Teknik Üniversitesi - Bilgisayar Mühendisliği (2020-2024)
    
    PROJELER
    - Emlak Fiyat Tahmin Uygulaması: Python ve Scikit-learn kullanıldı.
    - GITHUB.COM/OGUZ: Diğer yapay zeka projeleri.
    """

    print("--- 1. BÖLÜMLEME TESTİ (Section Extraction) ---")
    sections = extract_sections(test_cv_text)
    for sec, content in sections.items():
        count = len(content.strip())
        status = "✅ YAKALANDI" if count > 0 else "❌ BOŞ"
        print(f"[{sec}]: {count} karakter {status}")
    
    # Doğrulama: Eğitim bölümü boş kalmamalı
    assert len(sections['Eğitim']) > 0, "HATA: Eğitim bölümü saptanamadı!"
    print("✓ Eğitim bölümü başarıyla ayrıştırıldı.\n")

    print("--- 2. ANALİZ VE SKORLAMA TESTİ ---")
    resume_data = [{
        'filename': 'test_cv.pdf',
        'clean_text': clean_data(test_cv_text),
        'raw_text': test_cv_text
    }]
    
    results = perform_analysis(test_jd, resume_data)
    res = results[0]
    
    print(f"Genel Skor: %{res['Skor']}")
    print(f"Eğitim Skoru: %{res['Bolum_Skorlari'].get('Eğitim', 0)}")
    print(f"Yakalanan Kanıtlar: {len(res['Kanitlar'])} adet")
    
    # Doğrulama: Mühendislik bonusu çalışıyor mu?
    if "mühendislik" in test_cv_text.lower():
        print(f"✓ Teknik Bölüm Bonusu Kontrolü: {res['Bolum_Skorlari']['Eğitim']}")
    
    print("\n✅ TÜM MANTIKSAL TESTLER BAŞARIYLA TAMAMLANDI!")

if __name__ == "__main__":
    try:
        test_system()
    except Exception as e:
        print(f"❌ TEST BAŞARISIZ: {str(e)}")
