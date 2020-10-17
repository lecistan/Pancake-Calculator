eggsMin: int = 1
milkMin: int = 200 #milimeteres
flourMin: int = 100 #grams
print("What is your name?")
username = input()
print("Hello " + username)
print("How many eggs do you have?")
eggsAmount: int = input()
print("You have " + eggsAmount + " eggs")
print("How much milk do you have?")
milkAmount: int = input()
print("You have " + milkAmount + "ml of milk")
print("How much flour do you have?")
flourAmount: int = input()
print("You have " + flourAmount + "g of flour")
if int(eggsAmount) < int(eggsMin) or int(milkAmount) < int(milkMin) or int(flourAmount) < int(flourMin):
    print("You do not have enough materials to make a pancake :(.")
else:
    flourPortions: int = int(flourAmount) // int(flourMin)
    print("You have " + str(flourPortions) + " portions of flour")
    milkPortions: int = int(milkAmount) // int(milkMin)
    print("You have " + str(milkPortions) + " portions of milk")
    if int(eggsAmount) <= int(milkPortions) & int(milkPortions) <= int(flourPortions):
        smallest: int = int(eggsAmount)
    elif int(milkPortions) <= int(eggsAmount) & int(eggsAmount) <= int(flourPortions):
        smallest: int = int(milkPortions)
    else:
        smallest: int = int(flourPortions)
print("")
print("You can make " + str(smallest * 4) + " of pancakes")
print("")
print("You will need " + str(smallest * eggsMin) + " eggs")
print("You will need " + str(smallest * flourMin) + "g flour")
print("You will need " + str(smallest * milkMin) + "ml milk")
