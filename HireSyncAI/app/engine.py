import fitz  # PyMuPDF: PDF dosyalarından metin ayıklamak için
import docx2txt  # Word (.docx) dosyalarından metin ayıklamak için
import spacy  # NLP: Doğal Dil İşleme, yetenek ayıklama ve veri temizleme için
from sklearn.feature_extraction.text import TfidfVectorizer  # Metinleri matematiksel vektörlere çevirmek için
from sklearn.metrics.pairwise import cosine_similarity  # İki metin arasındaki benzerliği (skoru) hesaplamak için
import re  # Regex: E-posta, telefon ve özel karakterleri temizlemek için

# 1. ADIM: NLP Modelini Yükleme
# İngilizce dil modelini (en_core_web_sm) yüklüyoruz. Bu model, metindeki kelimelerin 
# rollerini (isim, fiil vb.) ve önemli varlıkları (Entity) tanımamızı sağlar.
try:
    nlp = spacy.load("en_core_web_sm")
except:
    # Eğer model yüklü değilse hata vermemesi için önlem
    pass

# 2. ADIM: Dosya Okuma Fonksiyonları
def extract_text(file_path):
    """
    Gelen dosyanın uzantısına göre (PDF veya DOCX) metin okuma işlemini başlatır.
    """
    # - PDF ise fitz.open(file_path) ile sayfaları dön ve metni birleştir.
    # - DOCX ise docx2txt.process(file_path) ile tüm içeriği stringe çevir.
    pass

# 3. ADIM: Yetenek Ayıklama (NLP NER)
def get_skills(text):
    """
    NLP kullanarak metindeki teknik yetenekleri ayıklar.
    """
    # - Metni nlp() fonksiyonundan geçir.
    # - Önceden tanımlanmış yetenek listesi veya NER (Named Entity Recognition) kullanarak 
    #   'Python', 'SQL', 'FastAPI' gibi kelimeleri cımbızla çek.
    pass

# 4. ADIM: Benzerlik Skoru (Cosine Similarity)
def calculate_score(cv_text, job_description):
    """
    CV ile İş İlanı arasındaki matematiksel uyumluluk puanını hesaplar.
    """
    # - TfidfVectorizer ile her iki metni de sayılara (vektörlere) dönüştür.
    # - cosine_similarity fonksiyonu ile bu iki vektör arasındaki açıyı hesapla.
    # - Sonucu 0 ile 100 arasında bir yüzdeye çevir.
    pass
