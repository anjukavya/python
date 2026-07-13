# Task: Create a function generate_report(student) that accepts student details and
# generates a complete performance report. The function should calculate total marks, 
# average marks, highest scoring subject, grade and pass/fail status.
# Example Input: student = { "name": "Rahul", "marks": { "Math": 85, "Science": 72, "English": 90 } } 
# Example Output: Name: Rahul Total Marks: 247 Average: 82.33 Highest Subject: English Grade: B Status: Pass
# def studentData(name,**marks):
#     sum=0
#     high=0
#     sub=""
#     count=0
#     for i in marks:
#         count+=1
#         sum+=marks[i]
#         if high<marks[i]:
#             high=marks[i]
#             sub=i
#     avg=sum/count
#     grade=""
#     if 250<=sum<=300:
#         grade="A"
#         Status="PASS"
#     elif 200<=sum<=249:
#         grade="B"
#         Status="PASS"
#     elif 150<=sum<=199:
#         grade="C"
#         Status="PASS"
#     else: 
#         Status="Fail"
#     print(f"Name: {name}")
#     print(f"Total marks: {sum}")
#     print(f"Average marks: {avg}")
#     print(f"Highest Subject: {sub}")
#     print(f"Grade: {grade}")
#     print(f"Status: {Status}")
# studentData(name="Kavya",Math=85,Science=72,English=90)

# Bank Account Simulator Task: Create process_account(balance, transactions).
# Process deposits and withdrawals, calculate final balance, total deposits, total withdrawals, highest withdrawal and transaction count. Example 
# Input: balance = 5000 transactions = [ ("deposit", 2000), ("withdraw", 1500), ("withdraw", 800), ("deposit", 1000) ] 
# Example Output: Final Balance: 5700 Total Deposits: 3000 Total Withdrawals: 2300 Highest Withdrawal: 1500 Total Transactions: 4
# def transactionData(balance,**transactions):
#     final_balance=balance
#     withdraws=0
#     Deposits=0
#     total_withdraws=0
#     total_deposits=0
#     Total_trans=0
#     high=0
#     for i in transactions:
#         Total_trans+=1
#         if transactions[i]>0:
#             final_balance+=transactions[i]
#             Deposits+=1
#             total_deposits+=transactions[i]
#         elif transactions[i]<0:
#             final_balance+=transactions[i]
#             withdraws+=1
#             total_withdraws+=-transactions[i]
#             if high<-transactions[i]:
#                 high=-transactions[i]
#     print(f"Final Balance: {final_balance}")
#     print(f"Total Deposits: {total_deposits}")
#     print(f"Total Withdraws: {total_withdraws}")
#     print(f"Highest withdraw: {high}")
#     print(f"Total transactions: {Total_trans}")   
# transactionData(balance=5000,deposit=2000,withdraw=-1500,withdraws=-800,deposite=1000)


# Online Shopping Order Processor Task: Create process_order(cart, coupon). 
# Calculate subtotal, discount, delivery charge, costliest product and final amount.
# Example Input: cart = { "Laptop": 50000, "Mouse": 500, "Keyboard": 1500 } 
# coupon = "SAVE10" 
# Example Output: Subtotal: 52000 Discount: 5200 Delivery Charge: 0 Most Expensive Product: Laptop Final Amount: 46800
# def onlineShopping(coupon,**cart):
#     subtotal=0
#     high=0
#     for i in cart:
#         sub=""
#         subtotal+=cart[i]
#         if high<cart[i]:
#             high=cart[i]
#             sub=i
#     discount=subtotal*(10/100)
#     print(f"coupon {coupon}")
#     print(f"subtotal: {subtotal}")
#     print(f"Discount: {discount}")
#     print(f"Delivery charge: 0")
#     print(f"Most Expensive Product: {sub}")
#     print(f"Final Amount: {subtotal-discount}")
# onlineShopping(coupon="SAVE10",Laptop=50000,Mouse=500,Keyboard=1500 )

# Employee Performance Analyzer Task: Create employee_review(employee). 
# Calculate average score, highest score, low performance months and rating.
# Example Input: employee = { "name": "John", "scores": [80, 60, 90, 40, 75] } 
# Example Output: Employee: John Average Score: 69 Highest Score: 90 
# def employee(name,*scores):
#     sum=0
#     count=0
#     high=0
#     for i in scores:
#         count+=1
#         sum+=i
#         if high<i:
#             high=i
#     avg=sum//count
#     print(f"{name} average Score: {avg}")
#     print(f"Highest Score {high}")
# employee("John",80,60,90,40,75)

# Password Security System Task: Create security_check(password). 
# Check length, uppercase, lowercase, digits, special characters and calculate security score. 
# Example Input: password = "Python123" Example Output:  Length: Valid   Uppercase: Yes   Lowercase: Yes 
# Digit: Yes   Special Character: No   Security Score: 3/4 Strength: Medium
# def security_check(password):
#     Upper=0
#     Lower=0
#     Digit=0
#     special=0
#     count=0
#     letter=""
#     for char in password:
#         if "A"<=char<="Z":
#             Upper=True
#         elif "a"<=char<="z":
#             Lower=True
#         elif "1"<=char<="9":
#             Digit=True
#         else:
#             special=True
#     if len(password)>=8:
#         print("Length : Valid")
#     else:
#         print("Length: Invalid")
#     if Upper:
#         count+=1
#     if Lower:
#         count+=1
#     if Digit:
#         count+=1
#     if special:
#         count+=1
#     if count==4:
#         Strength="Strong"
#     elif count==3:
#         Strength="Medium"
#     else:
#         Strength="Weak"
#     print("Uppercase: ","Yes" if Upper else "No" )
#     print("Lowercase: ","Yes" if Lower else "No" )
#     print("Digit: ","Yes" if Digit else "No" )
#     print("Special: ","Yes" if special else "No" )
#     print(f"Security Score: {count}/4")
#     print("Strength:",Strength) 
# security_check("Python123")


# Task: Create patient_summary(patients). Count patients, average age, critical patients, oldest patient and department count. 
# Example Input: patients = [ {"name":"Ravi","age":45,"dept":"Cardiology","critical":True}, 
# {"name":"Anu","age":30,"dept":"Dental","critical":False}, {"name":"Raj","age":70,"dept":"Cardiology","critical":True} ] 
# Output: Total Patients: 3 Average Age: 48.33 Critical Patients: 2 Oldest Patient: Raj
# def patient_summary(**patients):
#     names=patients["name"]
#     ages=patients["age"]
#     depts=patients["dept"]
#     criticals=patients["critical"]
#     count=0
#     for i in names:
#         count+=1
#     print(f"Total Patients: {count}")
#     sum=0
#     high=0
#     pat=-1
#     pat_name=""
#     for i in ages:
#         sum+=i
#         pat+=1
#         if high<i:
#             high=i
#             pat_name=names[pat]
#     print(f"Average age: {sum/count:.2f}")
#     crit=0
#     for i in criticals:
#         if i:
#             crit+=1
#     print(f"Critical Patients: {crit}")
#     print(f"Oldest Patient: {pat_name}")
# patient_summary(name=["Ravi","Anu","Raj"],age=[45,30,70],dept=["Cardiology","Dental","Cardiology"],critical=[True, False, True])

# Bus Travel Management Task: Create bus_report(passengers,total_seats). 
# Calculate passengers, revenue, highest ticket passenger, available seats and occupancy. 
# Example Input: passengers = [ {"name":"Ram","seat":1,"price":500}, {"name":"John","seat":2,"price":700}, 
#                              {"name":"Sam","seat":3,"price":400} ] 
# total_seats = 10 Example Output: Total Passengers: 3 Total Revenue: 1600 Highest Ticket Passenger: John Available Seats: 7 Occupancy: 30%


