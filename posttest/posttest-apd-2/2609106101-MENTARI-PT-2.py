# Data harga merchandise 
merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000
# Biaya bungkus kado
biaya_bungkus = 7500
#Menghitung total harga secara manual
total_harga = merchandise_1 + merchandise_2 + merchandise_3 + merchandise_4 + merchandise_5 + merchandise_6 + biaya_bungkus
# Menghitung rata-rata
rata_rata = total_harga / 6
# NIM
nim = 101
# Membandingkan NIM dengan rata-rata
bolean = nim > rata_rata
# List harga merchandise 
harga_merchandise = [
    merchandise_1,
    merchandise_2,
    merchandise_3,
    merchandise_4,
    merchandise_5,
    merchandise_6
]
# Konversi total harga ke USD
kurs_usd = 17800
total_usd = total_harga / kurs_usd
# Menampilkan barang 2 hingga barang 4 dengan slice index negatif
barang_2_sampai_4 = harga_merchandise[-5:-2]
# Menampilkan semua variabel
print("Merchandise 1:", merchandise_1)
print("Merchandise 2:", merchandise_2)
print("Merchandise 3:", merchandise_3)
print("Merchandise 4:", merchandise_4)
print("Merchandise 5:", merchandise_5)
print("Merchandise 6:", merchandise_6)
print("Biaya bungkus:", biaya_bungkus)
print("Total harga: Rp", total_harga)
print("Rata-rata:", rata_rata)
print("NIM:", nim)
print("Bolean:", bolean)
print("Harga merchandise:", harga_merchandise)
print("Total dalam USD:", total_usd)
print("Barang 2 sampai 4:", barang_2_sampai_4)