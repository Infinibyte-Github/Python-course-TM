# Ask for amount of Euro's
amount = int(input("Enter amount of Euro's: "))

# print what bills and coins this represents
print("This represents:")
print("{} 500 Euro bills".format(amount // 500))
amount %= 500
print("{} 200 Euro bills".format(amount // 200))
amount %= 200
print("{} 100 Euro bills".format(amount // 100))
amount %= 100
print("{} 50 Euro bills".format(amount // 50))
amount %= 50
print("{} 20 Euro bills".format(amount // 20))
amount %= 20
print("{} 10 Euro bills".format(amount // 10))
amount %= 10
print("{} 5 Euro bills".format(amount // 5))
amount %= 5
print("{} 2 Euro coins".format(amount // 2))
amount %= 2
print("{} 1 Euro coins".format(amount // 1))
amount %= 1