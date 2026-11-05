
# ==========================================
# PROGRAM UTAMA POSTTEST 8
# SISTEM MANAJEMEN PRODUK KOSMETIK
# ==========================================

import os

from auth import cek_login, register
from tampilan import tampilkan_menu

from produk import (
    tambah_produk,
    lihat_produk,
    ubah_produk,
    hapus_produk,
    menu_cari_produk
)


# PROSEDUR MEMBERSIHKAN TERMINAL
def bersihkan_layar():

    os.system("cls" if os.name == "nt" else "clear")


# PROGRAM UTAMA
while True:

    bersihkan_layar()

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

            bersihkan_layar()

            tampilkan_menu(role)

            menu = input("Pilih menu: ")


            # MENU ADMIN
            if role == "admin":

                if menu == "1":

                    tambah_produk()

                elif menu == "2":

                    lihat_produk()

                elif menu == "3":

                    ubah_produk()

                elif menu == "4":

                    hapus_produk()

                elif menu == "5":

                    menu_cari_produk()

                elif menu == "6":

                    print("\nLogout berhasil!")

                    input("\nTekan Enter untuk kembali...")

                    break

                else:

                    print("\nPilihan tidak tersedia!")


            # MENU PENGGUNA BIASA
            else:

                if menu == "1":

                    lihat_produk()

                elif menu == "2":

                    menu_cari_produk()

                elif menu == "3":

                    print("\nLogout berhasil!")

                    input("\nTekan Enter untuk kembali...")

                    break

                else:

                    print("\nPilihan tidak tersedia!")


            input("\nTekan Enter untuk kembali ke menu...")


    # REGISTER
    elif pilihan == "2":

        register()

        input("\nTekan Enter untuk kembali ke menu utama...")


    # KELUAR PROGRAM
    elif pilihan == "3":

        print("\nTerima kasih telah menggunakan program!")

        break


    else:

        print("\nPilihan tidak tersedia!")

        input("\nTekan Enter untuk melanjutkan...")
