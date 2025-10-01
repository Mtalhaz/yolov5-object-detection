import torch
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ YOLOv5 modelini yükle (hazır model)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# 2️⃣ Test resmi
img = "sokak.jpg"

# 3️⃣ Nesne tespiti
results = model(img)

# 4️⃣ Tespit tablosu
df = results.pandas().xyxy[0]

# 5️⃣ İnsan ve taşıtları filtrele
interested_classes = ['person', 'car', 'truck', 'bus', 'motorbike']
df_filtered = df[df['name'].isin(interested_classes)]
print(df_filtered)

# 6️⃣ Görselleştirme (YOLOv5 kendi fonksiyonunu kullanır, yeni pencerede açılır)
results.show()

# 7️⃣ Sınıf dağılımı grafiği
class_counts = df_filtered['name'].value_counts()
class_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Tespit Edilen İnsan ve Taşıtların Dağılımı")
plt.xlabel("Nesne Sınıfı")
plt.ylabel("Adet")
plt.show(block=True)

