num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed:", rev)
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)
n = int(input("Enter terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
num = int(input("Enter number: "))
even = odd = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10

print("Evena = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print("Largest:", a)
elif b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")
num = int(input("Enter number: "))
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

print("Sum:", sum)
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits:", count)
num = int(input("Enter number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
