print("1:toplama , 2:çıkarma , 3:çarpma , 4:bölme")
a = int(input("1. sayıyı giriniz:"))
b = int(input("2. sayıyı giriniz:"))
değer = input("hangi işlemi yapmak istiyorsunuz:")
if(değer == "1"):
    top = a + b
    print("sayıların toplamı:" , top)
elif(değer == "2"):
    if(a > b):
        fark1 = a - b
        print("sayıların farkı:" , fark1 )
    elif(b > a):
        fark2 = b - a
        print("sayıların farkı:" , fark2)
    else:
        print("sayıların farkı sıfır")
elif(değer == "3"):
    çarp = a * b
    print("sayıların çarpımı:" , çarp )
elif(değer == "4"):
    böl = a / b
    print("sayıların bölümü:" , böl)
else:
    print("geçersiz işlem")

