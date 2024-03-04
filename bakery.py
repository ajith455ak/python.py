num_loaves=eval(input("enter the number of loves being purchased:"))
price_per_bread=180
discount=0.60
regular_price = num_loaves * price_per_bread
discount_amount = regular_price * discount
total_price = regular_price - discount_amount
print(f"Regular Price: {regular_price:.2f} rupees")
print(f"Discount: {discount_amount:.2f} rupees")
print(f"Total Price: {total_price:.2f} rupees")
