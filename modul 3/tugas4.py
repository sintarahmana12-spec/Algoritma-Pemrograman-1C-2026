kuota_penuh = 0

for i in range(1,11):
    if kuota_penuh == 3:
        print("kuota beasiswa penuh sudah terpenuhi!")
        break

    print("mahasiswa ke - :", i)
    nama = input("masukkan nama:")
    ipk = float(input("masukkan ipk:"))
    penghasilan =int(input("masukkan penghasilan orang tua per bulan Rp:"))

    if ipk < 3.00:
        print(nama,"tidak memenuhi syarat beasiswa karena ipk kurang dari 3.00")
        continue

    if penghasilan <= 3000000:
        print(nama,"mendapatkan beasiswa penuh")
        kuota_penuh += 1
    elif penghasilan <= 5000000:
        print(nama,"mendapatkan beasiswa sebagian")
    else:
        print(nama,"tidak mendapatkan beasiswa")

    print("jumlah penerima beasiswa penuh:", kuota_penuh)