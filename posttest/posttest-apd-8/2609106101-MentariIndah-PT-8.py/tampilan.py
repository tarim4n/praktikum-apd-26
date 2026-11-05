
# ==========================================
# TAMPILAN PROGRAM
# ==========================================

from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)


# PROSEDUR 1 - TAMPILKAN PRODUK
def tampilkan_produk(produk_kosmetik):

    print(Fore.CYAN + "\n========== DAFTAR PRODUK ==========")

    if len(produk_kosmetik) == 0:

        print(Fore.YELLOW + "Belum ada produk.")

    else:

        tabel = PrettyTable()

        tabel.field_names = [
            "ID",
            "Nama Produk",
            "Merek",
            "Kategori",
            "Harga",
            "Stok"
        ]

        for nomor, produk in produk_kosmetik.items():

            tabel.add_row([
                nomor,
                produk["nama"],
                produk["merek"],
                produk["kategori"],
                "Rp " + format(produk["harga"], ",").replace(",", "."),
                produk["stok"]
            ])

        tabel.align["Nama Produk"] = "l"
        tabel.align["Merek"] = "l"
        tabel.align["Kategori"] = "l"

        print(Fore.GREEN + str(tabel))

    print(Fore.CYAN + "\nJumlah jenis produk:", len(produk_kosmetik))

    total_stok = 0

    for produk in produk_kosmetik.values():
        total_stok += produk["stok"]

    print("Total stok seluruh produk:", total_stok)


# PROSEDUR 2 - TAMPILKAN MENU
def tampilkan_menu(role):

    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + "      MANAJEMEN PRODUK KOSMETIK")
    print(Fore.CYAN + "=" * 40)

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

    print(Fore.CYAN + "=" * 40)


# PROSEDUR HASIL PENCARIAN
def tampilkan_hasil(hasil):

    print(Fore.CYAN + "\n========== HASIL PENCARIAN ==========")

    if len(hasil) == 0:

        print(Fore.RED + "Produk tidak ditemukan!")

    else:

        tabel = PrettyTable()

        tabel.field_names = [
            "ID",
            "Nama Produk",
            "Merek",
            "Kategori",
            "Harga",
            "Stok"
        ]

        for nomor, produk in hasil.items():

            tabel.add_row([
                nomor,
                produk["nama"],
                produk["merek"],
                produk["kategori"],
                "Rp " + format(produk["harga"], ",").replace(",", "."),
                produk["stok"]
            ])

        print(Fore.GREEN + str(tabel))
