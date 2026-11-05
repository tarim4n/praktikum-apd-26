
# ==========================================
# FUNGSI LOGIN DAN REGISTER
# ==========================================

from data import akun


# FUNGSI DENGAN PARAMETER 1
def cek_login(username, password):

    if username in akun:
        if password == akun[username]["password"]:
            return akun[username]["role"]

    return None


# PROSEDUR REGISTER
def register():

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
