import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. NLP İLE ANAHTAR KELİME (SKILL) AYIKLAMA ---
def extract_skills_demo(text):
    """
    spaCy kullanarak bir metinden önemli kelimeleri nasıl çekeriz?
    """
    # Modeli yüklüyoruz
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Örnek: Sadece isimleri (NOUN) ve özel isimleri (PROPN) çekiyoruz.
    # Genelde yetenekler (Python, SQL vb.) bu kategoridedir.
    found_keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    
    return list(set(found_keywords)) # Tekrar edenleri temizle

# --- 2. METİN BENZERLİĞİ (SCORE) HESAPLAMA ---
def calculate_similarity_demo(text1, text2):
    """
    İki metnin (CV ve İş İlanı) birbirine ne kadar benzediğini matematiksel olarak ölçer.
    """
    # TF-IDF: Kelimelerin metin içindeki önemini sayısallaştırır.
    vectorizer = TfidfVectorizer()
    
    # İki metni de vektöre (sayı dizisine) çeviriyoruz
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    
    # Cosine Similarity: İki vektör arasındaki 'açıyı' ölçer.
    # 1.0 tam eşleşme, 0.0 hiç benzerlik yok demektir.
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return round(similarity[0][0] * 100, 2) # Yüzdelik dilime çevir

# ÖRNEK:
cv = "I am a Python developer with experience in FastAPI and SQL."
job = "Looking for a developer familiar with Python and SQL databases."
# print(f"Uyum Skoru: %{calculate_similarity_demo(cv, job)}")
