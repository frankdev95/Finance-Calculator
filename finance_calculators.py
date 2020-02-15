import math

# Asks the user to type the type of calculator they require, investment or bond.
print("""Choose either 'investment' or 'bond' from the menu below to proceed: \n
investment     - to calculate the amount of interest you'll earn on interest
bond           - to calculate the amount you'll have to pay on a home loan\n""")

user_choice = input("Please enter choice here: ").lower()

# Depending on their choice, questions are asked to the user, the answers are then
# used in an equation to print the correct result.
if user_choice == "investment":

    amount = float(input("\nEnter amount of money depositing: "))
    interest_rate = float(input("Enter the interest rate: "))
    years = float(input("Enter number of years planning on investing: "))
    interest_type = input("Enter type of interest (simple or compound): ").lower()

    r = interest_rate / 100

    if interest_type == "simple":

        # Simple interest equation
        a = amount * (1 + r * years)
        print(f"\nAMOUNT: {a}")
        
    else:

        # Compound interest equation
        a = round(amount * math.pow((1 + r), years), 2)
        print(f"\nAMOUNT: {a}")

elif user_choice == "bond":
    
    house_value = float(input("\nEnter the current value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    repayment_time = float(input("Enter the number of months you plan to take to repay the bond: "))


    pv = house_value
    n = repayment_time
    r = (interest_rate / 12) / 100

    # Bond repayment equation    
    repayment = round(pv * ((r * (1 + r)**n) / (((1 + r)**n)-1)),2)
    
    print(f"\nMONTHLY REPAYMENT AMOUNT: {repayment}")

else:
    print("\nError, please restart program and enter a valid option\n")

input("\nPress ENTER to exit")
