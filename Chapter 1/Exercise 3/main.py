# Get two integers from user
int1, int2 = input("Enter two integers: ").split()

# Convert to integers
int1 = int(int1)
int2 = int(int2)

# Print sum and product
print("Sum: " + str(int1 + int2))
print("Product: " + str(int1 * int2))