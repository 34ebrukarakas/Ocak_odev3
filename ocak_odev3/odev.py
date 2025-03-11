# for döngüsü
n = int(input("Bir sayı giriniz:"))

toplam = 0
for i in range(1, n+1):
    toplam += i
print("For döngüsü ile toplam:",toplam)    

#while döngüsü
n = int(input("Bir sayı giriniz:"))

toplam_while, i = 0, 1
while i <= n:
    toplam_while += i
    i += 1
print("while döngüsü ile toplam:",toplam_while)    

