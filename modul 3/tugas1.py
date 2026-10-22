penumpang = 0
total_peendapatan = 0
maksimal_jarak = 0
total_jarak = 0

while True:
    jarak = float(input("jarak(0 untuk berhenti):"))

    if jarak == 0:
        break

    if jarak < 0:
        continue

    penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if penumpang % 5 == 0:
        tarif = tarif * 0.5

    total_peendapatan += tarif
    total_jarak += jarak

    if jarak > maksimal_jarak:
       maksimal_jarak = jarak

print("jumlah penumpang:", penumpang)
print("total pendapatan : Rp", total_peendapatan)
print("jarak jauh:", maksimal_jarak, "km")
print("rata-rata jarak:", total_jarak / penumpang if penumpang > 0 else 0, "km3")