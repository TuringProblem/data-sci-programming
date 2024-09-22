#######################################################################
## formula for calculating monthly payments on a fixed rate mortgages:#
## A = P(r(1+r)^n/(1+r)^n-1)                                         ##
## A == payment amount per period                                    ##
## P == initial principal (Loan amount)                              ##
## R == interest rate per period                                     ##
## n == total number of payments or periods                          ##
#######################################################################
#    | Author @Override: | See: https:github.com/TuringProblem |     ##
#######################################################################
import math

def calc(p, r, n):
    rate = r / 12
    years = n * 12
    a =  p * (rate * (1 + rate) ** years) / ((1 + rate) ** years - 1)
    return round(a, 2)

p = float(input("Please enter the amount you will borrow: "))
r = float(input("Enter the annual interest rate as a decimal\n[EXAMPLE] -> .05 == 5%: "))
n = float(input("Enter the number of years on the loan: "))

print(f"The Monthly payment is: {calc(p, r, n)}")




