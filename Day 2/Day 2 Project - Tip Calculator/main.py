print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
perc = float(input("What percentage tip would you like to give? (10, 12, or 15?)\n"))*0.01
peeps = int(input("How many people are going to split the bill?\n"))

each = round((bill+(bill*perc))/peeps, 2)

print(f"Each person should pay: {each}")