#praktikum = "orsikom"

#if praktikum == "apd":
   # print("kamu lagi mengikuti praktikum apd sekarang")
#else:
    #print("kamu mengikuti praktikum lain")#

# umur = int(input("masukkan umur kalian :"))

# if umur > 17:
#     print("kamu sudah legal")
# else:
#     print("kamu belum cukup umur")

# Input jenis kendaraan dari user
# kendaraan = input("Masukkan jenis kendaraan anda: ") .lower()
# # Misalnya, kendaraan = "mobil"
# # Percabangan
# if kendaraan == "mobil":
#     tarif_parkir = 10000
# elif kendaraan == "motor":
#     tarif_parkir = 5000
# else:
#     tarif_parkir = 15000
# # Menampilkan tarif parkir yang harus dibayar
# print("Tarif parkir yang harus dibayar:", tarif_parkir)

# Bentuk Ternary Operator
umur = 20
status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print(status)

#Program Merchandise
nama = "Uzumaki Tatang"
total = int(input("Masukkan total pembayaran Anda: Rp"))
if total > 200000:
    diskon = 30
elif total > 100000:
    diskon = 10
else:
    diskon = 0
print ("Nama Pelanggan:", nama)
print ("Total pembelian:", total)
print ("Selamat Anda mendapatkan diskon sebesar:", diskon, "%")

