# Find the Largest of N Numbers Problem Definition: Find the greatest value from a sequence of numbers. 
# Task: Read N, then read N numbers one by one and print the largest. Example Input: N=5 12 45 8 90 34 
# Example Output: Largest = 90
n=int(input("Enter length: "))
high=0
while n>0:
    num=int(input("Enter Number: "))
    if high<num:
        high=num
    n-=1
print(f"Largest: {high}")

# Find the Smallest of N Numbers Problem Definition: Find the smallest value from a sequence of numbers. 
# Task: Read N numbers and print the smallest. Example Input: N=5 18 3 45 7 12 Example Output: Smallest = 3
n=int(input("Enter length: "))
low=100
while n>0:
    num=int(input("Enter Number: "))
    if low>num:
        low=num
    n-=1
print(f"Smallest: {low}")

# Find the Second Largest Number Problem Definition: Find the second highest value without sorting. 
# Task: Read N numbers and print the second largest. Example Input: N=5 25 60 15 80 50 Example Output: Second Largest = 60
n=int(input("Enter length: "))
high=0 
sec_lar=0                                           
while n>0:
    num=int(input("Enter Number: "))
    if high<num:
        sec_lar=high
        high=num
    n-=1
print(sec_lar)

#  Find the Second Smallest Number Problem Definition: Find the second lowest value without sorting.
# Task: Read N numbers and print the second smallest. Example Input: N=5 25 60 15 80 50 
# Example Output: Second Smallest = 25
n=int(input("Enter length: "))
n1=int(input("Enter Low number"))
low=n1 
sec_low=0                                         
while n>0:
    num=int(input("Enter Number: "))
    if low>num:
        sec_low=low
        low=num
    n-=1
print(sec_low)

# Count Positive, Negative and Zero Values Problem Definition: Classify numbers based on their sign. 
# Task: Read N numbers and count positives, negatives and zeros. Example Input: N=6 10-5 0 18-2 0 
# Example Output: Positive = 2 Negative = 2 Zero = 2
N=int(input("Enter length: "))
pos=0
neg=0
zero=0
while N>0:
    num=int(input("Enter Number: "))
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1
    N-=1
print(f"Positive : {pos}")
print(f"Negative : {neg}")
print(f"Zero : {zero}")

#  Find the Missing Number Problem Definition: One number from 1 to N is missing. Task: Read N and the remaining numbers, 
# then find the missing number. Example Input: N=6 1 2 3 5 6 Example Output: Missing Number = 4
N=int(input("Enter length: "))
num=1
pre_sum=0
while num<=N:
    pre_sum+=num
    num+=1
num2=1
last_sum=0
while num2<N:
    digit=int(input("Enter number"))
    last_sum+=digit
    num2+=1
diff=pre_sum-last_sum
print(diff)

#  Check Whether a Number is Perfect Problem Definition: A perfect number equals the sum of its proper factors. 
# Task: Determine whether the given number is perfect. Example Input: 28Example Output: Perfect Number
N=int(input("Enter number: "))
temp=N
sum=0
num=1
while num<N:
    if N%num==0:
        sum+=num
    num+=1
print(sum)
if temp==sum:
    print("Perfect Number")
else:
    print("Not a perfect Number")

#  Find the GCD of Two Numbers Problem Definition: The GCD is the greatest number that divides both numbers. 
# Task: Find the GCD using loops. Example Input: 24 36 Example Output: GCD = 12
n1=int(input("Enter Number1: "))
n2=int(input("Enter Number2: "))
num1=1
high=0
while num1<n1:
    if n1%num1==0 and n2%num1== 0:
        if high<num1:
            high=num1
    num1+=1
print(high)

#  Find the LCM of Two Numbers Problem Definition: The LCM is the smallest number divisible by both numbers. 
# Task: Find the LCM using loops. Example Input: 12 18 Example Output: LCM = 36
n1=int(input("Enter Number1: "))
n2 = int(input("Enter Number2: "))
count = 1
gcd = 1
while count <= n1 and count <= n2:
    if n1 % count == 0 and n2 % count == 0:
        gcd = count
    count += 1
print(gcd)


#  Power Without Using ** Problem Definition: Calculate a power using repeated multiplication. 
# Task: Read the base and exponent, then compute the result using a loop. Example Input: Base = 3 Exponent = 4 
# Example Output: 81
n1=int(input("Enter Number1: "))
n2 = int(input("Enter Number2: "))
prod=1
while n2>0:
    prod*=n1
    n2-=1
print(prod)


