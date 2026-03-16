num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
num = int(input("Enter a number: "))
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
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits:", sum)
num = int(input("Enter a number: "))
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num = num // 10

print("Largest digit:", largest)
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
num = int(input("Enter a number: "))
even = 0
odd = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print("Even digits:", even)
print("Odd digits:", odd)
num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not Armstrong")
for i in range(1, 6):
    print("*" * i)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i) 