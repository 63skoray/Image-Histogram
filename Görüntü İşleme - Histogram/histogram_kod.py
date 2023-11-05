importort cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\Koray\\image.jpg")

# Histogramı hesaplamak için boş bir liste oluşturdum.

histogram = [0] * 256

# Görüntüdeki pikselleri dolaşarak histogramı hesaplamak için çift for döngüsü kullandım.

for i in range(img.shape[0]):
    for v in range(img.shape[1]):
        piksel_degeri = img[i, v, 0]
        histogram[piksel_degeri] += 1

# Histogramı grafiğe aktardım.

plt.bar(range(256), histogram, )
plt.xlim([0, 255])
plt.show()






