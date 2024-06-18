operation = input("")
operation = operation.split()
print(operation)
x = int(operation[0])
y = operation[1]
z = int(operation[2])
if y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
elif y == "/":
    print(float(x/z))


