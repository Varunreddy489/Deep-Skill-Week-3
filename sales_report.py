sales = [200, 600, 150, 800, 300]

def generate_report(sales):
    total_sales = 0
    for sale in sales:
        if sale > 500:
            print(f"High Sale: ${sale}")
        else:
            print(f"Sale: ${sale}")
        total_sales += sale
    return total_sales

total_sales = generate_report(sales)
print(f"Total sales for the month: ${total_sales}")
