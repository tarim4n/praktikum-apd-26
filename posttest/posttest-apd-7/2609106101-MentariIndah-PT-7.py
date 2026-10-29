import os

# VARIABEL GLOBAL

# GLOBAL 1
akun = {
    "admin": {
        "password": "2004",
        "role": "admin"
    }
}

# GLOBAL 2
produk_kosmetik = {
    1: {
        "nama": "Lip Tint",
        "merek": "Wardah",
        "kategori": "Makeup",
        "harga": 45000,
        "stok": 10
    },
    2: {
        "nama": "Sunscreen",
        "merek": "Azarine",
        "kategori": "Skincare",
        "harga": 120000,
        "stok": 8
    },
    3: {
        "nama": "Moisturizer",
        "merek": "Skintific",
        "kategori": "Skincare",
        "harga": 120000,
        "stok": 8
    },
    4: {
        "nama": "Skin Tint",
        "merek": "Esqa",
        "kategori": "Makeup",
        "harga": 150000,
        "stok": 10
    }
}

# GLOBAL 3
id_produk = 5


# FUNGSI DENGAN PARAMETER 1

def cek_login(username, password):
    if username in akun:
        if password == akun[username]["password"]:
            return akun[username]["role"]

    return None


# FUNGSI DENGAN PARAMETER 2

def cari_produk(kata_kunci):
    hasil = {}

    for nomor, produk in produk_kosmetik.items():
        if kata_kunci.lower() in produk["nama"].lower():
            hasil[nomor] = produk

    return hasil

# FUNGSI TANPA PARAMETER 1

def jumlah_produk():
    return len(produk_kosmetik)


# FUNGSI TANPA PARAMETER 2

def hitung_total_stok():
    daftar_stok = []

    for produk in produk_kosmetik.values():
        daftar_stok.append(produk["stok"])

    return jumlahkan_stok(daftar_stok, 0)


# FUNGSI REKURSIF

def jumlahkan_stok(daftar_stok, posisi):
    if posisi == len(daftar_stok):
        return 0

    return daftar_stok[posisi] + jumlahkan_stok(daftar_stok, posisi + 1)


# PROSEDUR 1 - TAMPILKAN PRODUK

def tampilkan_produk():
    print("\n========== DAFTAR PRODUK ==========")

    if jumlah_produk() == 0:
        print("Belum ada produk.")

    else:
        for nomor, produk in produk_kosmetik.items():
            print("\nNomor produk :", nomor)
            print("Nama         :", produk["nama"])
            print("Merek        :", produk["merek"])
            print("Kategori     :", produk["kategori"])
            print("Harga        : Rp", produk["harga"])
            print("Stok         :", produk["stok"])

    print("\nJumlah jenis produk:", jumlah_produk())
    print("Total stok seluruh produk:", hitung_total_stok())


# PROSEDUR 2 - TAMPILKAN MENU

def tampilkan_menu(role):
    print("=" * 40)
    print("      MANAJEMEN PRODUK KOSMETIK")
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


# ERROR HANDLING

def input_angka(pesan, minimal=0):
    try:
        angka = int(input(pesan))

    except ValueError:
        print("\nERROR! Masukkan angka yang benar.")
        return None

    else:
        if angka < minimal:
            print("\nERROR! Angka minimal adalah", minimal)
            return None

        return angka

    finally:
        print("Pemeriksaan input selesai.")


# FUNGSI CEK PRODUK DUPLIKAT

def produk_sudah_ada(nama, merek, nomor_diabaikan=0):
    for nomor, produk in produk_kosmetik.items():

        if nomor != nomor_diabaikan:
            if (nama.lower() == produk["nama"].lower()
                    and merek.lower() == produk["merek"].lower()):
                return True

    return False


# PROSEDUR TAMBAHAN - HASIL PENCARIAN

def tampilkan_hasil(hasil):
    if len(hasil) == 0:
        print("\nProduk tidak ditemukan!")

    else:
        for nomor, produk in hasil.items():
            print("\nNomor produk :", nomor)
            print("Nama         :", produk["nama"])
            print("Merek        :", produk["merek"])
            print("Kategori     :", produk["kategori"])
            print("Harga        : Rp", produk["harga"])
            print("Stok         :", produk["stok"])


# PROGRAM UTAMA

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 40)
    print("      SISTEM MANAJEMEN KOSMETIK")
    print("=" * 40)
    print("[1] Login")
    print("[2] Register")
    print("[3] Keluar")
    print("=" * 40)

    pilihan = input("Pilih menu (1-3): ")

    # LOGIN

    if pilihan == "1":
        print("\n========== LOGIN ==========")

        username = input("Username: ").strip().lower()
        password = input("Password: ")

        role = cek_login(username, password)

        if role is None:
            print("\nLogin gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
            continue

        print("\nLogin berhasil!")
        print("Selamat datang", username)

        input("\nTekan Enter untuk melanjutkan...")


        # MENU SETELAH LOGIN

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            tampilkan_menu(role)

            menu = input("Pilih menu: ")


            # MENU ADMIN

            if role == "admin":


                # CREATE
                if menu == "1":
                    print("\n========== TAMBAH PRODUK ==========")

                    nama = input("Nama produk: ").strip()
                    merek = input("Merek produk: ").strip()
                    kategori = input("Kategori: ").strip()

                    if nama == "" or merek == "" or kategori == "":
                        print("\nData produk tidak boleh kosong!")

                    elif produk_sudah_ada(nama, merek):
                        print("\nProduk dengan nama dan merek tersebut sudah terdaftar!")

                    else:
                        harga = input_angka("Harga: ", 1)

                        if harga is not None:
                            stok = input_angka("Jumlah stok: ", 0)

                            if stok is not None:
                                produk_kosmetik[id_produk] = {
                                    "nama": nama,
                                    "merek": merek,
                                    "kategori": kategori,
                                    "harga": harga,
                                    "stok": stok
                                }

                                id_produk += 1

                                print("\nProduk berhasil ditambahkan!")


                # READ
                elif menu == "2":
                    tampilkan_produk()


                # UPDATE
                elif menu == "3":
                    print("\n========== UBAH PRODUK ==========")

                    tampilkan_produk()

                    if jumlah_produk() > 0:
                        nomor = input_angka(
                            "\nNomor produk yang ingin diubah: ", 1
                        )

                        if nomor is not None:

                            if nomor not in produk_kosmetik:
                                print("\nNomor produk tidak ditemukan!")

                            else:
                                print("\nMasukkan data produk baru")

                                nama = input("Nama produk: ").strip()
                                merek = input("Merek produk: ").strip()
                                kategori = input("Kategori: ").strip()

                                if nama == "" or merek == "" or kategori == "":
                                    print("\nData produk tidak boleh kosong!")

                                elif produk_sudah_ada(nama, merek, nomor):
                                    print("\nProduk dengan nama dan merek tersebut sudah terdaftar!")

                                else:
                                    harga = input_angka("Harga: ", 1)

                                    if harga is not None:
                                        stok = input_angka("Jumlah stok: ", 0)

                                        if stok is not None:
                                            produk_kosmetik[nomor] = {
                                                "nama": nama,
                                                "merek": merek,
                                                "kategori": kategori,
                                                "harga": harga,
                                                "stok": stok
                                            }

                                            print("\nProduk berhasil diubah!")


                # DELETE
                elif menu == "4":
                    print("\n========== HAPUS PRODUK ==========")

                    tampilkan_produk()

                    if jumlah_produk() > 0:
                        nomor = input_angka(
                            "\nNomor produk yang ingin dihapus: ", 1
                        )

                        if nomor is not None:

                            if nomor not in produk_kosmetik:
                                print("\nNomor produk tidak ditemukan!")

                            else:
                                print("\nNama produk:", produk_kosmetik[nomor]["nama"])
                                print("Merek      :", produk_kosmetik[nomor]["merek"])

                                konfirmasi = input(
                                    "Yakin ingin menghapus? (ya/tidak): "
                                ).strip().lower()

                                if konfirmasi == "ya":
                                    del produk_kosmetik[nomor]
                                    print("\nProduk berhasil dihapus!")

                                else:
                                    print("\nPenghapusan dibatalkan.")


                # SEARCH
                elif menu == "5":
                    print("\n========== CARI PRODUK ==========")

                    kata_kunci = input("Nama produk: ").strip()

                    if kata_kunci == "":
                        print("\nNama produk tidak boleh kosong!")

                    else:
                        hasil = cari_produk(kata_kunci)
                        tampilkan_hasil(hasil)


                # LOGOUT ADMIN
                elif menu == "6":
                    print("\nLogout berhasil!")
                    input("\nTekan Enter untuk kembali...")
                    break

                else:
                    print("\nPilihan tidak tersedia!")


            # ==============================
            # MENU PENGGUNA BIASA
            # ==============================

            else:

                # READ
                if menu == "1":
                    tampilkan_produk()


                # SEARCH
                elif menu == "2":
                    print("\n========== CARI PRODUK ==========")

                    kata_kunci = input("Nama produk: ").strip()

                    if kata_kunci == "":
                        print("\nNama produk tidak boleh kosong!")

                    else:
                        hasil = cari_produk(kata_kunci)
                        tampilkan_hasil(hasil)


                # LOGOUT USER
                elif menu == "3":
                    print("\nLogout berhasil!")
                    input("\nTekan Enter untuk kembali...")
                    break

                else:
                    print("\nPilihan tidak tersedia!")

            input("\nTekan Enter untuk kembali ke menu...")


    # REGISTER

    elif pilihan == "2":
        print("\n========== REGISTER ==========")

        username_baru = input("Masukkan username: ").strip().lower()
        password_baru = input("Masukkan password: ").strip()

        if username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong!")

        elif username_baru in akun:
            print("\nUsername sudah digunakan!")

        else:
            akun[username_baru] = {
                "password": password_baru,
                "role": "user"
            }

            print("\nRegister berhasil!")
            print("Silakan login menggunakan akun baru.")

        input("\nTekan Enter untuk kembali ke menu utama...")

    # KELUAR PROGRAM

    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program!")
        break

    else:
        print("\nPilihan tidak tersedia!")
        input("\nTekan Enter untuk melanjutkan...")