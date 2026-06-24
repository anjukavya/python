#keep accepting the ages until the user enters -1 and skip when age is less than 1 or greater than 120, Find the valid ages
count=0
a=True
while a:
    age=int(input("enter ages:"))
    if age==-1:
        a=False
        continue
    elif age<1 or age>120:
        continue
    count+=1
print(f"valid ages:{count}")    


#keep accepting numbers until user enter 0, add only number divisible by 5, skip all other numbers
sum=0
a=True
while a:
    number=int(input("Enter number: "))
    if number==0:
        a=False
        continue
    elif number%5!=0:
        continue
    sum+=number
print(f"Total Sum: {sum}")


#Given text="PyTHon ProGRAM" count how many upper case letters are present skip all other by using continue.
text="PyTHon ProGRAM"
count=0
for i in text:
    if  "A"<=i<="Z":
        count+=1
    continue
print(f"Uppercase Letters count: {count}")

#Given sales=[500, 0, 1200, 0, 700] Find the total sales amount, Entries 0 should be skipped
sum=0
sales=[500, 0, 1200, 0, 700]
for i in sales:
    if i==0:
        continue
    sum+=i
print(f"Total Sales: {sum}")