# Ask for U, R1, R2
U = float(input("Enter U[V]: "))
R1 = float(input("Enter R1[Ohm]: "))
R2 = float(input("Enter R2[Ohm]: "))

# Calcualte I, U2
I = U / (R1 + R2)
U2 = I * R2

# Print I, U2
print("I = {:.6f} A, U2 = {:.6f} V".format(I, U2))