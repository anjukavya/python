#Task: An element is a leader if it is greater than every element to its right. 
len=int(input("Enter the list length: "))
list1=[]
for i in range(len):
    num=int(input("Enter a num: "))
    list1+=[num]
print(list1)
for i in range(len):
    for j in range(i+1,len):
        if list1[i]<list1[j]:
            break
    else:
        print(list1[i])
        break

#Rearrange the list so positive and negative numbers appear alternately.
#If one type runs out, append the remaining elements.
len=int(input("Enter the list length: "))
list1=[]
for i in range(len):
    num=int(input("Enter a num: "))
    list1+=[num]
print(list1)
neg_list=[]
pos_list=[]
neg_count=0
pos_count=0
for i in list1:
    if i<0:
        neg_list+=[i]
        neg_count+=1
    elif i>0:
        pos_list+=[i]
        pos_count+=1
    else:
        neg_list=neg_list
        pos_list=pos_list
print(f"Negative List: {neg_list}")
print(f"Positive List: {pos_list}")
new_list=[]
length=pos_count
if neg_count<length:
    length=neg_count
for i in range(length):
    new_list+=[pos_list[i]]
    new_list+=[neg_list[i]]
for i in pos_list:
    if i not in new_list:
        new_list+=[i]
for j in neg_list:
    if j not in new_list:
        new_list+=[j]
print(new_list)

# Find the Majority Element 
# Task: Return the element appearing more than n/2 times. 
# If none exists, return None. Example Input: 
# Input: [2, 2, 1, 2, 3, 2, 2] Example Output: Output: 2
len=int(input("Enter the list length: "))
list1=[]
for i in range(len):
    num=int(input("Enter a num: "))
    list1+=[num]
print(list1)
count=len//2
high=0
count1=1
high=0
for i in range(len):
    for j in range(i+1,len):
        if list1[i]==list1[j]:
            count1+=1
        else:
            count1+=0
    if high<count1:
        high=count1
    count1=1
if high>count:
    print(f" Repeating element greater than n/2 is {list1[i]}")
else:
   print("No Vlaue is Greaterr than n//2")

# Maximum Difference 
# Task: Find the maximum value of arr[j] - arr[i] where j > i. 
# Example Input: Input: [2, 3, 10, 6, 4, 8, 1] Example Output: Output: 8
len=int(input("Enter the list length: "))
list1=[]
for i in range(len):
    num=int(input("Enter a num: "))
    list1+=[num]
print(list1)
high=0
for i in range(len):
    for j in range(len):
        if i>j:
            val=list1[i]-list1[j]
            if high<val:
                high=val   
        else:
            continue
print(high)

# Equilibrium Index 
# Task: Find an index where the sum of elements on the left equals the sum on the right.
# Example Input: Input: [1, 3, 5, 2, 2] Example Output: Output: 2
len=int(input("Enter the list length: "))
list1=[]
for i in range(len):
    num=int(input("Enter a num: "))
    list1+=[num]
print(list1)
for i in range(len):
    sum1=0
    sum2=0
    for j in range(i):
        sum1+=list1[j]
    for k in range(i+1,len):
        sum2+=list1[k]
    if sum1==sum2:
        print(f"The Index is {i}")
        break
   
# #Find All Pairs with Given Sum
# Find every pair whose sum equals the target. Example: List=[1,5,7,-1,5] Target=6 Pairs: (1,5) (7,-1)
#(1,5) Return all valid pairs.
list1=[1,5,7,-1,5]
n=len(list1)
target=6
op_list=[]
for i in range(n):
    for j in range(i+1,n):
        if list1[i]+list1[j]==target:
            op_list+=[(list1[i],list1[j])]   
print(op_list)

# Partition Even and Odd Numbers
# Move all even numbers before all odd numbers. Do not sort. Example: [12,17,70,15,22,65,21,90]
# Output: [12,70,22,90,17,15,65,21]
list1=[12,17,70,15,22,65,21,90]
even_list=[]
odd_list=[]
for i in list1:
    if i%2==0:
        even_list+=[i]
    else:
        odd_list+=[i]
fin_list=even_list+odd_list
print(fin_list)


# Smallest Missing Positive Integer
# Ignore negative numbers and zero. Starting from 1, find the first positive number missing. Example:
# [3,4,-1,1] 1 exists. 2 is missing. Answer=2.
list1=[3,4,-1,1]
i=1
while True:
    if i in list1:
        i+=1
        continue
    else:
        print(f"Missing number: {i}")
        i+=1
        break
    
    