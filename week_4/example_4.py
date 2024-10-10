import operator
from argparse import _StoreTrueAction
from cgi import print_environ
from webbrowser import get


def greeting():
    print("hello")


def salutation(name_from_user):
    print(f"Salutations {name_from_user}")


def rating(wind_speed, storm_surge):
    print(wind_speed * storm_surge)
    print(f"Wind Speed: {wind_speed}")


def danger(wind_speed, storm_surge, message="evacuate"):
    print(f"Rating: {wind_speed * storm_surge}")
    print(message)


def big_danger(wind_speed, storm_surge, message="evacuate", x="NOW"):
    print(f"Rating: {wind_speed * storm_surge}")
    if (wind_speed * storm_surge) > 400:
        print(f"{message}, {x}")


def insturance(asset_purchase_price, asset_age, storm_rating):
    full_payout = asset_purchase_price
    depreciated_payout = asset_purchase_price / asset_age
    pain_suffering = asset_purchase_price * storm_rating * 0.05
    return full_payout, depreciated_payout, pain_suffering


greeting()
salutation("Andrew")

hurricane = "Nadine"
salutation(hurricane)

print(hurricane)
test_value = operator.mul(6, 10)
rating(5, 10)
print(test_value)
danger(100, 4)
user_first = int(input("Please enter the first value for the Wind Speed: "))
user_second = int(input("Please enter the second value for the storm surge: "))

assumption = big_danger(user_first, user_second)
print(assumption)
full, depreciated, p = insturance(100000, 10, 2)

print(full, depreciated, p)


def get_loan_info():
    principal = float(input("Enter the amount you will borrow: "))
    rate = float(input("Please enter the annual interest rate: "))
    years = int(input("Please enter the years: "))
    return principal, rate, years


def calculate_monthly_payment(principal_passed, rate_passed, years_passed):
    r = rate_passed / 12
    n = years_passed * 12
    a = principal_passed * ((rate_passed * (1 + r) ** n) / ((1 + r)) ** n - 1)
    return a


prin, rate, years = get_loan_info()

print(calculate_monthly_payment(prin, rate, years))

print(calculate_monthly_payment(300_000, 0.05, 30))

def __main__():


if __name__ == "__main__":
    
