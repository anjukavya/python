print("1.Addition, 2.Substraction, 3.Multiplication, 4.Division, 5.Modulus, 6.Floor_division, 7.Power, 8.exit")
aws=0
while True:
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        def addition(a,b):
            aws=0
            sum=a+b
            aws+=sum
            return aws
        aws=addition(230,520)
        print(aws)
    if choice==2:
        def substraction(b,a=aws):
            aws=a-b
            return aws
        aws=substraction(40)
        print(aws)
    if choice==3:
        def multiplication(b,a=aws):
            aws=a*b
            return aws
        aws=multiplication(10)
        print(aws)
    if choice==4:
        def division(b,a=aws):
            if b>0:
                aws=a/b
                return aws
            else:
                return "Invalid value"
        aws=division(5)
        print(aws)
    if choice==5:
        def modulus(b,a=aws):
            if b>0:
                aws=a%b
                return aws
            else:
                return "Invalid value"
        aws=modulus(aws,6)
        print(aws)
    if choice==6:
        def floor_division(b,a=aws):
            if b>0:
                aws=a//b
                return aws
            else:
                return "Invalid value"
        aws=floor_division(aws,2)
        print(aws)
    if choice==7:
        def power(b,a=aws):
            aws=a**b
        aws=power(aws,3)
        print(aws)
    if choice==8:
        def show(a=aws):
            return a
        aws=show()
        print(aws)
    if choice==9:
        def clear(a=aws):
            a=0
            return a
        aws=clear()
        print(aws)








