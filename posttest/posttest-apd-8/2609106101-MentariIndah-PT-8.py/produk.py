
# ==========================================
# MANAJEMEN PRODUK KOSMETIK
# ==========================================

import data

from validasi import input_angka, produk_sudah_ada
from tampilan import tampilkan_produk, tampilkan_hasil


# FUNGSI TANPA PARAMETER 1
def jumlah_produk():

    return len(data.produk_kosmetik)


# FUNGSI REKURSIF
def jumlahkan_stok(daftar_stok, posisi):

    if posisi == len(daftar_stok):
        return 0

    return daftar_stok[posisi] + jumlahkan_stok(
        daftar_stok, posisi + 1
    )


# FUNGSI TANPA PARAMETER 2
def hitung_total_stok():

    daftar_stok = []

    for produk in data.produk_kosmetik.values():
        daftar_stok.append(produk["stok"])

    return jumlahkan_stok(daftar_stok, 0)


# FUNGSI DENGAN PARAMETER 2
def cari_produk(kata_kunci):

    hasil = {}

    for nomor, produk in data.produk_kosmetik.items():

        if kata_kunci.lower() in produk["nama"].lower():
            hasil[nomor] = produk

    return hasil


# CREATE - TAMBAH PRODUK
def tambah_produk():

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

                data.produk_kosmetik[data.id_produk] = {
                    "nama": nama,
                    "merek": merek,
                    "kategori": kategori,
                    "harga": harga,
                    "stok": stok
                }

                data.id_produk += 1

                print("\nProduk berhasil ditambahkan!")


# READ - LIHAT PRODUK
def lihat_produk():

    tampilkan_produk(data.produk_kosmetik)

    print("Total stok berdasarkan rekursif:", hitung_total_stok())


# UPDATE - UBAH PRODUK
def ubah_produk():

    print("\n========== UBAH PRODUK ==========")

    tampilkan_produk(data.produk_kosmetik)

    if jumlah_produk() > 0:

        nomor = input_angka(
            "\nNomor produk yang ingin diubah: ", 1
        )

        if nomor is not None:

            if nomor not in data.produk_kosmetik:

                print("\nNomor produk tidak ditemukan!")

            else:

                print("\nMasukkan data produk baru")

                nama = input("Nama produk: ").strip()
                merek = input("Merek produk: ").strip()
                kategori = input("Kategori: ").strip()

                if nama == "" or merek == "" or kategori == "":

                    print("\nData produk tidak boleh kosong!")

                elif produk_sudah_ada(nama, merek, nomor):

                    print("\nProduk tersebut sudah terdaftar!")

                else:

                    harga = input_angka("Harga: ", 1)

                    if harga is not None:

                        stok = input_angka("Jumlah stok: ", 0)

                        if stok is not None:

                            data.produk_kosmetik[nomor] = {
                                "nama": nama,
                                "merek": merek,
                                "kategori": kategori,
                                "harga": harga,
                                "stok": stok
                            }

                            print("\nProduk berhasil diubah!")


# DELETE - HAPUS PRODUK
def hapus_produk():

    print("\n========== HAPUS PRODUK ==========")

    tampilkan_produk(data.produk_kosmetik)

    if jumlah_produk() > 0:

        nomor = input_angka(
            "\nNomor produk yang ingin dihapus: ", 1
        )

        if nomor is not None:

            if nomor not in data.produk_kosmetik:

                print("\nNomor produk tidak ditemukan!")

            else:

                print(
                    "\nNama produk:",
                    data.produk_kosmetik[nomor]["nama"]
                )

                print(
                    "Merek:",
                    data.produk_kosmetik[nomor]["merek"]
                )

                konfirmasi = input(
                    "Yakin ingin menghapus? (ya/tidak): "
                ).strip().lower()

                if konfirmasi == "ya":

                    del data.produk_kosmetik[nomor]

                    print("\nProduk berhasil dihapus!")

                else:

                    print("\nPenghapusan dibatalkan.")


# SEARCH - CARI PRODUK
def menu_cari_produk():

    print("\n========== CARI PRODUK ==========")

    kata_kunci = input("Nama produk: ").strip()

    if kata_kunci == "":

        print("\nNama produk tidak boleh kosong!")

    else:

        hasil = cari_produk(kata_kunci)

        tampilkan_hasil(hasil)
