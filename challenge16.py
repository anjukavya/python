# Sum of First and Last Digit Task: Given a number, find the sum of its first digit and last digit. 
# Example Input: Number = 58392 Example Output: First digit = 5, Last digit = 2, Sum = 7
Number = 58392
temp=Number
count=0
while temp>0:
    digit=temp%10
    temp//=10
    count+=1
print(count)
n=1
while Number>0:
    if n==1:
        digit=Number%10
        Last_num=digit
        Number//=10
    elif n==count:
        digit=Number%10
        First_num=digit
        Number//=10
    else:
        digit=Number%10
        Number//=10
    n+=1
print(f"First Number {First_num}")
print(f"Last Number {Last_num}")
print(f"Sum Of Numbers {First_num+Last_num}")

# Count Digits Greater Than 5 Task: Count digits in a number that are greater than 5. 
# Example Input: Number = 836921 Example Output: Digits greater than 5 = 4
n = int(input("Enter Number: ")) 
count = 0 
while n > 0: 
    digit = n % 10 
    if digit > 5:
        count = count + 1 
    n = n // 10 
print("Count =", count) 

# Product of Digits at Odd Positions Task: Find product of digits present at odd positions from right side. 
# Example Input: Number = 58294 Example Output: Product = 64
Number = 58294
count=1
prod=1
while Number>0:
    if count%2!=0:
        digit=Number%10
        Number//=10
        prod=prod*digit
        count+=1
    else:
        digit=Number%10
        Number//=10
        count+=1
print(prod)

# Largest Digit Difference Task: Find difference between largest and smallest digit. 
# Example Input: Number = 58392 Example Output: Largest = 9, Smallest = 2, Difference = 7
Number = 58392
high=0
low=10
while Number>0:
    digit=Number%10
    if high<digit:
        high=digit
    if low>digit:
        low=digit
    Number//=10
print(f"Largest: {high}")
print(f"Lowest: {low}")
print(f"Difference: {high-low}")

# Count Even and Odd Digits Task: Count even and odd digits in a number. 
# Example Input: Number = 58392 Example Output: Even digits = 2, Odd digits = 3
Number = 58392
even=0
odd=0
while Number>0:
    digit=Number%10
    if digit%2==0:
        even+=1
    else:
        odd+=1
    Number//=10
print(f"Even Digits {even}")
print(f"Odd Digits {odd}")

# Reverse Number Without Changing Middle Digit Task: 
# Reverse first and last digits while keeping middle digits unchanged. 
# Example Input: Number = 12345 Example Output: Result = 52341
Number = 12345
temp=Number
count=0
while temp>0:
    temp//=10
    count+=1
power=10 ** (count-1)
first=Number // power
last=Number % 10
mid=(Number % power)//10
result = last * power + mid * 10 + first
print("Result =", result)

# Digit Sum Until Single Digit Task: Add digits repeatedly until one digit remains. 
# Example Input: Number = 9876 Example Output: Final Result = 3
# Number = 9876

# 8. Second Largest Digit Task: Find the second largest digit in a number. 
# Example Input: Number = 58392 Example Output: Largest = 9, Second largest = 8
Number = 58392
temp=Number
high=0
second=0
while Number>0:
    digit=Number%10
    if high<digit:
        high=digit
    elif second<digit and digit!=high:
        second=digit
    Number//=10
print(f"Highest {high}")
print(f"Second Largest {second}")



# 9. Replace Zero Digits Task: Replace all zero digits with 9.Example Input: Number = 102030 
# Example Output: Result = 192939 
Number = 102030
ans=0 
c=1
while Number>0:
    digit=Number%10
    if digit==0:
        digit=9
    ans=digit*c+ans
    c=c*10
    Number//=10
print(ans)
    

# 10. Digit Position Finder Task: Find position of a digit in a number from right side. 
# Example Input: Number = 58392, Digit = 3 Example Output: Position = 3
Number = 58392
count=0
while Number>0:
    digit=Number%10
    count+=1
    Number//=10
    if digit==3:
        print(f"Position = {count}")
        break
