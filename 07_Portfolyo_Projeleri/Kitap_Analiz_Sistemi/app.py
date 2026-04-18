import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Sayfa yapılandırması
st.set_page_config(page_title="Pro Kitap Analiz & AI", layout="wide")

# Başlık ve Açıklama
st.title("🚀 Pro Kitap Analiz & AI Tahmin Sistemi")
st.markdown("""
Bu profesyonel panel; **Veri Filtreleme**, **Dışa Aktarma** ve **Çoklu AI Modeli Karşılaştırma** özelliklerine sahiptir.
""")

# Verileri Yükleme
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "data", "cleaned_books_data.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

df = load_data()

# Model Yükleme (Dinamik)
def load_model(model_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_file = "rf_model.joblib" if model_name == "Random Forest" else "lr_model.joblib"
    path = os.path.join(current_dir, "models", model_file)
    if os.path.exists(path):
        return joblib.load(path)
    return None

# --- Yan Panel (Sidebar) ---
st.sidebar.header("🔍 Kontrol ve Filtreler")
menu = st.sidebar.selectbox("Sayfa Seçin", ["📊 Veri Analizi & Filtreleme", "🤖 AI Tahmin Robotu"])

if df is not None:
    if menu == "📊 Veri Analizi & Filtreleme":
        st.header("📈 Veri Analizi ve Gelişmiş Filtreleme")
        
        # Filtreleme Seçenekleri
        st.sidebar.subheader("🎚️ Filtreler")
        price_range = st.sidebar.slider("Fiyat Aralığı (£)", 
                                        float(df['Price'].min()), 
                                        float(df['Price'].max()), 
                                        (float(df['Price'].min()), float(df['Price'].max())))
        
        min_rating = st.sidebar.select_slider("Minimum Rating ⭐", options=[1, 2, 3, 4, 5], value=1)

        # Filtreleme İşlemi
        filtered_df = df[(df['Price'] >= price_range[0]) & 
                        (df['Price'] <= price_range[1]) & 
                        (df['Rating_Num'] >= min_rating)]

        # İstatistikler
        col1, col2, col3 = st.columns(3)
        col1.metric("Filtrelenmiş Kitap", len(filtered_df))
        col2.metric("Ortalama Fiyat", f"£{filtered_df['Price'].mean():.2f}")
        col3.metric("Ortalama Rating", f"{filtered_df['Rating_Num'].mean():.2f} ⭐")

        # Görselleştirme
        st.subheader("📊 Fiyat Dağılımı (Filtrelenmiş)")
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.histplot(filtered_df['Price'], bins=15, kde=True, ax=ax, color="skyblue")
        col_left, col_mid, col_right = st.columns([1, 2, 1])
        with col_mid:
            st.pyplot(fig)

        # Veri Tablosu
        st.subheader("📋 Veri Listesi")
        st.dataframe(filtered_df[['Title', 'Price', 'Rating', 'Stock']], use_container_width=True)

        # Veri İndirme (CSV)
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8-sig')

        csv_data = convert_df(filtered_df)
        st.download_button(
            label="📄 Filtrelenmiş Veriyi CSV Olarak İndir",
            data=csv_data,
            file_name='filtrelenmiş_kitaplar.csv',
            mime='text/csv',
        )

    elif menu == "🤖 AI Tahmin Robotu":
        st.header("🤖 Yapay Zeka Rating Tahmini (Çoklu Model)")
        
        st.sidebar.subheader("🧠 Model Ayarları")
        selected_model_name = st.sidebar.radio("Tahmin Algoritması", ["Random Forest", "Linear Regression"])
        
        model = load_model(selected_model_name)

        if model:
            with st.form("prediction_form"):
                st.subheader(f"📖 {selected_model_name} ile Tahmin")
                input_title = st.text_input("Kitap Adı", "Örnek Kitap")
                input_price = st.slider("Tahmini Fiyat (£)", 5.0, 100.0, 30.0)
                
                submit = st.form_submit_button("🚀 Reytingi Tahmin Et")
                
                if submit:
                    title_len = len(input_title)
                    prediction = model.predict([[input_price, title_len]])
                    
                    st.success(f"### 🔮 Tahmin ({selected_model_name}): {prediction[0]:.2f} Yıldız")
                    
                    # Yıldız görselleştirme
                    stars = int(round(prediction[0]))
                    st.write("⭐" * stars if stars > 0 else "İstatistiksel olarak 1 yıldızın altında")
                    
                    st.info(f"Model Detayı: Fiyat {input_price} ve başlık uzunluğu {title_len} karakter temel alınarak hesaplandı.")
        else:
            st.error(f"❌ {selected_model_name} dosyası bulunamadı! Lütfen önce model_training.py dosyasını çalıştırın.")

else:
    st.warning("⚠️ Veri seti bulunamadı! Lütfen önce pipeline'ı çalıştırın.")

# Alt Bilgi (Opsiyonel)
# st.sidebar.markdown("---")

# ÖZET: Tüm bu karmaşık süreçleri son kullanıcının görebileceği, filtreleme yapabileceği 
# ve AI ile tahmin yürütebileceği modern ve interaktif bir web dashboard'udur.
