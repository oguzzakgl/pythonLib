import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Seaborn daha modern bir görünüm sunar
sns.set_theme(style="darkgrid")

# Örnek Veri: Bir sınıftaki 10 öğrencinin notları
data = pd.DataFrame({
    "Matematik": np.random.randint(40, 100, 20),
    "Fizik": np.random.randint(30, 90, 20),
    "Cinsiyet": np.random.choice(["Kız", "Erkek"], 20)
})

# 1. Dağılım Grafiği (Scatter Plot)
# Matematik vs Fizik notları arasındaki ilişki
plt.figure(figsize=(6, 4))
sns.scatterplot(data=data, x="Matematik", y="Fizik", hue="Cinsiyet", s=100)
plt.title("Matematik vs Fizik Notları İlişkisi")
plt.show()

# 2. Isı Haritası (Heatmap)
# Rastgele bir korelasyon matrisi yapalım
korelasyon = data[["Matematik", "Fizik"]].corr()

plt.figure(figsize=(5, 4))
sns.heatmap(korelasyon, annot=True, cmap="coolwarm")
plt.title("Dersler Arası İlişki Haritası")
plt.show()

# 3. Kutu Grafiği (Box Plot)
# Notların dağılımını görmek için (Medyan, Çeyrekler)
plt.figure(figsize=(6, 4))
sns.boxplot(data=data, x="Cinsiyet", y="Matematik", palette="pastel")
plt.title("Cinsiyete Göre Matematik Başarısı")
plt.show()

# �ZET: Matplotlib tabanl� ancak daha modern ve estetik grafikler sunan Seaborn k�t�phanesi ile veriler aras� ili�kiyi g�steren da��l�m (scatter) ve yo�unluk (heatmap) grafiklerini inceliyoruz.
