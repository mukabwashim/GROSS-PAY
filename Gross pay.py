def calculate_gross_pay(hours, rate):
    gross_pay = hours * rate
    return gross_pay

try:
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate per hour: "))

  
    if hours >= 0 and rate >= 0:
        gross_pay = calculate_gross_pay(hours, rate)
        print(f"Gross pay: ${gross_pay:.2f}")
    else:
        print("Hours and rate must be non-negative numbers.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
