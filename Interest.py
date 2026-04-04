# This simple program uses the concepts of functions to calculate the profit/interest for a given 
# principal, rate of interest and time period.

grace = int(input("Enter the grace period in months: "))   # grace period
amount = float(input("Enter the principle amount: "))      # principal amount   
rate = float(input("Enter the interest/profit rate: "))    # rate of interest/profit
f_balance = 0

# Function to calculate the interest/profit for the given amount, rate and time period.
def cal_interest(amount):
    # ((1000/100)*5)12
    f_balance = ( ( amount / 100) * rate ) * grace
    print(f_balance)       


cal_interest(amount)