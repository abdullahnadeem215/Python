a = int(input("Enter your first no. : "))

op = input("Enter operation(-+*/):" )

b = int(input("Enter your second no. : "))

ans = None

if op == "-":
    ans = a-b
    print(ans)
if op == "+":
    ans = a+b
    print(ans)
if op == "*":
    ans = a*b
    print(ans)
if op == "/":
    ans =a/b
    print(ans)
else:
    print("plese enter the valid operator")