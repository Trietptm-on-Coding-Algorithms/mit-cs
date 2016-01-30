
balance = 93
annualInterestRate = 0.2


def determine_monthly_payment(starting_balance, annual_interest_rate):
    """
    Uses a simple increment method to find the lowest payment to the nearest 10
    :param starting_balance:
    :param annual_interest_rate:
    :return:
    """

    fixed_payment = 10

    runs = 0

    end_balance = calculate_year_end_balance(starting_balance, fixed_payment, annual_interest_rate)

    while end_balance > 0:
        fixed_payment += 10
        end_balance = calculate_year_end_balance(starting_balance, fixed_payment, annual_interest_rate)

        runs += 1

    print "Lowest Payment:", fixed_payment


def calculate_year_end_balance(starting_balance, monthly_payment, annual_interest_rate):

    running_balance = starting_balance

    for month in range(12):

        running_balance -= monthly_payment

        monthly_interest_rate = (annual_interest_rate/12.0)

        interest_charged = monthly_interest_rate * running_balance

        running_balance += interest_charged

    return running_balance


determine_monthly_payment(balance, annualInterestRate)

