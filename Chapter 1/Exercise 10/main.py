# Write a program that asks 5 integer numbers and prints the average after each entry using 2
# decimal places. Do not use loops for this assignment and use 4 variables at most!

# Declare a list
numbers = []

# Ask for first number
numbers.append(int(input("Enter integer number 1: ")))
# Print average
print("Average so far: {:.2f}".format(sum(numbers) / len(numbers)))

# Ask for second number
numbers.append(int(input("Enter integer number 2: ")))
# Print average
print("Average so far: {:.2f}".format(sum(numbers) / len(numbers)))

# Ask for third number
numbers.append(int(input("Enter integer number 3: ")))
# Print average
print("Average so far: {:.2f}".format(sum(numbers) / len(numbers)))

# Ask for fourth number
numbers.append(int(input("Enter integer number 4: ")))
# Print average
print("Average so far: {:.2f}".format(sum(numbers) / len(numbers)))

# Ask for fifth number
numbers.append(int(input("Enter integer number 5: ")))
# Print average
print("Average so far: {:.2f}".format(sum(numbers) / len(numbers)))