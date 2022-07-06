import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
img = plt.imread("frog.jpg")
plt.title(label="Gambar Katak",
          fontsize=40,
          color="m",
          backgroundcolor='r')
plt.imshow(img)
plt.show()