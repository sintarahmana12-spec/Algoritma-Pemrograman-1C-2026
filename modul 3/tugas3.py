jumlah = 10

total_nilai = 0
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

nilai_tertinggi = -1
nilai_terrendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, jumlah + 1):
    print("mahasiswa ke-",i)

    nama = input("nama mahasiswa:")
    tugas = float(input("nilai tugas:"))
    uts = float(input("nilai uts:"))
    uas = float(input("nilai uas:"))

    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("nama:", nama)
    print("nilai tugas:", tugas)
    print("nilai uts:", uts)
    print("nilai uas:", uas)
    print("nilai akhir", round(akhir,2))
    print("kategori:", kategori)

    total_nilai += akhir

    if akhir > nilai_tertinggi:
        nilai_tertinggi = akhir
        nama_tertinggi

    if akhir < nilai_terrendah:
        nilai_terrendah = akhir
        nama_terendah = nama

print("HASIL")
print("jumlah mahasiswa kategori A:", jumlah_A)
print("jumlah mahasiswa kategori B:", jumlah_B)
print("jumlah mahasiswa kategori C:", jumlah_C)
print("jumlah mahasiswa kategori D:", jumlah_D)
print("jumlah mahasiswa kategori E:", jumlah_E)

print("nilai tertinggi:", nilai_tertinggi, "-", nama_tertinggi)
print("nilai terendah:", nilai_terrendah, "-", nama_terendah )