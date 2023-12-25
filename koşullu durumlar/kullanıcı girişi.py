print("*****************\nkullanıcı girişi\n*****************")
kullanıcı_adı = "simanur"
parola = "1234"
a = input("kullanıcı adı giriniz:")
b = input("parola giriniz:")
if(a == kullanıcı_adı and b == parola):
      print("giriş başarılı")
elif(a == kullanıcı_adı and b != parola):
      print("parola hatalı")
elif(a != kullanıcı_adı and b == parola ):
      print("kullanıcı adı hatalı")
else:
      print("giriş başarısız..")