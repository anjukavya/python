i=1
while i<=5:
    j=i
    while j<=5:
        if (i+j)%2==0:
            print(f"({i},{j})")
        j+=1
    i+=1


i=1
count=0
while i<=10:
    j=i
    while j<=10:
        m=i*j
        if m>30:
            print(f"({i},{j}) --> {i*j}")
            count+=1
        j+=1
    i+=1
print(f"Total pairs: {count}")


num=int(input("Enter Number: "))
while num!=0:
    total=0
    for i in range(1,num+1):
        if num%i==0:
            print(i)
            total+=i
           
    print(f"Total sum: {total}")            
    num=int(input("Enter Number: "))
print("Program Ended")
        
list_1=[12,7,20,9]
for i in list_1:
    num=1
    count=0
    while num<=i:
        if num%2==0:
            count+=1
        num+=1
    print(f"{i}--> Even count - {count}")
         