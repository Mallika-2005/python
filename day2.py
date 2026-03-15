num=int(input("enter a number:"))
if num%2==0:
  print("it is even")
else:
     print("odd")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a>b:
    print("a is largest")
else:
    print("b is largest")
a=int(input("enter a number"))
if a<0:
    print("negative")
elif a>0:
     print("positive")
else:
    print("zero")
i=0
for i in range(1,10):
    print(i)
sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum =", sum)
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Digits:", count)
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse:", rev)
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)