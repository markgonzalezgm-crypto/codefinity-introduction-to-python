# Initial conditions
product = 'Non-Perishable'
stock = 70
daysDelivered = 3

# Determine the handling of products based on type and condition
if product == 'Perishable':
    if daysDelivered >= 4:
        print("Not fresh - Initiate discount")
    else:
        print("Product is fresh")
elif product == 'Non-Perishable':
    if stock > 100:
        print("Consider discount")
    else:
        print("No discount needed")
else:
    print("The product is not specified")
