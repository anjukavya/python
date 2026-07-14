# Harshad Number Definition: A number that is divisible by the sum of its digits. 
# Example Calculation: Number = 18 Sum of digits = 1 + 8 = 9 Check divisibility: 18 ÷ 9 = 2 (remainder 0) 
# Therefore, 18 is a Harshad number. Task: Check whether a given number is Harshad. Example Input: 18 Example Output: 18 is a Harshad number
Number = 18
temp=Number
sum=0
while Number>0:
    digit=Number%10
    sum+=digit
    Number//=10
if temp%sum==0:
    print(f"{temp} is a Harshad Number")
else:
    print(f"{temp} is not a Harshad Number")

# Strong Number Definition: A number where the sum of factorials of its digits equals the original number. 
# Example Calculation: Number = 145 1! + 4! + 5! = 1 + 24 + 120 = 145 Therefore, 145 is a Strong number. 
# Task: Check whether a number is Strong. Example Input: 145 Example Output: 145 is a Strong number
Number = 145 
temp=Number
total=0
while Number>0:
    digit=Number%10
    prod=1
    num=digit
    while num>0:
        prod*=num
        num-=1
    total+=prod
    Number//=10
if total==temp:
    print(f"{temp} is a strong number")
else:
    print(f"{temp} is not a strong number")
    
# Neon Number Definition: A number where the sum of digits of its square equals the original number. 
# Example Calculation: Number = 9 Square = 9 × 9 = 81 Sum of digits = 8 + 1 = 9 Therefore, 9 is a Neon number. 
# Task: Check whether a number is Neon. Example Input: 9 Example Output: 9 is a Neon number
Number = 9
square=Number*2
sum=0
while square>0:
    digit=square%10
    sum+=digit
    square//=10
if Number==sum:
    print(f"{Number} is a Neon Number")
else:
    print(f"{Number} is not a Neon Number")

# Spy Number Definition: A number where the sum of digits equals the product of digits. 
# Example Calculation: Number = 1124 Sum = 1+1+2+4 = 8 Product = 1×1×2×4 = 8 Therefore, 1124 is a Spy number.
Number = 1124
temp=Number
sum=0
prod=1
while Number>0:
    digit=Number%10
    sum+=digit
    prod*=digit
    Number//=10
if sum==prod:
    print(f"{temp} is a Spy number")
else:
    print(f"{temp} is not a Spy number")

# Happy Number Definition: A number that reaches 1 after repeatedly replacing it with the sum of squares of its digits. 
# Example Calculation: 19 → 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1 Therefore, 19 is a Happy number. 
# Task: Check whether a number is Happy. Example Input: 19 Example Output: 19 is a Happy number
Number=19
temp=Number
seen=[]
while Number!=1 and Number not in seen:
    seen+=[Number]
    sum=0
    while Number>0:
        digit=Number%10
        sum+=digit**2
        Number//=10
    Number=sum   
if sum==1:
    print(f"{temp} is a Happy number")
else:
    print(f"{temp} is not a Happy number")

# Disarium Number Definition: A number where the sum of digits raised to their positions equals the original number. 
# Example Calculation: 135 = 1¹ + 3² + 5³ = 1 + 9 + 125 = 135 Therefore, 135 is a Disarium number. 
# Task: Check whether a number is Disarium. Example Input: 135 Example Output: 135 is a Disarium number
Number=135
temp=Number
num=Number
count=0
while Number>0:
    digit=Number%10
    count+=1
    Number//=10
n=0
sum=0
while temp>0:
    d=temp%10
    count-=n
    n+=1
    sq=d ** count
    temp//=10
    sum+=sq
if sum==num:
    print(f"{num} is a Disarium number")
else:
    print(f"{num} is not a Disarium number")

# Duck Number Definition: A number containing zero digits but not starting with zero. 
# Example Calculation: 1023 contains 0 after the first digit. Therefore, 1023 is a Duck number. 
# Task: Check whether a number is Duck. Example Input: 1023 Example Output: 1023 is a Duck number


# Abundant Number Definition: A number where the sum of proper divisors is greater than the number. 
# Example Calculation: 12 → Proper divisors: 1,2,3,4,6 Sum = 1+2+3+4+6 = 16 16 > 12, so 12 is Abundant. 
# Task: Check whether a number is Abundant. Example Input: 12Example Output: 12 is an Abundant number
Number=12
num=1
sum=0
while num<=Number:
    if Number%num==0:
        sum+=num
    num+=1
if sum>Number:
    print(f"{Number} is a Abundant number")
else:
    print(f"{Number} is not a Abundant number")

# Perfect Number Definition: A number where the sum of proper divisors equals the number. 
# Example Calculation: 6 → Proper divisors: 1,2,3 Sum = 1+2+3 = 6 Therefore, 6 is Perfect. 
# Task: Check whether a number is Perfect. Example Input: 6 Example Output: 6 is a Perfect number
Number=6
num=1
sum=0
while num<Number:
    if Number%num==0:
        sum+=num
    num+=1
if sum==Number:
    print(f"{Number} is a perfect number")
else:
    print(f"{Number} is not a perfect number")


# Automorphic Number Definition: A number whose square ends with the same digits as the original number. 
# Example Calculation: 25² = 625 Last two digits of 625 = 25 Therefore, 25 is Automorphic. 
# Task: Check whether a number is Automorphic. Example Input: 25 Example Output: 25 is an Automorphic number
Number=25
sq=Number**2 
temp=Number
count=0  
while temp>0:     
    count+=1     
    temp//=10  
remainder=sq%(10**(count))    
if Number==remainder:     
    print(f"{Number} is a Automorphic Number") 
else:     
    print(f"{Number} is not a Automorphic Number") 


