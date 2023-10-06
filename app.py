number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if number1 < number2:
    smaller_number = number1
else:
    smaller_number = number2

for i in range(1, smaller_number + 1):
    if (number1 % i == 0) and (number2 % i == 0):
        gcf = i
    else:
        gcf = 1
print(i)