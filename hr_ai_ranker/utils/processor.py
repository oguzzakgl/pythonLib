import re

def clean_data(raw_text):
    """
    Metni küçük harfe çevirir ve harf dışı karakterleri temizler.
    Türkçe karakter desteği içerir.
    """
    if not raw_text or not isinstance(raw_text, str):
        return ""
    
    try:
        # Küçük harfe çevir
        text = raw_text.lower()
        
        # Yeni satırları ve sekmeleri boşluğa çevir (Dikey metinler için kritik)
        text = text.replace('\r', ' ').replace('\n', ' ')
        
        # Teknik terimleri korumak için: harfler, sayılar ve bazı sembolleri (+, #, ., -) tut
        text = re.sub(r'[^a-zıüşöçğ0-9\s\+#\.\-]', ' ', text)
        
        # PDF'lerdeki "p y t h o n" veya "o ğ u z" gibi ayrık harfleri birleştirme
        for _ in range(20):
            text = re.sub(r'(^|\s)([a-zıüşöçğ])\s+(?=[a-zıüşöçğ](\s|$))', r'\1\2', text)

        # Eş Anlamlı (Synonym) Eşleştirme
        synonyms = {
            'makine öğrenmesi': 'machine learning',
            'yapay zeka': 'ai artificial intelligence',
            'derin öğrenme': 'deep learning',
            'veri bilimi': 'data science',
            'özgeçmiş': 'cv resume'
        }
        for key, value in synonyms.items():
            text = text.replace(key, value)

        # Birden fazla boşluğu teke indir
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    except Exception as e:
        print(f"⚠️ clean_data hatası: {e}")
        return raw_text.lower().strip() if raw_text else ""

def split_into_sentences(text):
    """
    Metni anlamlı cümlelere böler.
    Teknik terimleri (scikit-learn, veri analizi vb.) koruyacak şekilde böler.
    """
    if not text or not isinstance(text, str):
        return []
    
    try:
        # Önce satır bazlı böl (CV'ler genelde satır bazlı)
        lines = text.split('\n')
        sentences = []
        for line in lines:
            line = line.strip()
            if len(line) < 25:
                continue
            # Aynı satır içinde nokta veya ! ile böl (ama tire ile bölme!)
            parts = re.split(r'[.!?]', line)
            for p in parts:
                p = p.strip()
                if len(p) >= 25:  # En az 25 karakter (anlamlı cümle)
                    sentences.append(p)
        return sentences
    except Exception as e:
        print(f"⚠️ split_into_sentences hatası: {e}")
        return [text]  # En kötü ihtimal: Tüm metni tek cümle olarak döndür

def fix_vertical_text(text):
    """
    Dikey yazılmış veya gereksiz satır başı yapılmış metinleri birleştirir.
    """
    if not text or not isinstance(text, str):
        return ""
    
    try:
        lines = text.split('\n')
        fixed_lines = []
        buffer = ""
        
        for line in lines:
            clean = line.strip()
            if len(clean) == 1:
                buffer += clean
            else:
                if buffer:
                    fixed_lines.append(buffer)
                    buffer = ""
                fixed_lines.append(line)
        
        if buffer:
            fixed_lines.append(buffer)
            
        return '\n'.join(fixed_lines)
    except Exception as e:
        print(f"⚠️ fix_vertical_text hatası: {e}")
        return text

def extract_sections(raw_text):
    """
    Hibrit Bölümleme: Hem başlıklara hem de içerikteki kritik anahtar kelimelere 
    bakarak CV'yi bölümlere ayırır.
    """
    sections = {
        'Profil': '',
        'Eğitim': '',
        'Projeler': '',
        'Deneyim': '',
        'Yetenekler': '',
        'Diğer': ''
    }
    
    if not raw_text or not isinstance(raw_text, str):
        return sections
    
    try:
        # Dikey metinleri onar
        raw_text = fix_vertical_text(raw_text)
        
        # Başlık yakalama listesi (Genişletilmiş)
        headers_map = {
            'Profil': ['HAKKIMDA', 'HAKKINDA', 'ÖZET', 'PROFİL', 'PROFIL', 'SUMMARY', 'OBJECTIVE', 'ABOUT ME', 'KİŞİSEL', 'ABOUT', 'CAREER OBJECTIVE'],
            'Eğitim': ['EĞİTİM', 'EGITIM', 'EDUCATION', 'OKUL', 'ÜNİVERSİTE', 'UNIVERSITE', 'LİSANS', 'LISANS', 'YÜKSEK LİSANS', 'MEZUN', 'STUDENT', 'GRADUAT', 'ACADEMIC', 'SCHOOL', 'AKADEMİK', 'AKADEMIK', 'EĞİTİM BİLGİLERİ', 'EGITIM BILGILERI', 'ÖĞRENİM', 'OGRENIM'],
            'Projeler': ['PROJELER', 'PROJE', 'PROJECTS', 'PROJECT', 'YAPILAN İŞLER', 'ÜRETİLEN', 'PORTFOLIO', 'PORTFÖY', 'APPS', 'APPLICATIONS', 'KİŞİSEL PROJELER', 'SIDE PROJECTS'],
            'Deneyim': ['DENEYİM', 'DENEYIM', 'EXPERIENCE', 'İŞ GEÇMİŞİ', 'IS GECMISI', 'WORK', 'TECRÜBE', 'TECRUBE', 'STAJ', 'INTERNSHIP', 'EMPLOYMENT', 'İŞ DENEYİMİ', 'IS DENEYIMI', 'PROFESYONEL DENEYİM', 'WORK EXPERIENCE', 'CAREER'],
            'Yetenekler': ['YETENEKLER', 'YETKİNLİKLER', 'YETKINLIKLER', 'SKILLS', 'TEKNOLOJİLER', 'TEKNOLOJILER', 'TOOLS', 'ABILITIES', 'SERTİFİKALAR', 'SERTIFIKALAR', 'CERTIFICATES', 'TEKNİK BECERİLER', 'TEKNIK BECERILER', 'TECHNICAL SKILLS', 'BECERİLER', 'BECERILER', 'COMPETENCIES', 'QUALIFICATIONS', 'PROGRAMMING SKILLS'],
            'Diğer': ['REFERANSLAR', 'REFERANS', 'REFERENCES', 'REFERENCE', 'DİĞER', 'DIGER', 'MISC']
        }
        
        # İçerik tabanlı zorunlu atama
        force_triggers = {
            'Profil': ['ALANLARINDA DERİNLEŞEN', 'HEDEFLİYORUM', 'MOTİVE', 'DENEYİMLİ', 'AMACIM', 'KARİYER HEDEFİM'],
            'Eğitim': ['BİLGİSAYAR MÜHENDİSLİĞİ', 'COMPUTER ENGINEERING', 'LİSESİ', 'MÜHENDİSLİK', 'FAKÜLTE', 'BÖLÜM', 'MEZUN', 'GPA', 'BACHELOR', 'MASTER'],
            'Projeler': ['GITHUB.COM', 'KAGGLE.COM', 'PROJECT:', 'GELİŞTİRDİM', 'UYGULAMASI', 'TASARLADIM'],
            'Deneyim': ['A.Ş.', 'ANONİM ŞİRKETİ', 'WORKED AS', 'POZİSYON', 'LTD', 'ŞTİ', 'INTERN'],
            'Yetenekler': ['DİLLER', 'LANGUAGES:', 'STACK:', 'PROGRAMMING', 'PYTHON', 'JAVASCRIPT', 'REACT', 'DJANGO', 'FLUTTER', 'DOCKER']
        }
        
        lines = raw_text.split('\n')
        current_section = 'Diğer'
        
        for line in lines:
            clean_line = line.strip().upper()
            if not clean_line or len(clean_line) < 2:
                continue
                
            found_header = False
            
            if len(clean_line) < 60:
                for section_name, keywords in headers_map.items():
                    if any(kw == clean_line or clean_line.startswith(kw) for kw in keywords):
                        current_section = section_name
                        found_header = True
                        break
            
            if found_header:
                continue
                
            for section_name, triggers in force_triggers.items():
                if any(t in clean_line for t in triggers):
                    current_section = section_name
                    break
            
            sections[current_section] += line + '\n'
        
        # Smart Recovery
        diger_upper = sections['Diğer'].upper()
        
        if not sections['Eğitim'].strip() and ('ÜNİVERSİTE' in diger_upper or 'MÜHENDİSLİK' in diger_upper or 'FAKÜLTE' in diger_upper or 'LİSANS' in diger_upper):
            sections['Eğitim'] = sections['Diğer']
        
        if not sections['Yetenekler'].strip() and ('PYTHON' in diger_upper or 'JAVASCRIPT' in diger_upper or 'SQL' in diger_upper or 'REACT' in diger_upper):
            skill_lines = []
            remaining_lines = []
            for l in sections['Diğer'].split('\n'):
                lu = l.upper()
                if any(kw in lu for kw in ['PYTHON', 'JAVASCRIPT', 'SQL', 'REACT', 'DOCKER', 'GIT', 'HTML', 'CSS', 'JAVA', 'C++', 'FLUTTER', 'DJANGO', 'FLASK', 'NODEJS']):
                    skill_lines.append(l)
                else:
                    remaining_lines.append(l)
            if skill_lines:
                sections['Yetenekler'] = '\n'.join(skill_lines)
                sections['Diğer'] = '\n'.join(remaining_lines)
                
        return sections
        
    except Exception as e:
        print(f"⚠️ extract_sections hatası: {e}")
        sections['Diğer'] = raw_text
        return sections


def extract_contact_info(text):
    """
    Metin içerisinden e-posta, telefon, LinkedIn ve GitHub bilgilerini regex ile ayıklar.
    """
    default_result = {'emails': [], 'phones': [], 'linkedin': [], 'github': []}
    
    if not text or not isinstance(text, str):
        return default_result
    
    try:
        # E-posta regex (Daha katı ve doğru)
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)
        
        # Telefon regex (Uluslararası ve yerel formatlar: +90, 05xx, 5xx)
        phone_pattern = r'(?:\+90|0)?\s*[1-9][0-9]{2}\s*[0-9]{3}\s*[0-9]{2}\s*[0-9]{2}|(?:\+90|0)?\s*[1-9][0-9]{2}\s*[0-9]{3}\s*[0-9]{4}'
        phones = re.findall(phone_pattern, text)
        
        # LinkedIn & GitHub (Kullanıcı adlarını daha temiz yakalar)
        linkedin_pattern = r'linkedin\.com/in/[a-zA-Z0-9_-]+'
        github_pattern = r'github\.com/[a-zA-Z0-9_-]+'
        
        linkedins = re.findall(linkedin_pattern, text, re.IGNORECASE)
        githubs = re.findall(github_pattern, text, re.IGNORECASE)
        
        # Temizleme ve Benzersizleştirme
        unique_emails = sorted(list(set(emails)))
        unique_phones = sorted(list(set([re.sub(r'\s+', '', p) for p in phones])))
        unique_linkedins = sorted(list(set([l.lower() for l in linkedins])))
        unique_githubs = sorted(list(set([g.lower() for g in githubs])))
        
        return {
            'emails': unique_emails,
            'phones': unique_phones,
            'linkedin': [f"https://{l}" if not l.startswith('http') else l for l in unique_linkedins],
            'github': [f"https://{g}" if not g.startswith('http') else g for g in unique_githubs],
            'websites': []
        }
    except Exception as e:
        print(f"⚠️ extract_contact_info hatası: {e}")
        return default_result
