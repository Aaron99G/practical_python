# Get the loan details
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What's the annual percantage rate?\n"))    
payment = float(input("What will your monhtly payment, in dollars be??\n")) 
months = int(input("How many months to pay it off?\n")) 

#Divide apr by 100 to make it a percent, then by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):    
    # Add interest
    intrest_paid = money_owed* monthly_rate
    money_owed = money_owed + intrest_paid
    
    if (money_owed - payment < 0):
        print("The last payment is ", money_owed)
        print("You paid the loan off in ", i+1, "months")
        break

    # Make Payment
    money_owed = money_owed - payment

    # Print results
    print("Paid", payment, "of which", intrest_paid, "was intrest", end=' ')
    print("Now I owe: ", money_owed)