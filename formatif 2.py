daftar_paket = {
    '1' : {
        'nama_paket' : 'Cerdas',
        'materi' : 'Android Programming',
        'harga' : 3000000
    },

    '2' : {
        'nama_paket' : 'Ceria',
        'materi' : 'Desain Grafis',
        'harga' : 2500000
    },

    '3' : {
        'nama_paket' : 'Smile',
        'materi' : 'Multimedia',
        'harga' : 2000000
    }
}

lm = 70

while True:
    daftar_kode_paket = []
    daftar_nama_siswa = []

    print("-" * 40)
    print('KURSUS ONLINE "GANEBO"'.center(40))
    print("-" * 40)

    jumlah_data  = int(input("Masukan Jumlah Data  : "))
    for i in range(jumlah_data):
        print("\nData ke", i+1)
        nama_siswa  = input("Masukan Nama Siswa   : ")
        kode_paket  = input("Masukan Paket Kursus [ 1 / 2 / 3 ] : ")
        daftar_nama_siswa.append(nama_siswa)
        daftar_kode_paket.append(kode_paket)

    total = []
    print("\n\n")
    print("-" * lm)
    print("REKAPITULASI PENDAFTARAN KURSUS ONLINE".center(lm))
    print("-" * lm)
    print(" No.   Nama Siswa    Nama Paket    Harga           Materi ")
    print("-" * lm)
    for index in range(len(daftar_nama_siswa)):
        kode = daftar_kode_paket[index]
        nama_siswa = daftar_nama_siswa[index]
        paket_pilihan = daftar_paket[kode]
        nama_paket = paket_pilihan['nama_paket']
        harga_paket = paket_pilihan['harga']
        materi_paket = paket_pilihan['materi']
        total.append(harga_paket)

        print("  " + str(index+1).ljust(5) + nama_siswa.ljust(14) + nama_paket.ljust(14) + ("Rp. " + str(harga_paket)).ljust(15) + materi_paket)
    print("-" * lm)
    print('\n')

    print("Total".ljust(14) + "Rp.", sum(total))
    uang_bayar = int(input("Uang Bayar".ljust(14) + "Rp. "))
    print("Kembalian".ljust(14) + "Rp.", uang_bayar - sum(total))

    akhiri = input("\nTransaksi Lagi [Y/T] ? ").lower()

    if akhiri == "t":
        break
    else:
        print("LANJUT\n\n\n\n\n")