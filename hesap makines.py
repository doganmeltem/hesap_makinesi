# hesap makinesi programi
print("****** hesap makinesi programi******")
"""
1. toplama işlemi
2. çıkarma işlemi
3. çarpma işlemi
4. bölme işlemi

"""

a=int(input("birinci sayiyi girin: "))
b=int(input("ikinci sayiyi girin: "))
islem=input("islemi seciniz: ")
if(islem=="1"):
    print("{} ile {}'in toplami {}'dir".format(a,b,a+b))
elif(islem=="2"):
    print("{} ile {}'in farki {}'dir".format(a,b,a-b))
elif(islem=="3"):
    print("{} ile {}'in carpimi {}'dir".format(a,b,a*b))
elif(islem==4):
    print("{} ile {}'in bolumu {}'dir".format(a,b,a/b))
else:
    print("gecersiz islem")