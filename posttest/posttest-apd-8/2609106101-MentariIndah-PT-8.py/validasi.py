
# ==========================================
# VALIDASI DAN ERROR HANDLING
# ==========================================

from data import produk_kosmetik


# ERROR HANDLING INPUT ANGKA
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
