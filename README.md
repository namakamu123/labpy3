# labpy3
## latihan1.py : mencetak nilai secara acak yang lebih kecil dari 0.5
1. mengakses random "import random"
2. mendeklarasikan variable i = 1
3. menginputkan nilai ke variable n
4. membuat perulangan dengan menggunakan operator while dengan kondisi i <= n
    - membuat pemrosesan a = random.uniform (0.0,0.5) yaitu bilangan acak dari 0.0 sampai 0.5
    - mencetakan nilai random ke console
    - mengupdate nilai i " i += 1 ", supaya looping terbatasi
5. selesai.

berikut kode lengkapnya :
import random
i = 1
n = int (input ("masukan nilai N :"))

while i <= n :
    a = random.uniform(0.0,0.5)
    print ("data ke -",i, "adalah =>",a)
    i += 1
print("selesai")

berikut hasil screenshotnya :
![latihan1](https://user-images.githubusercontent.com/44119437/52901345-206a3e80-3235-11e9-8771-fb89fff6b67c.png)

## latihan2.py : menentukan bilangan terbesar dar sejumlah bilangan, menginputkan anggka nol untuk mengakhirinya
1. mendeklarasikan variable a = 1
2. mendeklarasikan variable max = 0
3. membuat perulangan dengan menggunakan operator while dengan kondisi a != 0
    - menginputkan nilai ke variable a
    - jika a lebih besar dar max maka max = a
    
4. menginputkan angkan nol untuk mengakhiri looping
5. mencetakan nilai terbesar ke console
6. selesai.

berikut kode lengkapnya :
a = 1
max = 0
while a != 0 :
	a = int (input ("masukan bilangan : "))
	if a > max :
		max = a
print ("bilangan terbesarnya adalah :",max)

berikut hasil screenshotnya :
![latihan2](https://user-images.githubusercontent.com/44119437/52901526-55779080-3237-11e9-9034-ebd1e4726e1c.png)

## program1.py : program sederhana dengan perulangan
1. mendeklarasikan variable modal = 100000000
2. mendeklarasikan variable bulan = 8
3. mendeklarasikan variable a = 1
4. mendeklarasikan variable b = 0
5. mendeklarasikan variable c = 0
6. membauat perulangan dengan menggunakan operator while dengan kondisi a <= bulan
7. untuk perulangan pertama dan kedua, membuat buat pemrosesan "bulan*0/100"
8. untuk perulangan ketiga dan keempat, membuat buat pemrosesan "bulan*1/100"
9. untuk perulangan kelima, keenam dan ketujuh, membuat buat pemrosesan "bulan*5/100"
10. untuk perulangan ke delapan, membuat buat pemrosesan "bulan*2/100"
11. mencetakan nilai perkalian dari masing - masing perulangan
12. menjumlahkan hasil dari semua perkalian perulangan di atas
13. mengupdate nilai i " i += 1 " agar looping terbatasi
14. mencetakan hasil hasil pemjumlahan dari semua perkalian perulangan di atas
15. selesai.

berikut kode lengkapnya :
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

berikut hasil screenshotnya :

![program1](https://user-images.githubusercontent.com/44119437/52901683-30841d00-3239-11e9-883e-74e5456e9584.png)


