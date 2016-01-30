balance = 320000
annualInterestRate = 0.2


def determine_monthly_payment(starting_balance, annual_interest_rate):
    """
    Uses bisection search to find the lowest monthly payment to the penny
    :param starting_balance:
    :param annual_interest_rate:
    :return:
    """

    monthly_interest_rate = annual_interest_rate / 12.0

    epsilon = 0.01
    upper = (starting_balance * (1 + monthly_interest_rate)**12) / 12.0
    lower = starting_balance / 12.0

    fixed_payment = (upper + lower) / 2.0

    end_balance = calculate_year_end_balance(starting_balance, fixed_payment, annual_interest_rate)

    while abs(end_balance) > epsilon:

        if end_balance < 0:
            upper = fixed_payment
        elif end_balance > 0:
            lower = fixed_payment

        fixed_payment = (upper + lower) / 2.0

        end_balance = calculate_year_end_balance(starting_balance, fixed_payment, annual_interest_rate)

    print "Lowest Payment:", round(fixed_payment, 2)


def calculate_year_end_balance(starting_balance, monthly_payment, annual_interest_rate):

    running_balance = starting_balance

    for month in range(12):

        running_balance -= monthly_payment

        monthly_interest_rate = (annual_interest_rate/12.0)

        interest_charged = monthly_interest_rate * running_balance

        running_balance += interest_charged

    return running_balance


determine_monthly_payment(balance, annualInterestRate)

