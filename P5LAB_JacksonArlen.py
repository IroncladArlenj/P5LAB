import random

def main():
    

 def disperse_change(change):
    dollars = change // 1
    change %= 1
    quarters = change // 0.25
    change %= 0.25
    dimes = change // 0.10
    change %= 0.10
    nickels = change // 0.05
    change %= 0.05
    pennies = round(change / 0.01)

    print("Change Dispensed:")
    print(int(dollars),"Dollars")
    print(int(quarters),"Quarters")
    print(int(dimes),"Dimes")
    print(int(nickels),"Nickels")
    print(int(pennies),"Pennies")

def main():
    owed = round(random.uniform(0.01, 100.00), 2)
    print("You owe: ", owed)
    cash = float(input("How much cash will you put in self checkout: "))

    change = cash - owed
    print(change)
    if change > 0:  # Ensure change is positive
        change = round(change, 2)  # Round change to 2 decimal places
        print(change)
        change = int(round(change * 100))
        print(change)
        disperse_change(change / 100)
        print("Change is: ", round(change / 100, 2))  # Print change rounded to 2 decimal places
    else:
        print("No change dispensed.")

if __name__ == "__main__":

     main()

    

# use an if statemnet 
# chnge - owed
