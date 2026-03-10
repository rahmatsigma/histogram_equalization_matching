import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

# 1. Load citra grayscale bebas
img = cv2.imread('source.jpg', cv2.IMREAD_GRAYSCALE)
img_target = cv2.imread('target.jpg', cv2.IMREAD_GRAYSCALE)

if img is None or img_target is None:
    print("Error")
    exit()

# 2. Implementasi Histogram Equalization 
# Hitung histogram
hist_manual, bins = np.histogram(img.flatten(), 256, [0, 256])
# HitungCDF
cdf = hist_manual.cumsum()
# Normalisasi CDF agar rentangnya 0-255
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf_final = np.ma.filled(cdf_m, 0).astype('uint8')

# Mapping nilai piksel citra asli dengan nilai CDF yang baru
img_manual_eq = cdf_final[img]

# 3. Implementasi Histogram Equalization 
img_cv2_eq = cv2.equalizeHist(img)

# 4. Melakukan Histogram Specification\
# Menggunakan library skimage untuk mencocokkan histogram img dengan img_target
img_matched = exposure.match_histograms(img, img_target).astype('uint8')

# Fungsi bantuan untuk plot gambar dan histogram 
def show_separate_figure(image, title):
    # Membuat figure baru setiap kali fungsi dipanggil
    plt.figure(figsize=(10, 4))
    plt.suptitle(title, fontsize=14, fontweight='bold')
    
    # Menampilkan Gambar di kiri
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    
    # Menampilkan Histogram di kanan
    plt.subplot(1, 2, 2)
    plt.hist(image.flatten(), 256, [0, 256], color='black')
    plt.title('Histogram')
    plt.xlim([0, 256])
    
    plt.tight_layout()

# 5. Memanggil fungsi 
show_separate_figure(img, '1. Citra Awal')
show_separate_figure(img_manual_eq, '2. Equalization (Manual)')
show_separate_figure(img_cv2_eq, '3. Equalization (Library OpenCV)')
show_separate_figure(img_target, '4. Citra Target (Referensi)')
show_separate_figure(img_matched, '5. Hasil Histogram Specification (Matching)')

# Menampilkan semua 
print("Menampilkan figure")
plt.show()