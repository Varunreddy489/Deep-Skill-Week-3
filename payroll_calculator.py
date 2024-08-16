hours_worked = 40
hourly_rate = 15

def calculate_pay(hours, rate):
    return hours * rate

total_pay = calculate_pay(hours_worked, hourly_rate)

print(f"The total pay for the employee is: ${total_pay:.2f}")
