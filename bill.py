bill = 25
x = input("Was the service great, good, okay, or bad?")

if x == "great":
    bill *= 1.25
    print(f"Your bill comes up to ${round(bill, 2)} with tip.")
elif x == "good":
    bill *= 1.2
    print(f"Your bill comes up to ${round(bill, 2)} with tip.")
elif x == "okay":
    bill *= 1.15
    print(f"Your bill comes up to ${round(bill, 2)} with tip.")
else:
    print(f"Your bill comes up to ${round(bill, 2)}.")