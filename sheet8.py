#  Highest Profit Month Definition: Find the maximum value and its position while reading inputs. Task: A shop owner records the profit for N months. Print the highest profit and its month number.
#  Example Input: 5 12000 15000 9800 17500 16000 Example Output: Highest Profit = 17500 Month = 4
n=int(input("Enter length: "))
num=1
high=0
month=0
while num<=n:
    number=int(input("Enter a number: "))
    if number>high:
        high=number
        month=num
    num+=1
print(f"Highest Profit = {high}")
print(f"Month = {month}")

# 2. Perfect Square Counter Definition: A perfect square is the square of an integer. Task: Read N numbers 
# and count how many are perfect squares. Example Input: 5 16 20 25 18 49 Example Output: 3
n=int(input("Enter length"))
count=0
while n>0:
    num=int(input("Enter the number: "))
    for i in range(1,num+1):
        if i*i==num:
            count+=1
        else:
            count=count
    n-=1
print(count)

# Sum of Multiples of 7 Definition: Multiples of 7 are numbers divisible by 7. 
# Task: Read A and B. Sum all multiples of 7 between them. Example Input: 10 35 Example Output: 84
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
sum=0
while num1<=num2:
    if num1%7==0:
        sum+=num1
    num1+=1
print(sum)

# 4. Longest Positive Streak Definition: A streak is consecutive values satisfying a condition. 
# Task: Read N numbers and find the longest positive streak. Example Input: 8 5 7-2 4 9 1012-5 
# Example Output: 4
n=int(input("Enter the number: "))
count=0
high=0
while n>0:
    num=int(input("Enter the number: "))
    if num>0:
        count+=1
        if count>high:
            high=count
    else:
        count=0
    n-=1
print(high)

# Count Numbers with Exactly Three Divisors Definition: Some numbers have exactly three positive divisors. 
# Task: Read N numbers and count them. Example Input: 5 4 9 8 16 25 Example Output: 3
n=int(input("Enter length: "))
count=0
while n>0:
    num=int(input("Enter the number: "))
    start=1
    fact=0
    while start<=num:
        if num%start==0:
            fact+=1
        start+=1
    if fact==3:
        count+=1
    n-=1
print(count)

# 6. Largest Difference Definition: Difference is the gap between two values. Task: Find the largest 
# difference between consecutive inputs. Example Input: 5 10 25 18 40 32 Example Output: 22
n=int(input("Enter length: "))
num1=int(input("Enter the number: "))
high=0
while n>1:
    num2=int(input("Enter the number: "))
    diff=num1-num2
    if diff<0:
        diff=-diff
    else:
        diff=diff
    if diff>high:
        high=diff
    num1=num2
    n-=1
print(high)

# 7. Salary Bonus Definition: Employees below a threshold qualify. 
# Task: Count salaries below Rs.30000. Example Input: 5 25000 40000 18000 32000 29000 Example Output: 3
n=int(input("Enter length: "))
count=0
while n>0:
    num=int(input("Enter the number: "))
    if num<30000:
        count+=1
    n-=1
print(count)   

# 8. Largest Digit Sum Definition: Digit sum is the sum of all digits.Task: 
# Print the number having the largest digit sum. Example Input: 4 123 98 555 71 Example Output: 98
n=int(input("Enter length: "))
high=0
while n>0:
    num=int(input("Enter the number: "))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit
        temp//=10
    if sum>high:
        high=sum
        number=num
    n-=1
print(number)

# Average Until Zero Definition: Average equals total divided by count. 
# Task: Read numbers until 0 and print the average. Example Input: 8 12 20 0 Example Output: 13.33
sum=0
count=0
while True:
    num=int(input("Enter the number: "))
    if num>0:
        sum+=num
        count+=1
    else:
        break
print(f"Average: {sum/count:.2f}")

# 10. Count Numbers Greater Than Average Definition: Compare values with the calculated average. 
# Task: Read N numbers, compute average, then count numbers above it. Example Input: 5 10 20 30 40 50 
# Example Output: 2
n=int(input("Enter length: "))
list1=[]
sum=0
count=0
while n>0:
    num=int(input("Enter the number:"))
    sum+=num
    count+=1
    list1+=[num]
    n-=1
average=sum/count
final_count=0
for i in list1:
    if i>average:
        final_count+=1
print(final_count)