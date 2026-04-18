import fitz  # PyMuPDF: PDF dosyalarını okumak içi en hızlı ve güçlü kütüphanelerden biridir.
import docx2txt  # Word (.docx) dosyalarını metne çevirmek için kullanılır.
import os

# --- 1. PDF OKUMA MANTIĞI ---
def read_pdf(file_path):
    """
    Bir PDF dosyasını açar ve içindeki tüm metni sayfalar halinde okur.
    """
    if not os.path.exists(file_path):
        return "Dosya bulunamadı!"

    # PDF dosyasını açıyoruz
    doc = fitz.open(file_path)
    full_text = ""

    # Sayfaları tek tek dönüyoruz
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Sayfayı yükle
        full_text += page.get_text()   # Sayfadaki metni ayıkla ve ana metne ekle
    
    return full_text

# --- 2. WORD OKUMA MANTIĞI ---
def read_word(file_path):
    """
    Word dosyasını saniyeler içinde düz metne çevirir.
    """
    # docx2txt kütüphanesi karmaşık Word yapılarını temizleyip sadece metni verir.
    text = docx2txt.process(file_path)
    return text

# --- 3. GENEL DOSYA YÖNETİCİSİ ---
def get_file_content(file_path):
    """
    Dosya uzantısına bakarak doğru fonksiyonu çağırır.
    """
    extension = file_path.split('.')[-1].lower()
    
    if extension == 'pdf':
        return read_pdf(file_path)
    elif extension in ['docx', 'doc']:
        return read_word(file_path)
    else:
        return "Desteklenmeyen dosya formatı!"

# ÖRNEK KULLANIM:
# print(get_file_content("ornek_cv.pdf"))
