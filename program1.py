modal = 100000000
bulan = 8
a = 1
b = 0
c = 0

while a <= bulan :
    if a == 1 :
        b = modal *0/100
    if a == 2:
        b = modal * 0 / 100
    if a == 3:
        b = modal * 1 / 100
    if a == 4:
        b = modal * 1 / 100
    if a == 5:
        b = modal * 5 / 100
    if a == 6:
        b = modal * 5 / 100
    if a == 7:
        b = modal * 5 / 100
    if a == 8:
        b = modal * 2 / 100

    print("laba bulan ke-", a, "adalah : ", b)
    c = c + b
    a += 1

print ("total laba adalah :",c)





