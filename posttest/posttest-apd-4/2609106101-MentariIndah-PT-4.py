print("========================================")
print("        REKAP PENGELUARAN BULANAN       ")
print("========================================")
username_benar = "mentari"
password_benar = "101"
percobaan = 0 
login_berhasil = False
while percobaan < 3:
    print()
    print("-------- LOGIN --------")

    username = input("Username : ") .strip().lower()
    password = input("Password : ") .strip()

    if username =="" or password == "":
        percobaan +=1
        print("Username dan password tidak boleh kosong!")
        print("Sisa percobaan:", 3 - percobaan)

    elif username != username_benar or password != password_benar:
        percobaan += 1
        print("Login Gagal. Sisa percobaan:", 3 - percobaan )

    else: 
        print("Login Berhasil!")
        login_berhasil = True
        break

if login_berhasil == False:
        print()
        print("===================================")
        print(  "Anda telah gagal login 3 kali.   ")
        print(  "Program berakhir.                ")
        print("===================================")
else:
    print()
    print("===================================")
    print("         DATA UANG SAKU            ")
    print("===================================")
    uang_bulanan = input("Masukkan uang saku awal: ") .strip()
    
    if uang_bulanan == "":
        print("Uang saku tidak boleh kosong.")
        print("Program berakhir.")

    elif not uang_bulanan.isdigit():
        print("Uang saku harus berupa angka.")
        print("Program berakhir.")
    else: 
        uang_bulanan =int(uang_bulanan)
        total_pengeluaran = 0
        if uang_bulanan <=0:
            print("Uang saku anda harus lebih dari 0.")
            print("Program berakhir.")
        else:
            while uang_bulanan > 0:
                print()
                print("==============================")
                print("     MENU UTAMA     ")
                print("==============================")
                print("[1] Catat Pengeluaran")
                print("[2] Cek Sisa Uang Saku")
                print("[3] Keluar")
                print("==============================")

                pilihan = input("Pilih menu (1-3): ").strip()

                if pilihan == "":
                    print("Menu tidak boleh kosong")
                elif pilihan == "1":
                    while True:
                        print()
                        print("------ CATAT PENGELUARAN ------")

                        pengeluaran = input("Masukkan nominal pengeluaran: ").strip()
                        if pengeluaran == "":
                            print("Nominal tidak boleh kosong.")

                        elif not pengeluaran.isdigit():
                            print("Nominal harus berupa angka.")
                        else: 
                            pengeluaran = int(pengeluaran)

                            if pengeluaran <= 0:
                                print("Nominal harus lebih dari 0.")

                            elif pengeluaran > uang_bulanan:
                                print("Saldo tidak mencukupi.")
                                print("Sisa uang saku: Rp", uang_bulanan)
                            else:
                                uang_bulanan -= pengeluaran
                                total_pengeluaran += pengeluaran
                                print()
                                print("Pengeluaran berhasil dicatat.")
                                print("Pengeluaran       : Rp", pengeluaran)
                                print("Sisa uang saku    : Rp", uang_bulanan)
                                print("Total pengeluaran  : Rp", total_pengeluaran)
                        if uang_bulanan == 0:
                            print("Saldo Anda telah habis.")
                            break
                        lagi = input ("Apakah Anda ingin mencatat  pengeluaran lagi? (Y/T): ").strip().upper()

                        if lagi == "Y":
                            continue
                        elif lagi == "T":
                            break
                        else:
                            print("Input harus Y atau T.")
                            break
                elif pilihan == "2":
                    print()
                    print("------ SISA UANG SAKU ------")
                    print("Sisa uang saku     :", uang_bulanan)
                    print("Total pengeluaran  :", total_pengeluaran)
                elif pilihan == "3":
                    print()
                    print("========================================")
                    print("     Terima kasih telah menggunakan      ")
                    print("   Program Rekap Pengeluaran Bulanan    ")
                    print("========================================")
                    break
                else:
                    print("Pilihan menu hanya 1, 2, atau 3.")

            if uang_bulanan == 0:
            
                print("=" * 40)
                print("      Saldo habis. Program selesai.        ")
                print("=" * 40)