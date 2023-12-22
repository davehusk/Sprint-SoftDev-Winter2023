
import csv
from datetime import datetime
from prettytable import PrettyTable
import os

class HABTaxiServiceSystem:
    def __init__(self):
        # Initialization with loading data from files
        # Set the directory where the script is located as the working directory
        self.script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        self.employees = self.load_data("Employees.dat")
        self.defaults = self.load_data("Defaults.dat")
        self.revenues = self.load_data("Revenues.dat")
        self.expenses = self.load_data("Expenses.dat")
        self.rentals = self.load_data("Rentals.dat")
        self.payments = self.load_data("Payments.dat")
        self.last_update = self.load_data("last_update.dat")
        self.main_menu_options = {
            "1": self.enter_new_employee,
            "2": self.enter_company_revenues,
            "3": self.enter_company_expenses,
            "4": self.track_car_rentals,
            "5": self.record_employee_payment,
            "6": self.print_company_profit_listing,
            "7": self.print_driver_financial_listing,
            "8": self.additional_report,
            "9": self.quit_program
        }

    def load_defaults(self, filename):
        """ Load default values from a CSV file. """
        full_path = os.path.join(self.script_dir, filename)
        defaults = {}
        try:
            with open(full_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 2:  # Expecting two columns: key and value
                        defaults[row[0]] = row[1]
        except FileNotFoundError:
            print(f"Defaults file {filename} not found in the directory {self.script_dir}.")
        except Exception as e:
            print(f"An error occurred while loading {filename}: {e}")
        return defaults

    def load_data(self, filename):
        # Method to load data from a file using the current script directory
        full_path = os.path.join(self.script_dir, filename)
        data = []
        try:
            with open(full_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"File {filename} not found in the directory {self.script_dir}.")
        except Exception as e:
            print(f"An error occurred while loading {filename}: {e}")
        return data

    def enter_new_employee(self):
        """ Enter a new employee (driver) into the system """
        print("\n--- Enter New Employee ---")
        expiry_date = input("Enter driver license expiry date (YYYY-MM-DD): ") or '2024-12-21'
        if not self.validate_date(expiry_date):
            print("\nInvalid date format. Please try again.\n")
            return
        balance_due = input("Enter initial balance due: ") or '0.00'
        if not balance_due.replace('.', '', 1).isdigit():
            print("\nInvalid amount. Please enter a numeric value.\n")
            return
        driver_no = input("Enter driver number: ") or '1234'
        name = input("Enter name: ") or 'John Doe'
        address = input("Enter address: ") or '123 Main St'
        city = input("Enter city: ") or 'St Johns'
        province = input("Enter province: ") or 'NL'
        postal_code = input("Enter postal code: ") or 'A1A 1A1'
        phone_number = input("Enter phone number: ") or '123-456-7890'
        driver_license_no = input("Enter driver license number: ") or '123456789'
        expiry_date = input("Enter driver license expiry date (YYYY-MM-DD): ") or '2023-12-21'
        insurance_policy_company = input("Enter insurance policy company: ") or 'Insurance Company'
        insurance_number = input("Enter insurance number: ") or '123456789'
        own_vehicle = input("Does the driver own a vehicle? (yes/no): ") or 'yes'
        balance_due = input("Enter initial balance due: ") or '0.00'

        # Validate entered data, for now, we'll assume the user enters everything correctly
        # In a real system, you would add error checking and validation here

        # Add the new employee to the employees list
        new_employee = {
            "Driver No": driver_no,
            "Name": name,
            "Address": address,
            "City": city,
            "Province": province,
            "Postal Code": postal_code,
            "Phone Number": phone_number,
            "Driver License No": driver_license_no,
            "Expiry Date": expiry_date,
            "Insurance Policy Company": insurance_policy_company,
            "Insurance Number": insurance_number,
            "Own Vehicle": own_vehicle.lower() == "yes",
            "Balance Due": balance_due
        }
        self.employees.append(new_employee)

    def calculate_hst(self, amount):
        """Calculate HST based on a given amount."""
        return amount * self.HST_RATE

    def validate_date(self, date_text):
        # Existing date validation method with added comments
        """ Validate date format YYYY-MM-DD """
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def update_data_file(self, data, filename):
        """ Write the data back to a CSV file. """
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            print(f"\nData updated successfully in {filename}.\n")
        except Exception as e:
            print(f"\nAn error occurred while updating {filename}: {e}\n")

    def enter_company_revenues(self):
        """ Enter company revenues """
        print("\n--- Enter Company Revenues ---")
        transaction_id = input("Enter transaction ID: ") or '7114'
        transaction_date = input("Enter transaction date (YYYY-MM-DD): ") or '2021-01-01'
        description = input("Enter transaction description: ") or 'Transaction'
        amount = float(input("Enter transaction amount: ")) or 0.00
        hst = self.calculate_hst(amount)
        total = amount + hst
        new_revenue = {
            "Transaction ID": transaction_id,
            "Transaction Date": transaction_date,
            "Description": description,
            "Amount": amount,
            "HST": hst,
            "Total": total
        }
        self.revenues.append(new_revenue)
        self.update_data_file(self.revenues, "Revenues.dat")

    def enter_company_expenses(self):
        """ Enter company expenses """
        print("\n--- Enter Company Expenses ---")
        invoice_number = input("Enter invoice number: ") or '4434'
        expense_date = input("Enter expense date (YYYY-MM-DD): ") or '2021-01-01'
        item_number = input("Enter item number: ") or '3234'
        description = input("Enter item description: ") or 'Item'
        cost = input("Enter item cost: ") or '0.00'
        quantity = input("Enter quantity: ") or '1'
        subtotal = input("Enter subtotal: ") or '0.00'
        hst = input("Enter HST: ") or '0.00'
        total = input("Enter total cost: ") or '0.00'

        new_expense = {
            "Invoice Number": invoice_number,
            "Expense Date": expense_date,
            "Item Number": item_number,
            "Description": description,
            "Cost": cost,
            "Quantity": quantity,
            "Subtotal": subtotal,
            "HST": hst,
            "Total": total
        }
        self.expenses.append(new_expense)
        self.update_data_file(self.expenses, "Expenses.dat")

    def track_car_rentals(self):
        """ Track car rentals """
        print("\n--- Track Car Rentals ---")
        rental_id = input("Enter rental ID: ")
        driver_no = input("Enter driver number: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        car_no = input("Enter car number: ")
        rental_days = input("Enter number of rental days: ")
        rental_cost = input("Enter rental cost: ")
        hst = input("Enter HST: ")
        total = input("Enter total cost: ")

        new_rental = {
            "Rental ID": rental_id,
            "Driver No": driver_no,
            "Start Date": start_date,
            "End Date": end_date,
            "Car No": car_no,
            "Rental Days": rental_days,
            "Rental Cost": rental_cost,
            "HST": hst,
            "Total": total
        }
        self.rentals.append(new_rental)
        self.update_data_file(self.rentals, "Rentals.dat")

    def record_employee_payment(self):
        """ Record employee payment """
        print("\n--- Record Employee Payment ---")
        payment_id = input("Enter payment ID: ")
        driver_no = input("Enter driver number: ")
        payment_date = input("Enter payment date (YYYY-MM-DD): ")
        amount = input("Enter payment amount: ")
        reason = input("Enter payment reason: ")
        method = input("Enter payment method (Cash, Debit, Visa): ")

        new_payment = {
            "Payment ID": payment_id,
            "Driver No": driver_no,
            "Payment Date": payment_date,
            "Amount": amount,
            "Reason": reason,
            "Method": method
        }
        self.payments.append(new_payment)
        self.update_data_file(self.payments, "Payments.dat")

    def print_company_profit_listing(self):
        """ Print company profit listing """
        print("\n--- Company Profit Listing ---")
        profit_listing = ""
        # For the simplicity of this example, we'll just print the revenues and expenses
        # In a real scenario, we'd calculate profits by subtracting expenses from revenues
        profit_table = PrettyTable()
        profit_table.field_names = ["Transaction ID", "Date", "Description", "Amount", "HST", "Total Revenue"]
        for revenue in self.revenues:
            profit_table.add_row([revenue["Transaction ID"], revenue["Transaction Date"], revenue["Description"], revenue["Amount"], revenue["HST"], revenue["Total"]])

        print(profit_table)

        expense_table = PrettyTable()
        expense_table.field_names = ["Invoice Number", "Date", "Item No", "Description", "Cost", "HST", "Total Cost"]
        for expense in self.expenses:
            expense_table.add_row([expense["Invoice Number"], expense["Expense Date"], expense["Item Number"], expense["Description"], expense["Cost"], expense["HST"], expense["Total"]])

        print(expense_table)

    def print_driver_financial_listing(self):
        """ Print driver financial listing """
        print("\n--- Driver Financial Listing ---")
        driver_no = input("Enter driver number to print financial listing: ")
        # Filter out the payments and rentals for the given driver number
        driver_payments = [payment for payment in self.payments if payment["Driver No"] == driver_no]
        driver_rentals = [rental for rental in self.rentals if rental["Driver No"] == driver_no]

        payment_table = PrettyTable()
        payment_table.field_names = ["Payment ID", "Date", "Amount", "Reason", "Method"]
        for payment in driver_payments:
            payment_table.add_row([payment["Payment ID"], payment["Payment Date"], payment["Amount"], payment["Reason"], payment["Method"]])

        print(payment_table)

        rental_table = PrettyTable()
        rental_table.field_names = ["Rental ID", "Start Date", "End Date", "Car No", "Days", "Cost", "HST", "Total"]
        for rental in driver_rentals:
            rental_table.add_row([rental["Rental ID"], rental["Start Date"], rental["End Date"], rental["Car No"], rental["Rental Days"], rental["Rental Cost"], rental["HST"], rental["Total"]])

        print(rental_table)

    def additional_report(self):
        """ Generate and print an additional custom report """
        print("\n--- Additional Custom Report ---")

        # Grouping rentals by date
        rentals_by_date = {}
        for rental in self.rentals:
            rental_date = rental["Start Date"]
            if rental_date not in rentals_by_date:
                rentals_by_date[rental_date] = []
            rentals_by_date[rental_date].append(rental)

        # Grouping payments by date
        payments_by_date = {}
        for payment in self.payments:
            payment_date = payment["Payment Date"]
            if payment_date not in payments_by_date:
                payments_by_date[payment_date] = []
            payments_by_date[payment_date].append(payment)

        # Printing the summary report
        report_table = PrettyTable()
        report_table.field_names = ["Date", "Total Rentals", "Total Payments"]

        # Assuming the report is for the current month
        current_month = datetime.now().strftime("%Y-%m")
        for date in sorted(rentals_by_date.keys()):
            if current_month in date:
                total_rentals = sum(float(rental["Total"]) for rental in rentals_by_date[date])
                total_payments = sum(float(payment["Amount"]) for payment in payments_by_date.get(date, []))
                report_table.add_row([date, total_rentals, total_payments])

        print(report_table)

    def quit_program(self):
        """ Exit """
        # Method to quit the program
        print("\nExiting the program. Goodbye!\n")
        exit()

    def run(self):
        # Main loop for running the application
        while True:
            print("\nHAB Taxi Services Company Services System\n")
            for option in self.main_menu_options:
                print(f"{option}. {self.main_menu_options[option].__doc__}")  # Print the docstring of each method as a menu item description
            choice = input("Enter choice (1-9): ")
            if choice in self.main_menu_options:
                self.main_menu_options[choice]()
            else:
                print("Invalid choice, please try again.")

    def validate_date(self, date_text):
        # Existing date validation method with added comments
        """ Validate date format YYYY-MM-DD """
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    system = HABTaxiServiceSystem()
    system.run()
