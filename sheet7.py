#  Count Passing Students Task: Read marks of N students.
# Count how many scored 35 or more. Example Input: 5 45 20 67 35 18 Example Output: 3
n=int(input("Enter the number: "))
count=0
while n>0:
    marks=int(input("enter the marks: "))
    if marks>=35:
        count+=1
    n-=1
print(count)

#  Shop Profit Days Task: Read profit for N days. 
# Count days with profit greater than Rs.1000. Example Input: 5 800 1200 1500 950 2000 Example Output: 3
n=int(input("Enter the number: "))
count=0
while n>0:
    profit=int(input("enter the profit: "))
    if profit>1000:
        count+=1
    n-=1
print(count)

# Largest Multiple of 5 Task: Read N numbers.
# Print the largest divisible by 5, else 'No Multiple of 5'. Example Input: 5 12 25 18 40 7 Example Output: 40
n=int(input("Enter the number: "))
high=0
count=0
while n>0:
    num=int(input("enter the number: "))
    if num%5==0:
        count+=1
        if num>high:
            high=num
    n-=1
if count>=1:
    print(high)
else:
    print("No multiple of 5")

# Average of Even Numbers Task: Read N numbers. Print average of even numbers, 
# else 'No Even Numbers'. Example Input: 5 2 5 8 7 10 Example Output: Average = 6.67
n=int(input("Enter the numbers: "))
count=0
sum=0
while n>0:
    num=int(input("Enter the number: "))
    if num%2==0:
        count+=1
        sum+=num
    n-=1
print(f"Average = {sum/count:.2f}")

#  Student Improvement Task: Read marks in N tests. 
# Count how many times marks increased. Example Input: 5 50 55 52 60 70 Example Output: 3
n=int(input("enter the length: "))
num1=int(input("Enter the number: "))
count=0
while n>1:
    num2=int(input("Enter the number: "))
    if num2>num1:
        count+=1
        num1=num2
    n-=1
print(count)

# Divisors Count Task: Read a number and count its divisors. Example Input: 12 Example Output: 6
n=int(input("Enter the number: "))
num=1
count=0
while num<=n:
    if n%num==0:
        count+=1
    num+=1
print(count)

# Smallest Odd Number Task: Read N numbers. 
# Print smallest odd number or 'No Odd Number'. Example Input: 5 8 13 6 5 10 Example Output: 5
n=int(input("Enter the length: "))
low=int(input("Enter lowest number: "))
count=0
while n>0:
    num=int(input("Enter the number: "))
    if num%2!=0:
        count+=1
        if num<low:
            low=num
    n-=1
if count>=1:
    print(low)
else:
    print("No odd number")

# Count Numbers Ending with 7 Task: Read N numbers. 
# Count numbers ending with digit 7. Example Input: 5 27 15 97 120 47 Example Output: 3
n=int(input("Enter the number: "))
count=0
while n>0:
    num=int(input("Enter the number: "))
    if num>0:
        digit=num%10
        if digit==7:
            count+=1
        num//=10
    n-=1
print(count)

# Multiplication Table Task: Read a number and 
# print table from 1 to 15. Example Input: 7Example Output: 7 x 1 = 7 ... 7 x 15 = 105
n=int(input("Enter the number: "))
num=1
while num<=15:
    print(f"{n} X {num} = {n*num}")
    num+=1

# Sum Until Negative Number Task: Read numbers until a negative number is entered.
# Print sum of positive numbers. Example Input: 5 10 8 2-1 Example Output: 25
sum=0
while True:
    num=int(input("Enter a number"))
    if num>0:
        sum+=num
    else:
        break
print(sum)

