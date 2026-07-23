#  Consecutive Pass Count Definition: A consecutive pass means students pass one after another 
# without any failure in between.Task: Read marks of N students and find the longest consecutive 
# sequence of students scoring 35 or more. Example Input: 8 40 55 20 36 70 90 15 45 
# Example Output: Longest Consecutive Passes = 3
n=int(input("Enter length: "))
high=0
count=0
while n>0:
    marks=int(input("Enter the marks: "))
    if marks>35:
        count+=1
        if count>high:
            high=count
    else:
        count=0
    n-=1
print(high)

# Largest Prime Entered Definition: A prime number has exactly two positive divisors. Task: Read N numbers 
# and print the largest prime. Example Input: 6 12 17 21 29 18 7 Example Output: Largest Prime = 29
n=int(input("Enter length"))
high=0
while n>0:
    num=int(input("Enter the number"))
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        if num>high:
            high=num
    n-=1
print(high)

#  Sum of Even Digits Definition: Even digits are 0,2,4,6,8. 
# Task: Read a number and print the sum of even digits. Example Input: 4827316 Example Output: 20
n=int(input("Enter the number: "))
sum=0
while n>0:
    digit=n%10
    if digit%2==0:
        sum+=digit
    else:
        sum=sum
    n//=10
print(sum)

# Factory Quality Check Definition: Quality below 50 is defective. Task: Read N scores and print defective and
# good counts. Example Input: 6 45 6072 38 80 49 Example Output: Defective = 3 Good = 3
n=int(input("Enter length: "))
good=0
defective=0
while n>0:
    num=int(input("Enter the quality rate: "))
    if num>50:
        good+=1
    else:
        defective+=1
    n-=1
print(f"Good = {good}")
print(f"Defective = {defective}")

# Maximum Sales Increase Definition: Increase is today's sales minus yesterday's. Task: Find the maximum increase 
# between consecutive days. Example Input: 5 100 130 110 180 200 Example Output: Maximum Increase = 70
n=int(input("Enter length: "))
num1=int(input('Enter the number: '))
high=0
while n>1:
    num2=int(input("Enter the number: "))
    if num1<num2:
        diff=num2-num1 
    else:
        diff=num1-num2
    if diff>high:
        high=diff  
    num1=num2
    n-=1
print(high)
        
#  Number with Most Digits Definition: Digit count is the number of digits. 
# Task: Print the number with the most digits. Example Input: 5 23 9876 105 123456 89 Example Output: 123456
n=int(input("Enter length: "))
high=0
while n>0:
    num=int(input("Enter the number: "))
    temp=num
    count=0
    while num>0:
        count+=1
        num//=10
    if count>high:
        high=count
        number=temp
    n-=1
print(number)

#  Count Numbers Divisible by Both 4 and 6 Definition: Such numbers are divisible by 12. 
# Task: Count such numbers. Example Input: 6 12 24 18 36 40 48 Example Output: 4
n=int(input("Enter length: "))
count=0
while n>0:
    num=int(input("Enter the number: "))
    if num%4 ==0 and num%6==0:
        count+=1
    else:
        count=count
    n-=1
print(count)

# Longest Odd Streak Definition: An odd streak is consecutive odd numbers. Task: Find the longest odd streak.
# Example Input: 8 3 5 8 7 9 11 4 13 Example Output: 3
n=int(input("Enter length: "))
count=0
high=0
while n>0:
    num=int(input("Enter the number: "))
    if num%2!=0:
        count+=1
        if count>high:
            high=count
    else:
        count=0
    n-=1
print(high)

# Smallest Digit Sum Definition: Digit sum is the sum of a number's digits. Task: Print the number with the 
# smallest digit sum. Example Input: 4 123 81 44 70 Example Output: 70
n=int(input("Enter length: "))
low=100
sum=0
while n>0:
    num=int(input("Enter the number: "))
    temp=num
    while num>0:
        digit=num%10
        sum+=digit
        num//=10
    if sum<low:
        low=sum
        number=temp
    n-=1
print(number)
    

# Running Balance Definition: Running balance updates after each transaction. Task: Print 
# balance after each transaction and final balance. Example Input: 1000 4 500-200 300-100 
# Example Output: Balance=1500 Balance=1300 Balance=1600 Balance=1500 Final Balance=1500
curr_balance=int(input("Enter the balance: "))
temp=curr_balance
n=int(input("Enter transaction count: "))
sum=0

while n>0:
    trans=int(input("Enter the transaction: "))
    curr_balance=curr_balance+trans
    sum+=trans
    print(f"Balance = {curr_balance}")
    n-=1
print(f"Final Balance {curr_balance}")
