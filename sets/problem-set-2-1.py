# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def payment_table(starting_balance, annual_interest_rate, monthly_payment_rate):

    paid = 0
    running_balance = starting_balance

    for month in range(12):

        minimum_monthly_payment = running_balance * monthly_payment_rate

        running_balance -= minimum_monthly_payment

        monthly_interest_rate = (annual_interest_rate/12.0)

        interest_charged = monthly_interest_rate * running_balance

        running_balance += interest_charged

        paid += minimum_monthly_payment

        display_month = month + 1

        print "Month:", display_month
        print "Minimum monthly payment:", round(minimum_monthly_payment, 2)
        print "Remaining balance:", round(running_balance, 2)

    print "Total paid:", round(paid, 2)
    print "Remaining balance:", round(running_balance, 2)


payment_table(balance, annualInterestRate, monthlyPaymentRate)

