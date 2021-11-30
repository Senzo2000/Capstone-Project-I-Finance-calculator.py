import math

print("Choose either investments or bonds from the menu below to proceed:""\n" "\n"
      "investment      - to calcuate the amount of intrest you'll earn on intrest""\n"
      "Bonds           - to calculate the amount you'll have to pay on a home loan")# for new line type "\n" 




investments_bonds = input("\n""investments or bonds:")

if (investments_bonds != "investments") and (investments_bonds != "bonds"):#the strings in the brackets should also be put in quotes("")
    print("Error!!! enter approriatly")                                    #spelling of values should be exacly the same after you use it  


elif investments_bonds == "investments":
    investment_deposite = float(input("How much money are you willing to deposite ? :"))#for elif statements all the variables should be aligned 
    investment_rate = float(input("What would your intrest rate be ? :"))#entered floats because were dealing with intrest rates and prices
    investment_years = int(input("How many years do you plan on investing for? :"))
    interest = (input("Do you want 'simple' or 'compound' interest ? "))

    
    if interest == "simple":#simple is a string therefore its in quotes
                simple = investment_deposite*(1 + (investment_rate/100)*investment_years)#calculation for simple interest
                print(simple)#to print the answer of the users simple intrests inputs

    
    
    
    if interest == "compound":
        compound = investment_deposite*math.pow((1+(investment_rate/100)),investment_years)#calculation for compound interest
        print(compound)

elif investments_bonds == "bonds":
    bond_value = float(input("Enter the present value of your house: "))
    bond_rate = float(input("What is your intrest rate ? :"))
    bond_months = float(input("In how any months do you plan on repaying the bond? :"))

    bond_rated_i = (bond_rate)/(12)

    repayment = (bond_rated_i*bond_value)/ (1 - (1 + bond_rated_i))**(-(bond_months))
    print(repayment)
                    


    
