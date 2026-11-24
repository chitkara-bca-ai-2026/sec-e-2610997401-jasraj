# Lab 04 - Data Conversion Utility

print("========================================")
print("         DATA CONVERSION UTILITY")
print("========================================")

# 1. Take product name as a string input
product_name = input("Enter Product Name : ")

# 2. Take price as input and convert it to float
price = float(input("Enter Price        : "))

# 3. Take quantity as input and convert it to int
quantity = int(input("Enter Quantity     : "))

# 4. Calculate the total price (price * quantity)
total_price = price * quantity

# 5. Convert the final amount into a string for displaying an invoice
amount_str = str(total_price)

# 6. Display the type of each variable using type() to show type casting
print("----------------------------------------")
print("          TYPE CASTING SUMMARY")
print("----------------------------------------")
print("Variable       Value         Python Type")
print("----------------------------------------")
print(f"product_name   {product_name:<13} {type(product_name)}")
print(f"price          {price:<13} {type(price)}")
print(f"quantity       {quantity:<13} {type(quantity)}")
print(f"total_price    {total_price:<13} {type(total_price)}")
print(f"amount_str     {amount_str:<13} {type(amount_str)}")
print("----------------------------------------")

# 7. Display the invoice with product name, price, quantity, and total
print("                 TAX INVOICE")
print("----------------------------------------")
print(f"Product Name   : {product_name}")
print(f"Price per Unit : Rs. {price}")
print(f"Quantity       : {quantity}")
print("----------------------------------------")
print(f"Invoice Total  : Rs. {amount_str}")
print("========================================")