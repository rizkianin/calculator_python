num1 = float(input("masukkan num1 = "))
operator = input("masukkan operator = ")
num2 = float(input("masukkan num2 = "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("invalid operator")
