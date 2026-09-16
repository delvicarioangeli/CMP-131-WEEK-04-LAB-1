# Name: Angelina Del Vicario
# Lab: 01
# Week: 04 
# Date: 09/13/2026
#
principal = float(input("Enter the starting principal amount ($):"))
annual_rate_percent = flloat(input("Enter the annual intrest rate (as a %):"))
compounding_periods = int(input("Enter the number of times intrest is compounded in a year"))

r = annual_rate_percent / 100

amount_after_one_year = principal * (1 + r / compounding_periods) ** compounding_periods
intrest_earned = amount_after_one_year - principal

print ("Initial Deposit: $" + principal )
print ("Intrest Earned after 1 year:  $" +intrest_earned)
print ("Ending balance: $" + amount_after_one_year)