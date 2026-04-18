"""
HR AI Ranker - Test CV Jeneratörü
Farklı profillerde 10 adet sahte CV üretir.
"""
from fpdf import FPDF
import os

# Sahte aday profilleri
candidates = [
    {
        "name": "Ahmet Yılmaz",
        "email": "ahmet.yilmaz@gmail.com",
        "phone": "+90 532 456 78 90",
        "linkedin": "linkedin.com/in/ahmetyilmaz",
        "github": "github.com/ahmetyilmaz",
        "profil": "Python ve Makine Ogrenmesi alaninda 3 yillik deneyime sahip bir Bilgisayar Muhendisiyim. Veri bilimi ve yapay zeka projeleri gelistirmeyi hedefliyorum.",
        "egitim": "Istanbul Teknik Universitesi - Bilgisayar Muhendisligi (2019-2023)\nNot Ortalamasi: 3.45/4.00",
        "projeler": "Emlak Fiyat Tahmin Uygulamasi\nTeknolojiler: Python, Scikit-Learn, Pandas, Streamlit\nRandom Forest algoritmasi ile emlak fiyatlarini tahmin eden yapay zeka uygulamasi gelistirdim.\n\nDuygu Analizi Sistemi\nTeknolojiler: Python, NLTK, TensorFlow\nSosyal medya verilerinden duygu analizi yapan NLP projesi.",
        "deneyim": "ABC Teknoloji A.S. - Junior Veri Bilimci (2023-Devam)\nMusteri segmentasyonu ve churn tahmin modelleri gelistirdim.\nPandas ve Scikit-Learn ile veri pipeline'lari kurdum.",
        "yetenekler": "Python, Pandas, NumPy, Scikit-Learn, TensorFlow, SQL, Git, Docker, Streamlit, FastAPI"
    },
    {
        "name": "Elif Kara",
        "email": "elif.kara@outlook.com",
        "phone": "+90 545 123 45 67",
        "linkedin": "linkedin.com/in/elifkara",
        "github": "github.com/elifkara",
        "profil": "Frontend gelistirme ve UI/UX tasarimi konusunda tutkulu bir yazilim muhendisiyim. React ve modern web teknolojileri ile kullanici deneyimini on plana koyan projeler gelistiriyorum.",
        "egitim": "Bogazici Universitesi - Yazilim Muhendisligi (2018-2022)\nNot Ortalamasi: 3.72/4.00",
        "projeler": "E-Ticaret Platformu\nTeknolojiler: React, Node.js, MongoDB, Stripe\nTam kapsamli bir e-ticaret web uygulamasi gelistirdim.\n\nPortfoy Web Sitesi Generatoru\nTeknolojiler: Next.js, Tailwind CSS, Vercel\nKullanicilarin drag-and-drop ile portfolyo olusturabilecegi bir platform.",
        "deneyim": "XYZ Digital - Frontend Developer (2022-Devam)\nReact ve TypeScript ile kurumsal web uygulamalari gelistirdim.\nCI/CD pipeline'lari kurdum ve kod kalitesini artirdim.",
        "yetenekler": "React, TypeScript, JavaScript, Next.js, Tailwind CSS, Node.js, MongoDB, Git, Figma, REST API"
    },
    {
        "name": "Mehmet Demir",
        "email": "mehmet.demir@hotmail.com",
        "phone": "+90 555 987 65 43",
        "linkedin": "linkedin.com/in/mehmetdemir",
        "github": "",
        "profil": "Siber guvenlik ve ag yonetimi alaninda uzmanlasmis bir BT profesyoneliyim. Kurumsal ag altyapilarinin guvenligi ve izlenmesi konusunda deneyim sahibiyim.",
        "egitim": "Ankara Universitesi - Bilgi Teknolojileri (2017-2021)\nNot Ortalamasi: 3.10/4.00",
        "projeler": "Ag Izleme Paneli\nTeknolojiler: Python, Flask, Grafana\nKurumsal ag trafigini izleyen ve anomali tespiti yapan bir dashboard gelistirdim.",
        "deneyim": "DEF Guvenlik - Siber Guvenlik Uzmani (2021-Devam)\nSIEM sistemlerini yonettim ve guvenlik olaylarini analiz ettim.\nPenetrasyon testleri ve zafiyet taramalari gerceklestirdim.",
        "yetenekler": "Linux, Wireshark, Nmap, Metasploit, Python, Bash, AWS, Firewalls, SIEM, Incident Response"
    },
    {
        "name": "Zeynep Aksoy",
        "email": "zeynep.aksoy@gmail.com",
        "phone": "+90 533 222 33 44",
        "linkedin": "linkedin.com/in/zeynepaksoy",
        "github": "github.com/zeynepaksoy",
        "profil": "Mobil uygulama gelistirme ve cross-platform cozumler konusunda deneyimli bir yazilimciyim. Flutter ve React Native ile kullanici odakli mobil uygulamalar tasarliyorum.",
        "egitim": "ODTU - Bilgisayar Muhendisligi (2019-2023)\nNot Ortalamasi: 3.55/4.00",
        "projeler": "Gider Takip Uygulamasi\nTeknolojiler: Flutter, Dart, Firebase\nKisisel finans yonetimi icin AI destekli mobil uygulama.\n\nSaglik Takip Uygulamasi\nTeknolojiler: React Native, Node.js, PostgreSQL\nHastaların saglik verilerini izleyen mobil platform.",
        "deneyim": "GHI Mobil - Mobil Gelistirici (2023-Devam)\nFlutter ile cross-platform mobil uygulamalar gelistirdim.\nFirebase entegrasyonlari ve push notification sistemleri kurdum.",
        "yetenekler": "Flutter, Dart, React Native, JavaScript, Firebase, SQLite, Git, REST API, Figma, Agile"
    },
    {
        "name": "Can Ozturk",
        "email": "can.ozturk@yandex.com",
        "phone": "+90 542 111 22 33",
        "linkedin": "linkedin.com/in/canozturk",
        "github": "github.com/canozturk",
        "profil": "Backend gelistirme ve mikroservis mimarileri konusunda uzmanlasmis bir yazilim muhendisiyim. Olceklenebilir ve yuksek performansli sistemler tasarliyorum.",
        "egitim": "Yildiz Teknik Universitesi - Bilgisayar Muhendisligi (2016-2020)\nNot Ortalamasi: 3.30/4.00",
        "projeler": "Mikroservis E-Ticaret Altyapisi\nTeknolojiler: Java, Spring Boot, Kubernetes, RabbitMQ\nDagilmis mimari ile olceklenebilir e-ticaret backend sistemi.\n\nGercek Zamanli Chat Uygulamasi\nTeknolojiler: Go, WebSocket, Redis, Docker\nYuksek trafikli mesajlasma altyapisi.",
        "deneyim": "JKL Yazilim - Senior Backend Developer (2020-Devam)\nSpring Boot ve Kubernetes ile mikroservis mimarileri tasarladim.\nCI/CD pipeline'lari ve monitoring sistemleri kurdum.",
        "yetenekler": "Java, Spring Boot, Go, Python, Kubernetes, Docker, PostgreSQL, Redis, RabbitMQ, AWS, Terraform"
    },
    {
        "name": "Selin Yildiz",
        "email": "selin.yildiz@gmail.com",
        "phone": "+90 537 444 55 66",
        "linkedin": "linkedin.com/in/selinyildiz",
        "github": "",
        "profil": "Veri muhendisligi ve ETL surecleri konusunda deneyimli bir profesyonelim. Buyuk veri altyapilari kurarak isletmelerin veri odakli karar almasini sagliyorum.",
        "egitim": "Hacettepe Universitesi - Istatistik (2018-2022)\nNot Ortalamasi: 3.60/4.00",
        "projeler": "Veri Ambari Modernizasyonu\nTeknolojiler: Apache Spark, Airflow, Snowflake\nLegacy veri ambarindan bulut tabanli modern veri platformuna gecis projesi.",
        "deneyim": "MNO Data - Veri Muhendisi (2022-Devam)\nApache Spark ile ETL pipeline'lari gelistirdim.\nAirflow ile veri akis orkestrasyonu kurdum.",
        "yetenekler": "Python, SQL, Apache Spark, Airflow, Snowflake, AWS, Kafka, dbt, Tableau, Power BI"
    },
    {
        "name": "Burak Sahin",
        "email": "burak.sahin@gmail.com",
        "phone": "+90 544 777 88 99",
        "linkedin": "linkedin.com/in/buraksahin",
        "github": "github.com/buraksahin",
        "profil": "DevOps ve bulut altyapi yonetimi konusunda uzmanlasmis bir sistem muhendisiyim. Otomasyon ve altyapi kod olarak yonetimi (IaC) tutkum.",
        "egitim": "Ege Universitesi - Bilgisayar Muhendisligi (2017-2021)\nNot Ortalamasi: 3.20/4.00",
        "projeler": "Kubernetes Cluster Yonetim Araci\nTeknolojiler: Go, Kubernetes, Prometheus, Grafana\nOtomatik olceklendirme ve izleme ozellikleri olan cluster yonetim paneli.",
        "deneyim": "PQR Cloud - DevOps Engineer (2021-Devam)\nAWS ve Azure uzerinde bulut altyapilari tasarladim.\nTerraform ile Infrastructure as Code uyguladim.",
        "yetenekler": "AWS, Azure, Docker, Kubernetes, Terraform, Ansible, Jenkins, GitHub Actions, Python, Bash, Prometheus"
    },
    {
        "name": "Ayse Celik",
        "email": "ayse.celik@gmail.com",
        "phone": "+90 538 333 22 11",
        "linkedin": "linkedin.com/in/aysecelik",
        "github": "github.com/aysecelik",
        "profil": "Yapay zeka ve derin ogrenme alaninda arastirma yapan bir bilgisayar bilimciyim. Dogal dil isleme ve bilgisayarli goru projelerinde deneyim sahibiyim.",
        "egitim": "Sabanci Universitesi - Bilgisayar Bilimi Yuksek Lisans (2020-2022)\nKoc Universitesi - Bilgisayar Muhendisligi Lisans (2016-2020)\nNot Ortalamasi: 3.85/4.00",
        "projeler": "Turkce NLP Modeli\nTeknolojiler: Python, PyTorch, Transformers, HuggingFace\nTurkce metin siniflandirma ve duygu analizi icin fine-tuned BERT modeli.\n\nNesne Tespiti Sistemi\nTeknolojiler: Python, YOLOv8, OpenCV, FastAPI\nGercek zamanli nesne tespiti yapan bilgisayarli goru uygulamasi.",
        "deneyim": "STU AI Lab - AI Researcher (2022-Devam)\nTransformer tabanli modeller uzerinde arastirma yaptim.\nMLOps pipeline'lari ve model deployment surecleri yonettim.",
        "yetenekler": "Python, PyTorch, TensorFlow, Transformers, HuggingFace, OpenCV, Scikit-Learn, MLflow, Docker, FastAPI"
    },
    {
        "name": "Emre Koc",
        "email": "emre.koc@gmail.com",
        "phone": "+90 541 666 77 88",
        "linkedin": "",
        "github": "github.com/emrekoc",
        "profil": "Oyun gelistirme ve 3D grafik programlama konusunda tutkulu bir yazilimciyim. Unity ve Unreal Engine ile interaktif deneyimler olusturuyorum.",
        "egitim": "Bahcesehir Universitesi - Oyun Tasarimi (2019-2023)\nNot Ortalamasi: 3.15/4.00",
        "projeler": "RPG Oyun Projesi\nTeknolojiler: Unity, C#, Blender\nAcik dunya RPG oyunu prototipi.\n\nAR Egitim Uygulamasi\nTeknolojiler: Unity, ARCore, Vuforia\nArttirilmis gerceklik ile interaktif egitim uygulamasi.",
        "deneyim": "VWX Games - Game Developer (2023-Devam)\nUnity ile mobil oyunlar gelistirdim.\nPerformans optimizasyonu ve shader programlama yaptim.",
        "yetenekler": "Unity, C#, Unreal Engine, C++, Blender, Shader Programming, Git, Photoshop, AR/VR, Agile"
    },
    {
        "name": "Deniz Arslan",
        "email": "deniz.arslan@gmail.com",
        "phone": "+90 536 999 88 77",
        "linkedin": "linkedin.com/in/denizarslan",
        "github": "github.com/denizarslan",
        "profil": "Full-stack web gelistirme ve sistem tasarimi konusunda 5 yillik deneyime sahip bir yazilim muhendisiyim. Python ve JavaScript ekosistemlerinde uzmanlasmis olup, olceklenebilir web uygulamalari gelistiriyorum.",
        "egitim": "Bilkent Universitesi - Bilgisayar Muhendisligi (2015-2019)\nNot Ortalamasi: 3.65/4.00",
        "projeler": "HR AI Ranker\nTeknolojiler: Python, Streamlit, Scikit-Learn, Sentence-Transformers\nYapay zeka tabanli CV analiz ve siralama sistemi.\n\nE-Ticaret Mikroservis Platformu\nTeknolojiler: Django, React, PostgreSQL, Docker, Redis\nTam kapsamli e-ticaret platformu.",
        "deneyim": "YZA Tech - Full Stack Developer (2019-Devam)\nDjango ve React ile kurumsal web uygulamalari gelistirdim.\nPostgreSQL veritabani tasarimi ve optimizasyonu yaptim.\nDocker ve CI/CD ile deployment sureclerini otomatiksestirdim.",
        "yetenekler": "Python, Django, FastAPI, JavaScript, React, TypeScript, PostgreSQL, Docker, Redis, Git, AWS, Streamlit, Pandas, Scikit-Learn"
    }
]

def create_cv_pdf(candidate, output_dir):
    pdf = FPDF()
    pdf.add_page()
    
    # Unicode font desteği
    pdf.add_font("DejaVu", "", "C:/Windows/Fonts/arial.ttf", uni=True)
    pdf.set_font("DejaVu", size=10)
    
    # İsim
    pdf.set_font_size(18)
    pdf.cell(0, 12, candidate["name"], new_x="LMARGIN", new_y="NEXT")
    
    # İletişim
    pdf.set_font_size(9)
    contact_line = f"{candidate['phone']} | {candidate['email']}"
    if candidate['linkedin']:
        contact_line += f" | {candidate['linkedin']}"
    if candidate['github']:
        contact_line += f" | {candidate['github']}"
    pdf.cell(0, 6, contact_line, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    
    # Profil
    pdf.set_font_size(12)
    pdf.cell(0, 8, "PROFİL", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_size(10)
    pdf.multi_cell(0, 5, candidate["profil"])
    pdf.ln(3)
    
    # Eğitim
    pdf.set_font_size(12)
    pdf.cell(0, 8, "EĞİTİM", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_size(10)
    pdf.multi_cell(0, 5, candidate["egitim"])
    pdf.ln(3)
    
    # Projeler
    pdf.set_font_size(12)
    pdf.cell(0, 8, "PROJELER", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_size(10)
    pdf.multi_cell(0, 5, candidate["projeler"])
    pdf.ln(3)
    
    # Deneyim
    pdf.set_font_size(12)
    pdf.cell(0, 8, "DENEYİM", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_size(10)
    pdf.multi_cell(0, 5, candidate["deneyim"])
    pdf.ln(3)
    
    # Yetenekler
    pdf.set_font_size(12)
    pdf.cell(0, 8, "YETENEKLER", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_size(10)
    pdf.multi_cell(0, 5, candidate["yetenekler"])
    
    # Kaydet
    filename = candidate["name"].replace(" ", "_") + "_CV.pdf"
    filepath = os.path.join(output_dir, filename)
    pdf.output(filepath)
    print(f"  ✅ {filename} oluşturuldu")
    return filepath

if __name__ == "__main__":
    output_dir = os.path.join("data", "test_cvs")
    os.makedirs(output_dir, exist_ok=True)
    
    print("🚀 Test CV'leri oluşturuluyor...\n")
    
    for c in candidates:
        create_cv_pdf(c, output_dir)
    
    print(f"\n✅ {len(candidates)} adet test CV'si '{output_dir}' klasörüne kaydedildi!")
    print("📂 Bu dosyaları HR AI Ranker'a yükleyerek sistemi test edebilirsiniz.")
