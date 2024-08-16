order_amount = 150

def apply_discount(order_amount):
    if order_amount > 100:
        discount = 0.10  # 10% discount
        final_price = order_amount * (1 - discount)
    else:
        final_price = order_amount
    return final_price

final_price = apply_discount(order_amount)

print(f"The final price after applying the discount is: ${final_price:.2f}")
