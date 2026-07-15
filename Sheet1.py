# Swap Two Numbers Without Third Variable Definition: Exchange values of two variables without using an extra variable. 
# Task: Swap using arithmetic operators and bitwise XOR. Example Input: A=15, B=25 Example Output: A=25, B=15
a=15 #01111
b=25 #11001
a=a^b #10110 #22
b=a^b #01111 #15
a=a^b #11001 #25
print(f"A={a}")
print(f"B={b}")


# Convert Seconds Into Hours, Minutes and Seconds Definition: Convert total seconds into time units. 
# Task: Find hours, minutes and remaining seconds. Example Input: Total seconds=7384 
# Example Output: Hours=2, Minutes=3, Seconds=4
Total_seconds=7384
hours=Total_seconds//3600
balance=Total_seconds-(3600*hours)
minutes=balance//60
seconds=balance-(60*minutes)
print(hours)
print(minutes)
print(seconds)


# Temperature Conversion System Definition: Convert temperature values between Celsius and Fahrenheit. 
# Task: Convert Celsius to Fahrenheit and Fahrenheit to Celsius. Example Input: Celsius=30 
# Example Output: Fahrenheit=86
Celsius=30
fhrnht=(Celsius*(9/5))+32
print(f"Fehrenhiet = {fhrnht:.0f}")

# Calculate Compound Amount Definition: Compound interest calculates interest on both the original amount and 
# previously earned interest. Task: Calculate final amount using the compound interest formula. 
# Formula: Amount = P × (1 + R/100)^T Where: P = Principal amount R = Rate of interest T = Time period 
# Example Input: Principal = 10000 Rate = 10 Time = 2 years Example Output: Final Amount = 12100
Principal = 10000
Rate = 10 
Time = 2
com_int=Principal * ((1+Rate/100))**Time
print(f"Final_Amount: {com_int:.0f}")

# Split Bill Among Friends Definition: Divide a total bill equally among people. 
# Task: Find each person's share and remaining amount.Example Input: Bill=2455, Friends=5 
# Example Output: Each pays=491, Remaining=0
Bill=2455
Friends=5
Each_pay=Bill//Friends
remaining=Bill-(Each_pay*Friends)
print(f"Each Pay {Each_pay}")
print(f"Remaining {remaining}")

# Convert Distance Units Definition: Convert kilometers into smaller units. 
# Task: Convert km into meters, centimeters and millimeters. 
# Example Input: Distance=5 km Example Output: Meters=5000, Centimeters=500000, Millimeters=5000000
Distance=5
print(f"Meters {Distance*1000}")
print(f"Centimeters {Distance*100000}")
print(f"Millimeters {Distance*1000000}")

# Digital Storage Conversion Definition: Convert storage units from GB to smaller units. 
# Task: Convert GB into MB, KB and Bytes. Example Input: Storage=2 GB 
# Example Output: MB=2048, KB=2097152, Bytes=2147483648 
Storage_GB=2
MB=Storage_GB*1024
KB=MB*1024
Bytes=KB*1024
print(f"MB = {MB}  KB = {KB}  Bytes = {Bytes}")

# Minimum Currency Notes Definition: Find the number of currency notes required for an amount. 
# Task: Use 500, 200, 100 and 50 denomination notes. Example Input: Amount=1850 
# Example Output: 500 notes=3, 200 notes=1, 100 notes=1, 50 notes=1
Amount=1850 
Five=Amount//500
balance=Amount-(Five*500)
print(f"500 notes={Five}")
Two=balance//200
balance2=balance-(Two*200)
print(f"200 Notes={Two}")
One=balance2//100
balance3=balance2-(One*100)
print(f"100 Notes={One}")
Fifty=balance3//50
print(f"50 Notes={Fifty}")

# Salary Calculation System Definition: Calculate final salary after adding bonus and deducting tax. 
# Task: Calculate the final salary. Example Input: Salary=40000, Bonus=5000, Tax=10% 
# Example Output: Final Salary=40500
Salary=40000 
Bonus=5000 
Tax=10
Tax_pay=(Salary+Bonus)*(Tax/100)
print(f"Total Salary= {Salary+Bonus-Tax_pay:.0f}")

# Travel Time Calculator Definition: Calculate travel duration using distance and speed. 
# Task: Find time for two journeys and total time. Formula: Time = Distance / Speed 
# Example Input: Distance1=120, Speed1=60, Distance2=100, Speed2=50 
# Example Output: Journey1=2 hours, Journey2=2 hours, Total=4 hours
Distance1=120
Speed1=60
Distance2=100
Speed2=50
Time1=Distance1//Speed1
Time2=Distance2//Speed2
print(f"Journey1={Time1} hours")
print(f"Journey2={Time2} hours")
print(f"Total={Time1+Time2} hours")