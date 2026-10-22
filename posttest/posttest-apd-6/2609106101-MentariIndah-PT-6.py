import os

#DATA AKUN
akun = { 
    "admin": {
        "password": "2004",
        "role": "admin"
    }
}
#DATA PRODUK KOSMETIK
produk_kosmetik = { 
    1: {
        "nama" : "lip Tint",
        "merek": "Wardah",
        "kategori": "Makeup",
        "harga": 45000,
        "stok": 10
    },
    2: {
        "nama" : "Sunscreen",
        "merek" : "Azarine",
        "kategori" : "Skincare",
        "harga" :  120000,
        "stok" : 8
    },
    3: {
        "nama" : "Moisturizer", 
        "merek" : "Skintific",
        "kategori" : "Skincare",
        "harga" : 120000,
        "stok" : 8
    },
    4: {
        "nama" : "Skin Tint",
        "merek" : "Esqa",
        "kategori" : "Makeup",
        "harga" : 150000,
        "stok" : 10
    }
}

#NOMOR PRODUK BERKUTNYA
id_produk = 5

#MENU UTAMA
while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 40)
    print("         SISTEM MANAJEMEN KOSMETIK          ")
    print("=" * 40)
    print("[1] Login")
    print("[2] Register")
    print("[3] Keluar")
    print("=" * 40)

    pilihan = input("Pilih menu (1-3): ")

    #LOGIN
    if pilihan == "1":
        print("\n========== LOGIN ==========")

        username = input("Username: ").strip().lower()
        password = input("Password: ")

        login_berhasil = False
        role = "" 

        if username in akun:
            if password == akun[username]["password"]:
                login_berhasil = True
                role = akun[username]["role"]

        if login_berhasil == True:
            print("\nLogin Berhasil!")
            print("Selamat datang", username)
            input("\nTekan Enter untuk melanjutkan...")

            #MENU SETELAH LOGIN
            while True:
                os.system("cls" if os.name == "nt" else "clear")

                print("=" * 40)
                print("     MANAJEMEN PRODUK KOSMETIK        ")
                print("=" * 40)

                if role == "admin":
                    print("[1] Tambah Produk")
                    print("[2] Lihat Produk")
                    print("[3] Ubah Produk")
                    print("[4] Hapus Produk")
                    print("[5] Cari Produk")
                    print("[6] Logout")
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
                        print("\n========== TAMBAH PRODUK ==========")
                        nama = input("Nama produk: ").strip()
                        merek = input("Merek Produk: ").strip()
                        kategori = input("Kategori: ").strip()
                        stok = input("Jumlah stok: ").strip()
                        harga = input("Harga: ").strip()

                        produk_ada = False

                        for produk in produk_kosmetik.values():
                            if (nama.lower() == produk["nama"].lower()
                                    and merek.lower() ==produk["merek"].lower()):
                                produk_ada = True
                                break 
                        if nama == "" or merek == "" or kategori == "":
                            print("\nData produk tidak boleh kosong!")
                        elif not harga.isdigit() or not stok.isdigit():
                            print("Harga dan stok harus berupa angka!")
                        elif int(harga) <= 0: 
                            print("\nHarga harus lebih dari 0!")
                        elif produk_ada == True:
                            print("\nProduk dengan nama dan merek tersebut sudah terdaftar!")
                        else: 
                            produk_kosmetik[id_produk] = {
                                "nama" : nama,
                                "merek" : merek,
                                "kategori" : kategori,
                                "harga" : int(harga),
                                "stok" : int(stok)
                            }
                            id_produk += 1
                            print("\nProduk berhasil ditambahkan!")
                #READ 
                    elif menu == "2":
                        print("========= DAFTAR PRODUK ==========")
                        if len(produk_kosmetik) == 0:
                            print("Belum ada produk")
                        else:
                            for nomor, produk in produk_kosmetik.items():
                                print("\nNomor produk : ", nomor)
                                print("Nama Produk    : ", produk["nama"])
                                print("Merek          :", produk["merek"])
                                print("Kategori       :", produk["kategori"])
                                print("Harga          :", produk["harga"])
                                print("Stok           :", produk["stok"])
                #UPDATE
                    elif menu == "3":
                        print("\n========= UBAH PRODUK =========")
                        if len(produk_kosmetik) == 0:
                         print("Belum ada produk yang dapat diubah.")
                        else:
                            for nomor, produk in produk_kosmetik.items():
                                print(nomor, ".", produk["nama"], "-", produk["merek"])

                            nomor = input("\nNomor produk yang ingin diubah: ")

                            if not nomor.isdigit():
                                print("\nNomor harus berupa angka!")

                            elif int(nomor) not in produk_kosmetik:
                                print("\nNomor produk tidak ditemukan!") 
                            else:
                                nomor = int(nomor)
                                print("\nMasukkan data produk baru")

                                nama = input("Nama Produk: ").strip()
                                merek = input("Merek Produk: ").strip()
                                kategori = input("Kategori: ").strip()
                                harga = input("Harga: ").strip()
                                stok = input("Jumlah Stok: ").strip()

                                produk_ada = False

                                for id_lain, produk in produk_kosmetik.items():
                                    if id_lain != nomor:
                                        if (nama.lower() == produk["nama"].lower()
                                                and merek.lower() == produk["merek"].lower()):
                                            produk_ada = True
                                            break

                                if nama == "" or merek == "" or kategori == "":
                                    print("\nData produk tidak boleh kosong!")
                                elif not harga.isdigit() or not stok.isdigit():
                                    print("\nHarga dan stok harus berupa angka!")
                                elif int(harga) <=0:
                                    print("\nHarga harus lebih dari 0!")

                                elif produk_ada == True:
                                    print("\nProduk dengan nama dan merek tersebut sudah terdaftar!")

                                else: 
                                    produk_kosmetik[nomor] = {
                                        "nama" : nama,
                                        "merek" : merek,
                                        "kategori" : kategori,
                                        "harga" : int(harga),
                                        "stok" : int(stok)
                                    }

                                    print("\nProduk berhasil diubah!")

                #DELETE 
                    elif menu == "4":
                        print("\n========= HAPUS PRODUK =========")

                        if len(produk_kosmetik) == 0:
                            print("Belum ada produk yang dapat dihapus.")
                        else:
                            for nomor, produk in produk_kosmetik.items():
                                print(nomor, ".", produk["nama"], "-", produk["merek"])
                            nomor = input("\nNomor produk yang ingin dihapus: ")

                            if not nomor.isdigit():
                                print("\nNomor harus berupa angka!")

                            elif int(nomor) not in produk_kosmetik:
                                print("\nNomor produk tidak ditemukan!")

                            else:
                                nomor = int(nomor) 

                                print("\nNama Produk:", produk_kosmetik[nomor]["nama"])
                                print("Merek        :", produk_kosmetik[nomor]["merek"])

                                konfirmasi = input("Yakin ingin menghapus? (Ya/Tidak): ").strip().lower()

                                if konfirmasi == "ya":
                                    del produk_kosmetik[nomor]
                                    print("\nProduk berhasil dihapus!")
                                else:
                                    print("\nPenghapusan dibatalkan.")
                #SEARCH
                    elif menu == "5":
                        print("\n========= CARI PRODUK =========")
                        cari = input("Nama Produk: ").strip().lower()
                        ditemukan = False
                        if cari == "":
                            print("\nNama produk tidak boleh kosong!")
                        else:
                            for nomor, produk in produk_kosmetik.items():
                                if cari in produk["nama"].lower():
                                    print("\nNomor produk :", nomor)
                                    print("Nama          :",produk["nama"])
                                    print("Merek         :",produk["merek"])
                                    print("Kategori      :",produk["kategori"])
                                    print("Harga         : Rp",produk["harga"])
                                    print("Stok          :", produk["stok"])

                                    ditemukan = True
                            if ditemukan == False:
                                print("\nProduk tidak ditemukan!")
                #LOGOUT ADMIN
                    elif menu == "6":
                        print("\nLogout berhasil!")
                        input("\nTekan Enter untuk kembali ke menu utama...")
                        break
                    else: 
                        print("\nPilihan tidakk tersedia!")

                #MENU USER BIASA
                else: 
                #READ
                    if menu == "1":
                        print("\n========= DAFTAR PRODUK ========")

                        if len(produk_kosmetik) == 0:
                            print("Belum ada produk.")
                        else:
                            for nomor, produk in produk_kosmetik.items():
                                print("\nNomor Produk :", nomor)
                                print("Nama           :", produk["nama"])
                                print("Merek          :", produk["merek"])
                                print("Kategori       :", produk["kategori"])
                                print("Harga          :", produk["harga"])
                                print("Stok           :", produk["stok"])

                #SEARCH
                    elif menu == "2":
                        print("\n=========  CARI PRODUK ========")

                        cari = input("Nama produk: ").strip().lower()
                        ditemukan = False

                        if cari == "":
                                print("\nNama produk tidak boleh kosong!")
                        else: 
                            for nomor, produk in produk_kosmetik.items():
                                if cari in produk["nama"].lower():
                                    print("\nNomor produk :", nomor)
                                    print("Nama           :", produk["nama"])
                                    print("Merek          :", produk["merek"])
                                    print("Kategori       :", produk["kategori"])
                                    print("Harga          : Rp", produk["harga"])
                                    print("Stok          :", produk["stok"])

                                    ditemukan = True
                            if ditemukan == False:
                                    print("\nProduk tidak ditemukan!")

                #LOGOUT USER
                    elif menu == "3":
                        print("\nLogout berhasil!")
                        input("Tekan Enter untuk kembali ke menu utama...")
                        break

                    else:
                        print("\nPilihan tidak tersedia!")

                #JEDA SEBELUM KEMBALI KE MENU
                input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("\nLogin gagal! Username atau password salah")
            input("\nTekan Enter untuk kembali ke menu utama...")

    #REGISTER
    elif pilihan == "2":
        print("\n========== REGISTER =========")
        username_baru = input("Masukkan username: ").strip().lower()
        password_baru = input("Masukkan password: ").strip()

        if username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong!")

        elif username_baru in akun:
            print("Username sudah digunakan!")

        else: 
            akun[username_baru] = {
                "password" : password_baru,
                "role": "user"
            }
            print("\nRegister berhasil!")
            print("Silakan login menggunakan akun baru.")
        input("\nTekan Enter untuk kembali ke menu utama...")
            

    #KELUAR PROGRAM
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program!")
        break
    else: 
        print("\nPilihan tidak tersedia!")
        input("Tekan Enter untuk melanjutkan...")
