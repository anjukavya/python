# Count Even and Odd Numbers from 1 to N Problem Definition: A program can classify numbers as even or odd.
# Task: Read N. Count even and odd numbers from 1 to N. Example Input: 10 Example Output: Even Numbers = 5 Odd Numbers = 5
n=int(input("Enter number: "))
num=1
even=0
odd=0
while num<=n:
    if num%2==0:
        even+=1
    else:
        odd+=1
    num+=1
print("Even", even)
print("odd" , odd)

#  Sum of Numbers Divisible by 3 Problem Definition: Process only numbers that satisfy a condition.
# Task: Read N. Find the sum of numbers divisible by 3. Example Input: 10 Example Output: 18
n=int(input("Enter number: "))
num=1
sum=0
while num<n:
    if num%3==0:
        sum+=num
    num+=1
print(sum)

#  Print Leap Years in a Range Problem Definition: Leap years follow specific rules. 
# Task: Read start year and end year. Print all leap years. Example Input: 2000 2020 Example Output: 2000 2004 2008 2012 2016 2020
n1=int(input("Enter Starting year: "))
n2=int(input("Enter Sending year: "))
while n1<=n2:
    print(n1)
    n1+=4

# Count Multiples of 5 and 7 Problem Definition: Numbers may satisfy multiple divisibility rules. 
# Task: Read N. Count multiples of 5, 7 and both. Example Input: 50 Example Output: 5=10 7=7 Both=1
n=int(input("Enter number: "))
num=1
five=0
seven=0
both=0
while num<=n:
    if num%5==0:
        five+=1
    if num%7==0:
        seven+=1
    if num%5==0 and num%7==0:
        both+=1
    num+=1
print("Both",both)
print("Five",five)
print("Seven",seven)

#  Print All Factors and Their Count Problem Definition: Factors divide a number exactly.
# Task: Print all factors and total count. Example Input: 12 Example Output: 1 2 3 4 6 12 Total Factors = 6
n=int(input("Enter number: "))
num=1
count=0
while num<=n:
    if 12%num==0:
       print(num,end=" ")
       count+=1
    num+=1
    print()
print("count",count)

# Largest Digit Problem Definition: Find the greatest digit. Task: Read a number and print the largest digit.
# Example Input: 583920 Example Output: Largest Digit = 9
n=int(input("Enter number: "))
high=0
while n>0:
    digit=n%10
    if digit>high:
        high=digit
    n//=10
print(high)

# Smallest Digit Problem Definition: Find the smallest digit. Task: Read a number and print the smallest digit. 
# Example Input: 583920 Example Output: Smallest Digit = 0
n=int(input("Enter number: "))
low=10
while n>0:
    digit=n%10
    if digit<low:
        low=digit
    n//=10
print(low)

# Count Digits Greater Than 5 Problem Definition: Count digits meeting a condition. 
# Task: Read a number and count digits > 5. Example Input: 589762 Example Output: 4
n=int(input("Enter number: "))
count=0
while n>0:
    digit=n%10
    if digit>5:
        count+=1
    n//=10
print(count)

#  Sum Only Even Digits Problem Definition: Add only even digits. 
# Task: Read a number and print the sum of even digits. Example Input: 58294 Example Output: 14
n=int(input("Enter number: "))
sum=0
while n>0:
    digit=n%10
    if digit%2==0:
        sum+=digit
    n//=10
print(sum)

# Divisible by 3 but Not 5 Problem Definition: Filter numbers using two conditions. Task: Read N and print numbers divisible by 3 but not 5.
# Example Input: 30 Example Output: 3 6 9 12 18 21 24 27
n=int(input("Enter number: "))
num=1
while num<=n:
    if num%3==0 and num%5!=0:
        print(num,end=" ")
    num+=1
