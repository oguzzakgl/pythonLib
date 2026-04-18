import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib
import os

"""
🧠 Makine Öğrenmesi Model Eğitimi (Gelişmiş)
------------------------------------------
Temizlenmiş verileri kullanarak birden fazla model eğitir.
- Random Forest Regressor
- Linear Regression
Hedef: Kitabın fiyatı ve isim uzunluğuna bakarak 'Rating' tahmini yapmak.
"""

def train_models():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    clean_path = os.path.join(current_dir, "data", "cleaned_books_data.csv")
    
    if not os.path.exists(clean_path):
        print(f"❌ Hata: Temizlenmiş veri bulunamadı! Yol: {clean_path}")
        return

    df = pd.read_csv(clean_path)

    # 1. Özellik Seçimi (X) ve Hedef Değişken (y)
    X = df[['Price', 'Title_Length']]
    y = df['Rating_Num']

    # 2. Veriyi Eğitim ve Test olarak ayırma
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modelleri saklayacağımız klasör
    models_dir = os.path.join(current_dir, "models")
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    results = []

    # 3. Model 1: Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    print("🤖 Random Forest eğitiliyor...")
    rf_model.fit(X_train, y_train)
    rf_mae = mean_absolute_error(y_test, rf_model.predict(X_test))
    joblib.dump(rf_model, os.path.join(models_dir, "rf_model.joblib"))
    results.append({"Model": "Random Forest", "MAE": rf_mae})

    # 4. Model 2: Linear Regression
    lr_model = LinearRegression()
    print("📈 Linear Regression eğitiliyor...")
    lr_model.fit(X_train, y_train)
    lr_mae = mean_absolute_error(y_test, lr_model.predict(X_test))
    joblib.dump(lr_model, os.path.join(models_dir, "lr_model.joblib"))
    results.append({"Model": "Linear Regression", "MAE": lr_mae})

    # 5. Sonuçları Karşılaştırma
    print("\n📊 Model Performans Karşılaştırması:")
    for res in results:
        print(f"👉 {res['Model']}: MAE = {res['MAE']:.2f}")

    # Geriye uyumluluk için ana model olarak en iyisini kaydet (veya varsayılan kalsın)
    # Şimdilik rf_model'i varsayılan olarak tutuyoruz
    joblib.dump(rf_model, os.path.join(models_dir, "book_rating_model.joblib"))

    print(f"\n✅ Tüm modeller {models_dir} klasörüne kaydedildi.")

if __name__ == "__main__":
    train_models()

# ÖZET: İki farklı yapay zeka modelini (Random Forest ve Linear Regression) eğitip 
# karşılaştıran ve en iyisini kaydeden 'beyin' katmanıdır.
