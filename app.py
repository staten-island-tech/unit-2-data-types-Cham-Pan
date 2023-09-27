numberx = int(input("Enter a number: "))
numbery = int(input("Enter a number: "))

for i in range(1, numberx + 1):
    if numberx % i == 0:
        print(i)

for i in range(1, numbery + 1):
    if numbery % i == 0:
        print(i)