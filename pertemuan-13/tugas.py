siswa_nama = list()
siswa_nilai = list()

while True:
    jumlah_siswa = len(siswa_nama)
    print('\n')
    print("========================================")
    print("         PROGRAM KELOLA NILAI           ")
    print("========================================")
    print("(1) tampilkan seluruh data siswa.")
    print("(2) tambahkan data siswa.")
    print("(3) hapus data siswa.")
    print("(4) rubah data siswa.")
    print("(5) cari data siswa.")
    print("(0) keluar program.\n")

    menu = input("masukan nomer menu pilihan : ")

    if menu == "1":
        print('\n')
        print("========================================")
        print("        Menampilkan Data Siswa          ")
        print("========================================")

        if jumlah_siswa > 0:
            for i in range(jumlah_siswa):
                print("Nama  :", siswa_nama[i])
                print("Nilai :", siswa_nilai[i], '\n')
            
            print("----------------------------------------")
            print("Nilai Tertinggi :", max(siswa_nilai))
            print("Nilai Terendah  :", min(siswa_nilai))
            print("Nilai Rata-rata :", sum(siswa_nilai) / len(siswa_nilai))
            print("----------------------------------------\n")
        else:
            print("data siswa masih kosong, silahkan tambahkan dulu\n")

        print("(1) kembali ke menu.")
        print("(0) keluar program.\n")

        while True:
            pilihan = input("masukan pilihan : ")
            if pilihan == "1":
                break
            elif pilihan == "0":
                menu = "0"
                break
    elif menu == "2":
        print('\n')
        print("========================================")
        print("        Menambahkan Data Siswa          ")
        print("========================================")
        nama  = input("masukan nama siswa  : ")
        nilai = input("masukan nilai siswa : ")

        siswa_nama.append(nama)
        siswa_nilai.append(int(nilai))

        print("\nData siswa berhasil ditambahkan")
    elif menu == "3":
        print('\n')
        print("========================================")
        print("          Menghapus Data Siswa          ")
        print("========================================")
        while True:
            nama = input("\nmasukan nama siswa yang ingin dihapus : ")
            jumlah_siswa = len(siswa_nama)
            index = list()

            if siswa_nama.count(nama) > 0:
                for i in range(jumlah_siswa):
                    if siswa_nama[i] == nama:
                        index.append(i)
                        print("----------------------------------------")
                        print("No    :", i)
                        print("Nama  :", siswa_nama[i])
                        print("Nilai :", siswa_nilai[i])
                        print("----------------------------------------\n")

                while True:
                    no = int(input("masukan No yang sesuai untuk dihapus : "))

                    if no in index:
                        del siswa_nama[no]
                        del siswa_nilai[no]
                        print("\nData berhasil dihapus.\n")
                        break
                    else:
                        print("\nNomer yang anda masukan tidak ada di daftar.\n")
            else:
                print("\nTidak ada data dengan nama " + nama + " yang ditemukan.\n")


            print("(1) hapus data lagi.")
            print("(2) kembali ke menu.")
            print("(0) keluar program.\n")

            while True:
                pilihan = input("masukan pilihan : ")
                if pilihan == "1":
                    break
                elif pilihan == "2":
                    pilihan = "menu"
                    break
                elif pilihan == "0":
                    pilihan = "menu"
                    menu = "0"
                    break
                else:
                    print("masukan pilihan yang ada.\n")
            
            if pilihan == "menu":
                break
    elif menu == "4":
        print('\n')
        print("========================================")
        print("          Mengubah Data Siswa           ")
        print("========================================")
        while True:
            nama = input("\nmasukan nama siswa yang ingin di edit : ")
            index = list()

            if siswa_nama.count(nama) > 0:
                for i in range(jumlah_siswa):
                    if siswa_nama[i] == nama:
                        index.append(i)
                        print("----------------------------------------")
                        print("No    :", i)
                        print("Nama  :", siswa_nama[i])
                        print("Nilai :", siswa_nilai[i])
                        print("----------------------------------------\n")

                while True:
                    no = int(input("masukan No yang sesuai untuk diedit : "))

                    if no in index:
                        nama  = input("(new) Nama  : ")
                        nilai = int(input("(new) Nilai : "))

                        siswa_nama[no] = nama
                        siswa_nilai[no] = nilai

                        print("\nData berhasil diedit.\n")
                        break
                    else:
                        print("\nNomer yang anda masukan tidak ada di daftar.\n")
            else:
                print("\nTidak ada data dengan nama", nama, "yang ditemukan.\n")


            print("(1) edit data lagi.")
            print("(2) kembali ke menu.")
            print("(0) keluar program.\n")

            while True:
                pilihan = input("masukan pilihan : ")
                if pilihan == "1":
                    break
                elif pilihan == "2":
                    pilihan = "menu"
                    break
                elif pilihan == "0":
                    pilihan = "menu"
                    menu = "0"
                    break
                else:
                    print("masukan pilihan yang ada.\n")
            
            if pilihan == "menu":
                break
    elif menu == "5":
        print('\n')
        print("========================================")
        print("          Mencari Data Siswa            ")
        print("========================================")
        while True:
            print("\n(1) cari data siswa berdasarkan nama")
            print("(2) cari data siswa berdasarkan nilai\n")

            pilihan = input("masukan pilihan : ")
            
            if pilihan == "1":
                nama = input("\nmasukan nama untuk dicari : ")
                print("----------------------------------------")
                for i in range(jumlah_siswa):
                    if siswa_nama[i] == nama:
                        print("Nama  :", siswa_nama[i])
                        print("Nilai :", siswa_nilai[i], '\n')
                print(siswa_nama.count(nama), "Data berhasil ditemukan.")
                print("----------------------------------------\n")
            
            elif pilihan == "2":
                nilai = int(input("\nmasukan nilai untuk dicari : "))
                print("----------------------------------------")
                for i in range(jumlah_siswa):
                    if siswa_nilai[i] == nilai:
                        print("Nama  :", siswa_nama[i])
                        print("Nilai :", siswa_nilai[i], '\n')
                print(siswa_nilai.count(nilai), "Data ditemukan.")
                print("----------------------------------------\n")
            else:
                continue

            while True:
                print("(1) cari lagi.")
                print("(2) kembali ke menu.")
                print("(0) keluar program.")

                pilihan = input("\nmasukan pilihan : ")

                if pilihan == "1":
                    break
                elif pilihan == "2":
                    pilihan = "menu"
                    break
                elif pilihan == "0":
                    menu = "0"
                    pilihan = "menu"
                    break

            if pilihan == "menu":
                break

    if menu == "0":
        break