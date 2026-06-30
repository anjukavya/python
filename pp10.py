# Program to calculate the sum of numbers from 1 to a positive integer
num = int(input("Enter a positive integer: "))
while num <= 0:
    print("Please enter a positive integer.")
    num = int(input("Enter a positive integer: "))
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("Sum =", sum)