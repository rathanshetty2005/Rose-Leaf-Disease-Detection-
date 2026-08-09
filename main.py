import os
import random
from PIL import Image
import matplotlib.pyplot as plt

dataset_path = "dataset/train"
classes = os.listdir(dataset_path)

plt.figure(figsize=(15, 8))

plot_index = 1

for disease in classes:
    disease_path = os.path.join(dataset_path, disease)

    images = os.listdir(disease_path)

    if len(images) == 0:
        print(f"{disease} folder is empty. Skipping...")
        continue

    image_name = random.choice(images)
    image_path = os.path.join(disease_path, image_name)

    img = Image.open(image_path)

    plt.subplot(3, 3, plot_index)   # 3×3 grid supports up to 9 classes
    plt.imshow(img)
    plt.title(disease)
    plt.axis("off")

    plot_index += 1
    
plt.tight_layout()
plt.show()