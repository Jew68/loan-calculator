import math


print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
question = input()
if question == 'n':
    print('Enter the loan principal:')
    principal = float(input())
    print('Enter the monthly payment:')
    monthly_payment = float(input())
    print('Enter the loan interest:')
    interest = float(input())
    i = (interest / 100) / 12
    n = math.log(monthly_payment / (monthly_payment - i * principal), 1 + i)
    answer_months = math.ceil(n) % 12
    answer_years = int((math.ceil(n) - answer_months) / 12)
    if answer_months > 0 and answer_years > 0:
        print(f'It will take {answer_years} years and {answer_months} months to repay this loan!')
    elif answer_months == 0:
        print(f'It will take {answer_years} years to repay this loan!')
    else:
        print(f'It will take {answer_months} months to repay this loan!')
if question == 'a':
    print('Enter the loan principal:')
    principal = float(input())
    print('Enter the number of periods:')
    periods = float(input())
    print('Enter the loan interest:')
    interest = float(input())
    i = (interest / 100) / 12
    a = round(principal * (i * (1 + i) ** periods / ((1 + i) ** periods - 1)))
    print(f'Your monthly payment = {a}!')
if question == 'p':
    print('Enter the annuity payment:')
    annuity_payment = float(input())
    print('Enter the number of periods:')
    periods = float(input())
    print('Enter the loan interest:')
    interest = float(input())
    i = (interest / 100) / 12
    p = math.floar(annuity_payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1)))
    print(f'Your loan principal = {p}!')
    
