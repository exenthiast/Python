print("|=================================|")
print("|  Program Mencari Tahun Kabisat  |")
print("|=================================|")

def cek_tahun_kabisat(tahun):
    if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
        return True
    else:
        return False
    
tahun_awal = int(input("Masukkan Tahun Awal: "))
tahun_akhir = int(input("Masukkan Tahun Akhir: "))

print()
print("Hasil:")
for tahun in range(tahun_awal, tahun_akhir + 1):
    if cek_tahun_kabisat(tahun):
        print(tahun, "ini tahun kabisat")
    else:
        print(tahun, "ini bukan tahun kabisat")
        