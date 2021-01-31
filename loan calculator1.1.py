import math


principal = int(input("Enter the loan principal:"))
question = input("""What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:""")
if question == "m":
    payments = int(input("Enter the monthly payment:"))
    speed = math.ceil(principal / payments)
    print()
    if speed == 1:
        print("It will take 1 month to repay the loan")
    else:
        print(f"It will take {speed} months to repay the loan")
if question == "p":
    months = float(input("Enter the number of months:"))
    amount1 = principal / months
    if int(amount1) == float(amount1):
        amount1 = int(amount1)
        print()
        print(f"Your monthly paymet = {amount1}")
    else:
        amount1 = math.ceil(amount1)
        amount2 = principal - (months - 1) * amount1
        print()
        print(f"Your monthly payment = {amount1} and the last payment = {amount2}.")


