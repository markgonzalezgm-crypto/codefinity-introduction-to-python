# Sample data received from a cashier or inventory management system
product_name = "Almond Milk"
product_price = "3.49"
product_quantity = 30

# Checking if the data types are as expected
correct_name_type = type(product_name) == str
correct_price_type = type(product_price) == float  # Intentional error for demonstration
correct_quantity_type = type(product_quantity) == int

# Print the results to verify data types
print("Is product_name a string?", correct_name_type)
print("Is product_price a float?", correct_price_type)  # Expected: False, actual data type is a string
print("Is product_quantity an integer?", correct_quantity_type)

print("Data type check complete. Please review and correct any 'False' outcomes for data corrections.")
