ori = input("")
xyz = ori.split(" ")

x = xyz[0]
y = xyz[1]
z = xyz[2]

if y == "+":
    print(x+z)
if y == "-":
    print(x-z)
if y == "*":
    print(x*z)
if y == "/":
    print(x/z)
