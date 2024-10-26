import numpy as np
import imageio as img
import matplotlib.pyplot as plt

image = img.imread("./source.jpg")

red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

imgRed = np.zeros_like(image)
imgRed[:, :, 0] = red

# Tambahkan kode untuk channel Green
imgGreen = np.zeros_like(image)
imgGreen[:, :, 1] = green

# Tambahkan kode untuk channel Blue
imgBlue = np.zeros_like(image)
imgBlue[:, :, 2] = blue

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(imgRed)
plt.title('Red Channel')

plt.subplot(2, 2, 3)
plt.imshow(imgGreen)
plt.title('Green Channel')

plt.subplot(2, 2, 4)
plt.imshow(imgBlue)
plt.title('Blue Channel')

# Menyesuaikan spasi dan margin antar subplot
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1,
                    wspace=0.3, hspace=0.3)

plt.show()
