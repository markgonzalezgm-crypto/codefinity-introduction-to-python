product = "apples"
quantity = 12
price_per_item = 0.75

total_cost = quantity * price_per_item

# Using an f-string to include variables and an expression in a single message
message = f"You bought {quantity} {product} at ${price_per_item} each. Total cost: ${total_cost:.2f}."

print(message)

# Embedding an expression directly in the f-string
print(f"Half of your apples would be {quantity // 2}.")
