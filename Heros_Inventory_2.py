# Hero's Inevntory 2.o
# Demonstrates tuples

# create a tuple with some items and display with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print("Your items:")
for item in inventory:
    print(item)
    
input("\nPress the enter key to continue.")

# get the length of a tuple
print("You have", len(inventory), "items in your possession.")

# test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

input("\nPress the enter key to continue.")
