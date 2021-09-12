x = int(input())
y = int(input())
# Start Code
if x ** 2 == y:
    print(x, "adalah akar positif dari", y)
else:
    print(x, "adalah bukan akar positif dari", y)

x = int(input())
# Code here
if x % 3 == 0:
    print("Fizz")
    if x % 5 == 0:
        print("Bazz")
elif x % 5 == 0:
    print("Bazz")
    
a = int(input())
# code in here
if a % 2 == 0:
    print(a, "adalah bilangan genap")
else:
    print(a, "bukan bilangan genap")
    
bil1 = float(input())
bil2 = float(input())
operator = input()
if operator == "+":
    print(bil1,operator,bil2,"=",bil1+bil2)
if operator == "-":
    print(bil1,operator,bil2,"=",bil1-bil2)
if operator == "*":
    print(bil1,operator,bil2,"=",bil1*bil2)
if operator == "/":
    print(bil1,operator,bil2,"=",bil1/bil2)

a, x, y = map(int, input().split())
if a % x == 0 and a % y != 0:
    print("Ya")
else:
    print("Tidak")

r = int(input())
#Code Here
phi = 3.14
if r % 7 != 0:
    print("Luas lingkaran berjari jari {} adalah {:.2f}".format(r,phi*(r*r)))
else:
    phi = 22/7
    print("Luas lingkaran berjari jari {} adalah {:.2f}".format(r,phi*(r*r)))
