import os
#DATA AKUN
akun = [
    ["admin", "2004","admin" ]
]

#DATA PRODUK KOSMETIK
produk_kosmetik = [
    ["Lip Tint", "Wardah", "Makeup", 45000, 10],
    ["Sunscreen", "Azarine", "Skinacre", 65000, 15],
    ["Moisturizer", "Skintific", "Skincare", 120000, 8],
    ["Skin tint", "Esqa", "Makeup", 150000, 10]
]

#MENU UTAMA
while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=======================================")
    print("      SISTEM MANAJEMEN KOSMETIK        ")
    print("=" * 40)
    print("[1] Login")
    print("[2] Register")
    print("[3] keluar")
    print("=" * 40)

    pilihan = input("Pilih menu (1-3): ")

    #lOGIN
    if pilihan == "1":
        print("\n========== LOGIN ==========")
        username = input("Username: ").strip().lower()
        password = input("Password: ")

        login_berhasil = False
        role = ""

        for data_akun in akun:
            if username == data_akun[0] and password == data_akun[1]:
                login_berhasil = True
                role = data_akun[2]
                break
        if login_berhasil == True:
            print("\nLogin berhasil!")   
            print("Selamat datang", username)
            input("\nTekan Enter untuk melanjutkan..")

            #MENU SETELAH LOGIN
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 40)
                print("    MANAJEMEN PRODUK KOSMETIK     ")
                print("=" * 40)

                if role == "admin":
                    print("[1] Tambah Produk")
                    print("[2] Lihat Produk")
                    print("[3] Ubah produk")
                    print("[4] Hapus Produk")
                    print("[5] Cari Produk")
                    print('[6] Logout')
                else:
                    print("[1] Lihat Produk")
                    print("[2] Cari Produk")
                    print("[3] Logout")
                print("=" * 40)
                menu = input("Pilih menu: ")

                #MENU ADMIN 
                if role == "admin":
                    #CREATE 
                    if menu == "1":
                        print("\n======== TAMBAH PRODUK ========")
                        nama = input("Nama Produk: ").strip()
                        merek = input("Merek Produk: ").strip()
                        kategori = input("Kategori: ").strip()
                        harga = input("Harga: ")
                        stok = input("Jumlah Stok: ")

                        produk_ada = False
                        for produk in produk_kosmetik:
                            if nama.lower() == produk[0].lower() and merek.lower() == produk[1].lower():
                                produk_ada = True
                                break
                        if nama == "" or merek == "" or kategori =="":
                            print("\nData produk tidak boleh kosong!")
                        elif not harga.isdigit() or not stok.isdigit():
                            print("\nData dan stok harus berupa angka!")
                        elif int(harga) <= 0:
                            print("\nHarga harus lebih dari 0!")
                        else: 
                            produk_baru = [
                                nama,
                                merek,
                                kategori,
                                int(harga),
                                int(stok)
                            ]
                            produk_kosmetik.append(produk_baru)
                            print("\nProduk berhasil ditambahkan!")
                    #READ
                    elif menu == "2":
                        print("\n========== DAFTAR PRODUK ==========")

                        if len(produk_kosmetik) == 0:
                            print("Belum ada produk.")
                        else: 
                            for i in range(len(produk_kosmetik)):
                                print("\nProduk ke-", i + 1)
                                print("Nama       : ", produk_kosmetik[i][0])
                                print("Merek      : ", produk_kosmetik[i][1])
                                print("Kategori   : ",produk_kosmetik[i][2])
                                print("Harga      : Rp", produk_kosmetik[i][3])
                                print("Stok       : ", produk_kosmetik[i][4])
                    #UPDATE
                    elif menu == "3":
                        print("\n ========== UBAH PRODUK ==========")
                        if len(produk_kosmetik) == 0:
                            print("Belum ada produk yang dapat diubah.")
                        else: 
                            for i in range(len(produk_kosmetik)):
                                print(i + 1, ".", produk_kosmetik[i][0], "-", produk_kosmetik[i][1])

                            nomor = input("\nNomor produk yang ingin diubah: ")
                            if not nomor.isdigit():
                                print("\nNomor harus berupa angka!")
                            elif int(nomor) < 1 or int(nomor) > len(produk_kosmetik):
                                print("\nNomor produk tidak ditemukan!")
                            else:
                                index = int(nomor) - 1

                                print("\nMasukkan data produk baru")
                                nama = input("Nama Produk     : ").strip()
                                merek = input("Merek Produk   : ").strip()
                                kategori = input("Kategori    : ").strip()
                                harga = input("Harga          : ")
                                stok = input("Jumlah Stok     : ")

                                produk_ada = False

                                for i in range(len(produk_kosmetik)):
                                    if i != index:
                                        if nama.lower() == produk_kosmetik[i][0].lower() and merek.lower() == produk_kosmetik[i][1].lower():
                                            produk_ada = True
                                            break
                                if nama == "" or merek == "" or kategori == "":
                                    print("\nData tidak boleh kosong!")
                                elif not harga.isdigit() or not stok.isdigit():
                                    print("\nHarga dan stok harus berupa angka!")
                                elif int(harga) <= 0:
                                    print("\nHarga harus lebih dari 0!")
                                elif produk_ada == True:
                                    print("\nProduk dengan nama dan merek tersebut sudah terdaftar!")
                                else: 
                                    produk_kosmetik[index] =[
                                        nama, 
                                        merek,
                                        kategori,
                                        int(harga),
                                        int(stok)
                                    ]
                                    print("\nProduk berhasil diubah!")
                    #DELETE
                    elif menu == "4":
                        print("\n========== HAPUS PRODUK ==========")
                        if len(produk_kosmetik) == 0:
                            print("belum ada produk yang dapat dihapus.")
                        else: 
                            for i in range(len(produk_kosmetik)):
                                print(i + 1, ".", produk_kosmetik[i][0],"-", produk_kosmetik[i][1])
                            nomor = input("\nNomor produk yang ingin dihapus: ")
                            if not nomor.isdigit():
                                print("\nNomor harus berupa angka!")
                            elif int(nomor) < 1 or int(nomor) > len(produk_kosmetik):
                                print("\nNomor produk tidak ditemukan!")
                            else:
                                index = int(nomor) - 1
                                print("\nProduk: ", produk_kosmetik[index][0])
                                print("Merek: ", produk_kosmetik[index][1])
                                konfirmasi = input("Yakin ingin menghapus? (Ya/Tidak): ").strip().lower()

                                if konfirmasi == "ya":
                                    produk_kosmetik.pop(index)
                                    print("\nProduk berhasil dihapus!")
                                else:
                                    print("\nPenghapusan dibatalkan.")
                    #SEARCH 
                    elif menu == "5":
                        print("\n========== CARI PRODUK ==========")

                        cari = input("Nama produk: ").strip().lower()
                        ditemukan = False
                        if cari == "":
                            print("Nama produk tidak boleh kosong!")
                        else:
                            for produk in produk_kosmetik:
                                if cari in produk[0].lower():
                                    print("\nNama   : ", produk[0])
                                    print("Merek    : ", produk[1])
                                    print("Kategori : ", produk[2])
                                    print("Harga    : ", produk[3])
                                    print("Stok     : ", produk[4])

                                    ditemukan = True
                            if ditemukan == False:
                                print("\nProduk tidak ditemukan!")
                    #LOGOUT ADMIN
                    elif menu == "6":
                        print("\nLogout berhasil!")
                        input("\nTekan enter untuk kembali ke menu utama...")
                        break
                    else:
                        print("\nPiilihan tidak tersedia!")
                #MENU USER BIASA
                else:
                    #READ
                    if menu == "1":
                        print("\n========== DAFTAR PRODUK =========")

                        if len(produk_kosmetik) == 0:
                            print("Belum ada produk.")
                        else: 
                            for i in range(len(produk_kosmetik)):
                                print("\nProduk ke-", i + 1)
                                print("Nama      : ", produk_kosmetik[i][0])
                                print("Merek     : ", produk_kosmetik[i][1])
                                print("Kategori  : ", produk_kosmetik[i][2])
                                print("Harga     : Rp", produk_kosmetik[i][3])
                                print("Stok      : ", produk_kosmetik[i][4])
                    #SEARCH
                    elif menu == "2":
                        print("\n========== CARI PRODUK ==========")

                        cari = input("Nama Produk: ").strip().lower()
                        ditemukan = False

                        if cari == "":
                            print("\nNama produk tidak boleh kosong!")
                        else: 
                            for produk in produk_kosmetik:
                                if cari in produk[0].lower():
                                    print("\nNama      : ", produk[0])
                                    print("Merek       : ", produk [1])
                                    print("Kategori    : ", produk[2])
                                    print("Harga       : ", produk[3])
                                    print("Stok        : ", produk[4])

                                    ditemukan = True
                            if ditemukan == False:
                                print("\nProduk tidak ditemukan!")
                    #LOGOUT USER
                    elif menu == "3":
                        print("\nLogout berhasil!")
                        input("\nTekan Enter untuk kembali ke menu utama...")
                        break
                    else:
                        print("\nPilihan tidak tersedia!")

     #JEDA SEBELUM KEMBALI KE MENU UTAMA
                input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("\nLogin gagal! Username atau Passowrd salah.")
        input("\nTekan Enter untuk kembali ke menu utama...")

    #REGISTER 
    elif pilihan == "2":
        print("\n========== REGISTER ==========")

        username_baru = input("Buat username: ").strip().lower()
        password_baru = input("Buat password: ").strip()

        username_ada = False

        for data_akun in akun:
            if username_baru == data_akun[0]:
                username_ada = True
                break
        if username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong!")
        elif username_ada == True:
            print("\nUsername sudah digunakan!")
        else:
            akun.append([username_baru, password_baru, "user"])

            print("\nRegister berhasil!")
            print("Silakan login menggunakan akun baru.")
            input("\nTekan Enter untuk kembali ke menu utama...")
    #KELUAR PROGRAM
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program!")
        break
    else: 
        print("\nPilihan tidak tersedia!")
        input("\nTekan Enter untuk melanjutkan...")
        