print("Selamat datang di Rental PS!")
print("Silakan login terlebih dahulu: ")
print()

nama = input("Masukkan nama panggilan Anda: ") .lower()
nim = input ("Masukkan 3 digit terakhi NIM Anda: " )

if nama == "mentari" and nim == "101":
    print ()
    print ("Login berhasil!")
    print ("Selamat datang", nama)
    print()

    print("Silakan pilih jenis konsol")
    print ("1. PS4      = 10000/jam")
    print ("2. PS4 Pro  = 15000/jam")
    print ("3. PS5      = 20000/jam")
    
    pilihan = int(input("Silakan masukkan pilihan konsol Anda (1-3): "))

    if pilihan == 1:
        konsol = "PS4"
        harga = 10000
    elif pilihan == 2:
        konsol = "PS4 Pro"
        harga = 15000
    elif pilihan == 3:
        konsol = "PS5"
        harga = 20000
    else:
        print("Pilihan tidak tersedia.")
        print("Program selesai.")
    if pilihan == 1 or pilihan == 2 or pilihan == 3:
        jam = int(input("Masukkan durasi yang Anda inginkan: "))
        total = harga * jam 

    if jam >= 5:
        diskon = total * 8 / 100
    elif jam >= 3:
        diskon = total * 5 / 100
    else:
        diskon = 0

    print()
    print("Pilih hari sewa: ")
    print("1. Weekday")
    print("2. Weekend")

    hari = int(input("Masukkan pilihan(1/2): "))
    if hari == 1:
        weekend = 0
        jenis_waktu = "weekday"
    elif hari == 2:
        weekend = total * 10/100
        jenis_waktu = "weekend"   
    else:
        weekend = 0
        jenis_waktu = "Tidak diketahui"

    total_bayar = total - diskon + weekend 

    print()
    print("==== STRUK PENYEWAAN PS ====")
    print("Nama pelanggan        :", nama)
    print("NIM pelanggan         :", nim)
    print("Jenis Konsol          :", konsol)
    print("Waktu sewa            :", jenis_waktu)
    print("Jumlah jam            :", jam)   
    print("Total harga           :Rp", total)
    print("Diskon                :Rp", diskon)
    print("Biaya weekend         :Rp", weekend)
    print("Total bayar           :Rp", total_bayar) 


else:
    print()
    print("Login gagal.")
    print("Nama atau NIM Anda salah")
    print("Program selesai.")