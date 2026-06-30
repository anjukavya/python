# Initialize the counter
num = 1

# Loop through numbers from 1 to 10
while num <= 10:

    # Stop the loop when the number reaches 8
    if num == 8:
        # break exits the loop completely
        break

    # Check if the number is odd
    if num % 2 != 0:
        # Move to the next iteration without printing
        num += 1
        continue

    # Print only even numbers
    print(num)

    # Increment the counter
    num += 1