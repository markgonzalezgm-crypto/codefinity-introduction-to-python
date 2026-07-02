# Initial conditions
totalCost = 150

# Applying discounts based on purchase amount
if totalCost >= 200:
    print("20% discount applied")
elif totalCost >= 100:
    print("10% discount applied")
else:
    print("No discount for purchases under $100")
