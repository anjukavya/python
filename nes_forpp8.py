for i in range(1,6):
    Total=0
    for j in range(1,4):
        marks=int(input(f"Subject {j} marks: "))
        Total+=marks
    print(f"Student {i} total marks: {Total}")

for i in range(1,5):
    total=0
    for j in range(1,8):
        sales=int(input(f"Day {j} sale : "))
        total+=sales
    print(f"Product 1 Total Sales: {total}")

for i in range(1,5):
    high=0
    for i in range(1,6):
        mark=int(input(f"Enter sub{i} marks:"))
        if mark>high:
            high=mark
    print(f"Highest Mark: {high}")


booked = []
print("Enter seat status:")
for i in range(5): 
    count = 0
    for j in range(6): 
        seat = int(input(f"Row {i+1}, Seat {j+1}: "))
        if seat == 1:
            count += 1
    booked.append(count)
for i in range(5):
    print("Row", i+1, "Booked Seats =", booked[i])