# Get two integers from user
int1, int2 = input("Enter two integers: ").split()

# Convert to integers
int1 = int(int1)
int2 = int(int2)

# Print integer quotient
print("Integer quotient: " + str(int1 // int2))

# Print real quotient
print("Quotient: " + str(int1 / int2))

# Print remainder
print("Remainder: " + str(int1 % int2))