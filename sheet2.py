# Print Numbers from 1 to N Definition: Loops allow a program to repeat the same task multiple times. 
# Task: Read a number N and print all numbers from 1 to N using a loop. Example Input: N = 5 
# Example Output: 1 2 3 4 5
N = 5
num=1
while num<=N:
    print(num,end=" ")
    num+=1

# Print Numbers from N to 1 Definition: Reverse counting is useful in many programming problems. 
# Task: Read a number N and print numbers from N to 1 using a loop. Example Input: N = 5 Example Output: 5 4 3 2 1
N = 5
while N>0:
    print(N,end=" ")
    N-=1

# Sum of First N Natural Numbers Definition: Natural numbers start from 1. 
# Task: Find the sum of numbers from 1 to N using a loop. Example Input: N = 5 Example Output: 15
N = 5
sum=0
while N>0:
    sum+=N
    N-=1
print(sum)

#  Factorial of a Number Definition: The factorial of a number is the product of all positive integers from 1 to that number. 
# Task: Calculate the factorial using a loop. Example Input: N = 5 Example Output: 120
N = 5
num=1
fact=1
while num<=N:
    fact*=num
    num+=1
print(fact)

# Multiplication Table Definition: A multiplication table shows the multiples of a number. 
# Task: Print the multiplication table of a given number up to 10. Example Input: N = 3 
# Example Output: 3 x 1 = 3 ... 3 x 10 = 30
N=3
num=1
while num<=10:
    print(f"{N} X {num} = {N*num}")
    num+=1

# Count Digits Definition: Every number contains one or more digits. 
# Task: Count the total number of digits using a loop.Example Input: 45892 Example Output: 5
N=45892
count=0
while N>0:
    count+=1
    N//=10
print(count)

#  Reverse a Number Definition: Reversing digits is a common number problem. 
# Task: Reverse the given number using a loop. Example Input: 1234 Example Output: 4321
N=1234
rev=0
while N>0:
    digit=N%10
    rev=rev*10+digit
    N//=10
print(rev)

# Sum of Digits Definition: Add all digits present in the number. 
# Task: Calculate the sum of digits using a loop. Example Input: 572 Example Output: 14
N=572
sum=0
while N>0:
    digit=N%10
    sum+=digit
    N//=10
print(sum)

# Product of Digits Definition: Multiply all digits present in the number. 
# Task: Calculate the product of digits using a loop. Example Input: 572 Example Output: 70
N=572
prod=1
while N>0:
    digit=N%10
    prod*=digit
    N//=10
print(prod)

# Count Even and Odd Digits Definition: Separate digits based on whether they are even or odd. 
# Task: Count even digits and odd digits using a loop.
# Example Input: 583920 Example Output: Even Digits = 3 Odd Digits = 3
N=583920
even=0
odd=0
while N>0:
    digit=N%10
    if digit%2==0:
      even+=1
    else:
      odd+=1
    N//=10
print(f"Even Digits= {even}")
print(f"Odd Digits={odd}")
