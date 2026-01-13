bus_perjalanan = {
    "R" : {
        "nama_bus" : "Rosalia",
        "SBY" : 300000,
        "MLG" : 400000
    },
    "S" : {
        "nama_bus" : "Sinar Jaya",
        "SLO" : 200000,
        "TGL" : 250000
    },
    "H" : {
        "nama_bus" : "Hiba Utama",
        "LMP" : 350000,
        "JGY" : 400000
    }
}


print("=============================================")
print("|           AGEN BUS PERJALANAN             |")
print("=============================================\n")

nama_penumpang = input("Masukan nama penumpang         : ")
kode_bus       = input("Masukan kode bus [ R / S / H ] : ").upper()
tujuan_bus     = input("Masukan tujuan bus             : ").upper()



bus = bus_perjalanan.get(kode_bus)

if bus == None:
    print("\n!!! BUS DENGAN KODE", kode_bus , "TIDAK TERSEDIA !!!\n")
    exit()


nama_bus = bus.get('nama_bus')
harga_tiket = bus.get(tujuan_bus)

if harga_tiket == None:
    print("\n!!! TUJUAN KE", tujuan_bus, "TIDAK ADA !!!\n")
    exit()



print("\n=============================================\n")

print("Nama Bus    :", nama_bus)
print("Tujuan      :", tujuan_bus)
print("Harga Tiket : Rp.", harga_tiket)

jumlah_beli = int(input("\nMasukan Jumlah Beli : "))

print("\n=============================================\n")

total_harga = harga_tiket * jumlah_beli

if jumlah_beli >= 3:
    hadiah = "jam tangan"
else:
    hadiah = "ga dapet"

ppn = total_harga * 5/100

total_bayar = total_harga + ppn



print("Total Harga        : Rp.", total_harga)
print("Hadiah             :", hadiah)
print("PPN (5%)           : Rp.", int(ppn))
print("Total Bayar        : Rp.", int(total_bayar))


while True:
    duit_pembeli = int(input("\nMasukan Pembayaran : Rp. "))
    if duit_pembeli < total_bayar:
        print("\n!!! DUIT ANDA KURANG !!!\n")
    else:
        break

print("Uang Kembaliannya  : Rp.", int(duit_pembeli - total_bayar))