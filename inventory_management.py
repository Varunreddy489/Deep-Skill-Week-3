inventory = [('item1', 10), ('item2', 0), ('item3', 5)]

def check_inventory(inventory):
    for item, quantity in inventory:
        if quantity == 0:
            print(f"Alert: {item} is out of stock!")

check_inventory(inventory)
