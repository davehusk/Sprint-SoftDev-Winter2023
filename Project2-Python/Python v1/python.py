import os
import operator
from datetime import datetime
from prettytable import PrettyTable
from tabulate import tabulate

# Change the working directory to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")
os.chdir(data_dir)

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return False

def read_defaults(filename="Defaults.dat"):
    with open(filename, "r") as file:
        lines = file.readlines()
        # Assume each line contains "key,value" and convert to dictionary
        defaults = dict(line.strip().split(',') for line in lines)
    return defaults

def write_defaults(defaults, filename="Defaults.dat"):
    with open(filename, "w") as file:
        for key, value in defaults.items():
            file.write(f"{key},{value}\n")

def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_valid_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_first_of_month():
    today = datetime.date.today()
    return today.day == 1

def charge_monthly_stand_fees():
    if is_first_of_month():
        if not os.path.exists('Employees.dat'):
            print("Employees file not found.")
            return

        with open('Employees.dat', 'r') as file:
            employees = file.readlines()

        for employee in employees:
            data = employee.strip().split(',')
            if data[8].lower() == 'true':  # Checking if the employee owns a car
                charge_fee_for_employee(data[0])

def charge_fee_for_employee(driver_number):
    fee_amount = 175.00  # Assuming a fixed fee amount
    hst_rate = 0.15  # Assuming HST rate of 15%
    hst = fee_amount * hst_rate
    total = fee_amount + hst

    next_transaction_number = get_next_transaction_number()
    today = datetime.date.today().strftime('%Y-%m-%d')
    with open('Revenues.dat', 'a') as file:
        file.write(f"{next_transaction_number},{today},Monthly Stand Fees,{driver_number},{fee_amount:.2f},{hst:.2f},{total:.2f}\n")

    update_next_transaction_number(next_transaction_number + 1)

    update_employee_balance_for_stand_fees(driver_number, total)

def get_next_transaction_number():
    # Read the current next transaction number from a file or database
    try:
        with open('NextTransactionNumber.dat', 'r') as file:
            next_transaction_number = int(file.read())
    except FileNotFoundError:
        # If the file doesn't exist, start with 1 as the next transaction number
        next_transaction_number = 1

    return next_transaction_number

def update_next_transaction_number(new_number):
    # Write the updated next transaction number to a file or database
    with open('NextTransactionNumber.dat', 'w') as file:
        file.write(str(new_number))

def update_employee_balance_for_stand_fees():
    defaults = read_defaults()
    monthly_stand_fee = float(defaults['Monthly stand fee'])

    # Read the Employees Table
    with open('Employees.dat', 'r') as file:
        employees = [line.strip().split(',') for line in file]

    if has_already_updated_this_month():
        print("Balances have already been updated for this month.")
        return

    for index, employee in enumerate(employees):
        try:
            if len(employee) != 10:
                print(f"Error: Invalid number of fields (expected 10, got {len(employee)}) in line {index + 1}: {employee}")
                continue

            driver_number, name, address, phone_number, license_number, expiry_date, insurance_company, policy_number, owns_car, balance_due = employee
            if owns_car.lower() == 'true':
                balance_due = float(balance_due)
                balance_due += monthly_stand_fee
                employee[-1] = str(balance_due)

        except Exception as e:
            print(f"Error processing line {index + 1}: {employee}, Error: {e}")
            continue

    # Write the updated employee data back to the Employees Table
    with open('Employees.dat', 'w') as file:
        for employee in employees:
            file.write(','.join(employee) + '\n')
    record_update_done_for_this_month()
    print("Employee balances updated for stand fees.")


def record_update_done_for_this_month():
    current_month = datetime.now().strftime("%Y-%m")
    with open('last_update.dat', 'w') as file:
        file.write(current_month)

def has_already_updated_this_month():
    try:
        with open('last_update.dat', 'r') as file:
            last_update = file.read().strip()
        current_month = datetime.now().strftime("%Y-%m")
        return last_update == current_month
    except FileNotFoundError:
        return False

def main_menu():
    while True:
        print("""
        HAB Taxi Services
        Company Services System

        1. Enter a New Employee (driver).
        2. Enter Company Revenues.
        3. Enter Company Expenses.
        4. Track Car Rentals.
        5. Record Employee Payment.
        6. Print Company Profit Listing.
        7. Print Driver Financial Listing.
        8. Print Company Financial Listing.
        9. Update Employee Balances for Stand Fees.
        10. Quit Program.
        """)
        choice = input("Enter choice (1-10): ")
        if choice == '1':
            enter_new_employee()
        elif choice == '2':
            enter_company_revenues()
        elif choice == '3':
            enter_company_expenses()
        elif choice == '4':
            record_rental()
        elif choice == '5':
            record_payment()
        elif choice == '6':
            print_company_profit_listing()
        elif choice == '7':
            print_driver_financial_listing()
        elif choice == '8':
            print_company_financial_listing()
        elif choice == '9':
            update_employee_balance_for_stand_fees()
        elif choice == '10':
            break
        else:
            print("Invalid choice, please try again.")

def enter_new_employee():
    defaults = read_defaults()
    next_driver_number = int(defaults['Next driver number'])
    print("Enter New Employee Details")
    name = input("Name: ")
    address = input("Address: ")
    phone_number = input("Phone Number: ")
    license_number = input("License Number: ")
    license_expiry = input("License Expiry Date (YYYY-MM-DD): ")
    while not validate_date(license_expiry):
        license_expiry = input("License Expiry Date (YYYY-MM-DD): ")
    insurance_company = input("Insurance Company: ")
    policy_number = input("Policy Number: ")
    owns_car = input("Owns Car? (True/False): ").lower()
    if owns_car not in ('true', 'false'):
        print("Invalid input for 'Owns Car'. Please enter 'True' or 'False'.")
        return
    balance_due = 0  # Initial balance due for new employee

    # Write the new employee details to a file
    with open('Employees.dat', 'a') as file:
        file.write(f"{next_driver_number},{name},{address},{phone_number},{license_number},{license_expiry},{insurance_company},{policy_number},{owns_car},{balance_due}\n")

    # Update the next driver number
    defaults['Next driver number'] = str(next_driver_number + 1)
    write_defaults(defaults)
    print("Employee added successfully.")

def enter_company_revenues():
    defaults = read_defaults()
    next_transaction_number = int(defaults['Next transaction number'])
    print("Enter Company Revenues")
    date = input("Date (YYYY-MM-DD): ")
    while not validate_date(date):
        date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")
    driver_number = input("Driver Number: ")
    amount = input("Amount: ")
    if not is_valid_float(amount):
        print("Invalid input for 'Amount'. Please enter a valid number.")
        return
    amount = float(amount)
    hst_rate = float(defaults['HST rate'])
    hst = amount * hst_rate / 100
    total = amount + hst

    # Write the revenue details to the Revenues file
    with open('Revenues.dat', 'a') as file:
        file.write(f"{next_transaction_number},{date},{description},{driver_number},{amount:.2f},{hst:.2f},{total:.2f}\n")

    # Update the next transaction number
    defaults['Next transaction number'] = str(next_transaction_number + 1)
    write_defaults(defaults)
    print("Revenue entry added successfully.")

def enter_company_expenses():
    defaults = read_defaults()
    next_invoice_number = int(defaults['Next invoice number'])
    print("Enter Company Expenses")
    invoice_date = input("Invoice Date (YYYY-MM-DD): ")
    while not validate_date(invoice_date):
        invoice_date = input("Invoice Date (YYYY-MM-DD): ")
    driver_number = input("Driver Number: ")

    # Collect multiple expense items
    expenses = []
    while True:
        item_number = input("Item Number: ")
        description = input("Description: ")
        cost = input("Cost: ")
        if not is_valid_float(cost):
            print("Invalid input for 'Cost'. Please enter a valid number.")
            continue
        cost = float(cost)
        quantity = input("Quantity: ")
        if not is_valid_int(quantity):
            print("Invalid input for 'Quantity'. Please enter a valid integer.")
            continue
        quantity = int(quantity)
        item_total = cost * quantity
        expenses.append((item_number, description, cost, quantity, item_total))
        another_item = input("Enter another item? (Yes/No): ")
        if another_item.lower() != 'yes':
            break

    # Calculate Subtotal, HST, and Total
    subtotal = sum(item[4] for item in expenses)
    hst_rate = float(defaults['HST rate'])
    hst = subtotal * hst_rate / 100
    total = subtotal + hst

    # Write the expense details to the Expenses file
    with open('Expenses.dat', 'a') as file:
        for item_number, description, cost, quantity, item_total in expenses:
            file.write(f"{next_invoice_number},{invoice_date},{driver_number},{item_number},{description},{cost:.2f},{quantity},{item_total:.2f}\n")

    # Update the next invoice number and write defaults
    defaults['Next invoice number'] = str(next_invoice_number + 1)
    write_defaults(defaults)
    print("Expense entry added successfully.")

def print_company_profit_listing():
    # Calculate the profit by subtracting expenses from revenues
    total_revenue = sum(float(line.split(',')[4]) for line in open('Revenues.dat') if not line.startswith("Transaction"))
    total_expenses = sum(float(line.split(',')[5]) for line in open('Expenses.dat') if not line.startswith("Invoice"))

    profit = total_revenue - total_expenses

    # Create a PrettyTable to display the profit information
    table = PrettyTable()
    table.field_names = ["Category", "Amount"]
    table.add_row(["Total Revenues", f"${total_revenue:.2f}"])
    table.add_row(["Total Expenses", f"${total_expenses:.2f}"])
    table.add_row(["Profit", f"${profit:.2f}"])

    print(table)

def print_driver_financial_listing():
    driver_name = input("Enter driver's name to print financial listing (or press Enter to list all drivers): ")

    drivers = []

    with open('Employees.dat', 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            driver_data = line.strip().split(',')
            if not driver_name or driver_data[1] == driver_name:
                driver_number = driver_data[0]

                # Initialize revenues and expenses to 0
                revenues = 0
                expenses = 0

                # Read the Revenues and Expenses files while skipping the header lines
                with open('Revenues.dat', 'r') as rev_file:
                    next(rev_file)  # Skip the header line
                    for rev_line in rev_file:
                        rev_fields = rev_line.strip().split(',')
                        if rev_fields[3] == driver_number:
                            revenues += float(rev_fields[4])

                with open('Expenses.dat', 'r') as exp_file:
                    next(exp_file)  # Skip the header line
                    for exp_line in exp_file:
                        exp_fields = exp_line.strip().split(',')
                        if exp_fields[2] == driver_number:
                            expenses += float(exp_fields[5])

                net_income = revenues - expenses
                drivers.append((driver_number, driver_data[1], revenues, expenses, net_income))

    # Define a dictionary to map sorting options to sorting functions
    sorting_options = {
        1: ('Driver Number', operator.itemgetter(0)),
        2: ('Driver Name', operator.itemgetter(1)),
        3: ('Revenues', operator.itemgetter(2)),
        4: ('Expenses', operator.itemgetter(3)),
        5: ('Net Income', operator.itemgetter(4)),
    }

    # Ask the user for sorting options
    print("Sorting Options:")
    for option, (desc, _) in sorting_options.items():
        print(f"{option}. Sort by {desc}")

    sort_choice = input("Enter sorting option (or press Enter to list drivers): ")

    if sort_choice == '':
        # If the user just presses Enter, list all drivers
        sorted_drivers = drivers
    else:
        try:
            sort_choice = int(sort_choice)
            if sort_choice in sorting_options:
                sort_key = sorting_options[sort_choice][1]
                reverse_sort = input("Sort in descending order? (y/n): ").lower() == 'y'

                # Sort the drivers list based on the chosen criteria
                sorted_drivers = sorted(drivers, key=sort_key, reverse=reverse_sort)
            else:
                print("Invalid sorting option.")
                sorted_drivers = []  # Empty list to avoid printing results if sorting option is invalid
        except ValueError:
            print("Invalid input. Please enter a valid sorting option or press Enter to list drivers.")
            sorted_drivers = []  # Empty list to avoid printing results if input is invalid

    if sorted_drivers:
        # Define the table headers
        header = ['Driver Number', 'Driver Name', 'Revenues', 'Expenses', 'Net Income']

        # Print the sorted data in a table format
        print(tabulate(sorted_drivers, headers=header, tablefmt="pretty"))

def print_company_financial_listing():
    print("Company Financial Listing")

    # Initialize revenues and expenses to 0
    total_revenues = 0
    total_expenses = 0

    # Read the Revenues and Expenses files while skipping the header lines
    with open('Revenues.dat', 'r') as rev_file:
        next(rev_file)  # Skip the header line
        for rev_line in rev_file:
            rev_fields = rev_line.strip().split(',')
            total_revenues += float(rev_fields[4])

    with open('Expenses.dat', 'r') as exp_file:
        next(exp_file)  # Skip the header line
        for exp_line in exp_file:
            exp_fields = exp_line.strip().split(',')
            total_expenses += float(exp_fields[5])

    # Calculate the company's net income
    net_income = total_revenues - total_expenses

    # Create a PrettyTable to display the financial summary
    table = PrettyTable()
    table.field_names = ["Category", "Amount"]
    table.add_row(["Total Revenues", f"${total_revenues:.2f}"])
    table.add_row(["Total Expenses", f"${total_expenses:.2f}"])
    table.add_row(["Net Income", f"${net_income:.2f}"])

    # Print the PrettyTable
    print(table)

def record_rental(driver_number, start_date, car_number, duration, number_of_days):
    defaults = read_defaults()
    daily_rental_fee = float(defaults['Daily rental fee'])
    weekly_rental_fee = float(defaults['Weekly rental fee'])
    hst_rate = float(defaults['HST rate'])

    # Calculate the rental cost based on the duration and apply HST
    if duration == 'week':
        rental_cost = weekly_rental_fee
    else:
        rental_cost = daily_rental_fee * number_of_days

    hst = rental_cost * hst_rate / 100
    total_cost = rental_cost + hst

    # Update the Rentals Table
    with open('Rentals.dat', 'a') as file:
        file.write(f"{driver_number},{start_date},{car_number},{duration},{number_of_days},{rental_cost:.2f},{hst:.2f},{total_cost:.2f}\n")

    # Update the Revenues Table
    next_transaction_number = int(defaults['Next transaction number'])
    with open('Revenues.dat', 'a') as file:
        file.write(f"{next_transaction_number},{start_date},Rental,{driver_number},{total_cost:.2f},{hst:.2f},{total_cost:.2f}\n")

    # Update the Employee's Balance Due
    with open('Employees.dat', 'r') as file:
        employees = [line.strip().split(',') for line in file]

    for i, employee in enumerate(employees):
        if employee[0] == driver_number:
            balance_due = float(employee[-1])
            balance_due += total_cost
            employees[i][-1] = str(balance_due)

    # Write the updated employee data back to the Employees Table
    with open('Employees.dat', 'w') as file:
        for employee in employees:
            file.write(','.join(employee) + '\n')

def record_payment(driver_number, amount, payment_reason, payment_method):
    # Record the payment details to the Payments table
    with open('Payments.dat', 'a') as file:
        file.write(f"{driver_number},{datetime.now().strftime('%Y-%m-%d')},{amount:.2f},{payment_reason},{payment_method}\n")

    # Update the Employee's Balance Due
    with open('Employees.dat', 'r') as file:
        employees = [line.strip().split(',') for line in file]

    for i, employee in enumerate(employees):
        if employee[0] == driver_number:
            balance_due = float(employee[-1])
            balance_due -= amount
            employees[i][-1] = str(balance_due)

    # Write the updated employee data back to the Employees Table
    with open('Employees.dat', 'w') as file:
        for employee in employees:
            file.write(','.join(employee) + '\n')

if __name__ == "__main__":
    main_menu()
