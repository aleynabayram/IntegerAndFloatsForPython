######## INTEGER AND FLOAT ########

from re import A


sayi1 = 5 
sayi2 = 3.8 # floattır ancak tam sayı ya da ondalıklı olduğunu belirtmemize gerek yok

print(type(sayi2)) # değişkenin tipini yazdırır örneğin <class 'float'> şeklinde

sayi = 5 ** 100 #integer ve float tipinin herhangi bir sınırı yoktur
print(sayi) # 5^100 sayısının değerini yazdırır

print(3 + 4) # toplama işlemi = 7
print(3 - 4) # çıkarma işlemi = -1
print(3 * 4) # çarpma işlemi = 12
print(16 / 5) # bölme işlemi = 3.2
print(16 // 5) # bölme işleminin sadece tam kısmını yazdırır = 3
print(3 ** 4) # kuvvet alır = 81
print(abs(-2)) # mutlak değer alır = 2

sonuç = 22 / 7
print(round(sonuç)) # içerisinde bulunan sayıyı yuvarlar
print(round(sonuç,3)) # virgülden sonra üç basamak olacak şekilde yuvarlar

sayi3 = 10
sayi4 = 6
print(3 == 3) # eşitlik doğruysa true yanlışsa false döner
print(sayi3 != sayi4) # eğer eşit değillerse true döner
print( sayi3 <= sayi4) # küçük eşit değilse false küçük eşitse true olarak döner

a = 1
b = a # bu satırdan sonra a sayısında olacak değişiklikler b sayısının değerini etkilemez
a = 5
print(b) # bu durumda b sayısı 1 olarak yazılır 

sayi5 ="100"
sayi6 = 100
print(type(sayi5)) # <class 'str'> olarak çıktı görünür yani tipi stringtir
print(type(sayi6)) # <class 'int'> olarak çıktı görünür yani tipi integerdır
print( sayi5 == sayi6) #false olarak görünür çünkü sayi5 herhangi bir büyüklük ifade etmeyen metindir ancak sayi6 sayısal olarak 100 ü ifade eder

sayi7 = int(sayi5) #sayı5 stringini integer değere dönüştürerek sayi7 değişkenine atadık
print(sayi6 == sayi7) # True olarak döner çünkü sayi5 i üst satırda sayı7 değişkenine integre olarak atadık

sayi8 = "100asd"
# sayi9 = int(sayi8) kodu hata verecektir çünkü içerisinde integera dönüştürülemeyecek bir ifade barındırmaktadır

sayi10 = int(3.5) # ondalıklı sayılarda integer fonksiyonu bir yuvarlama yapmaz tam kısmını alır
print(sayi10) # çıktısını 3 şeklinde görürüz

sayı11 = 123
sayı12 = str(sayı11) # herhangi bir int değeri str değere dönüştürebiliriz
print(type(sayı12)) # <class 'str'> olarak görünür çünkü üst satırda değeri str formatına dönüştürdük

i = 1
i += 2 # i sayısına 2 ekle ve i ye eşitle 
i *= 5 # i sayısını 5 ile çarp ve i ye eşitle 
print(i) # bu durumda 15 çıktısını görürüz 

