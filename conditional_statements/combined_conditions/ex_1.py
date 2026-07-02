is_perishable = True
item_quantity = 110
perishable_highStockRisk = 100

# Combine two or more conditions
consider_discount = is_perishable and (item_quantity >= perishable_highStockRisk)

# Print the result
print("Is the item perishable and high in stock?", consider_discount)
