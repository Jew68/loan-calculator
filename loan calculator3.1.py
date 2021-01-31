import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--type",
                    choices=["diff", "annuity"])
parser.add_argument("--payment", default=False)
parser.add_argument("--principal", default=False)
parser.add_argument("--periods", default=False)
parser.add_argument("--interest", default=False)

args = parser.parse_args()

ppp = [args.principal, args.periods, args.payment]

P = float(args.principal)
i = float(args.interest) / 1200
n = int(args.periods)
A = int(args.payment)

conditions1 = (P < 0, i < 0, n < 0)
conditions2 = (
    args.principal is not False, args.periods is not False, args.interest is not False, args.payment is False)
conditions3 = (
    args.payment is not False, args.periods is not False, args.interest is not False, args.principal is False)
conditions4 = (
    args.principal is not False, args.payment is not False, args.interest is not False, args.periods is False)

if any(conditions1):
    print("Incorrect parameters")
elif args.type == "diff":
    if all(conditions2):
        total_payment = 0
        for month in range(1, n + 1):
            print("Month " + str(month) + " : payment is " + str(math.ceil(P / n + i * (P - ((P * (month - 1)) / n)))))
            total_payment += math.ceil(P / n + i * (P - ((P * (month - 1)) / n)))
        print()
        print("Overpayment = " + str(int(total_payment - P)))
    else:
        print("Incorrect parameters")
elif args.type == "annuity":
    if all(conditions2):
        A = math.ceil(P * (i * (1 + i) ** n / ((1 + i) ** n - 1)))
        print("Your annuity payment = " + str(A) + "!")
        print("Overpayment = " + str(int(n * A - P)))
    elif all(conditions3):
        P = A / (i * (1 + i) ** n / ((1 + i) ** n - 1))
        print("Your loan principal = " + str(math.floor(P)) + "!")
        print("Overpayment = " + str(math.ceil(n * A - P)))
    elif all(conditions4):
        n = math.log(A / (A - i * P), 1 + i)
        answer_months = math.ceil(n) % 12
        answer_years = int((math.ceil(n) - answer_months) / 12)
        if answer_months > 0 and answer_years > 0:
            print(f'It will take {answer_years} years and {answer_months} months to repay this loan!')
        elif answer_months == 0:
            print(f'It will take {answer_years} years to repay this loan!')
        else:
            print(f'It will take {answer_months} months to repay this loan!')
        print("Overpayment = " + str(int(math.ceil(n) * A - P)))
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
