class VendingMachine:
    def __init__(self):
        self.drinks = {
            'D1': {'name': 'Cola', 'price': 5.50},
            'D2': {'name': 'Soda', 'price': 4.50},
            'D3': {'name': 'Water', 'price': 3.50},
            'D4': {'name': 'Fanta', 'price': 4.50},
            'D5': {'name': 'Juice', 'price': 2.50},
            'D6': {'name': 'Energy drink', 'price': 6.50}
        }

        self.snacks = {
            'S1': {'name': 'Chips', 'price': 4.00},
            'S2': {'name': 'Candy', 'price': 3.00},
            'S3': {'name': 'Popcorn', 'price': 5.00},
            'S4': {'name': 'Samosa', 'price': 2.00},
            'S5': {'name': 'Jelly', 'price': 3.00},
            'S6': {'name': 'Icecream', 'price': 4.00}
        }

        self.balance = 0.0

    def display_menu(self, menu):
        print("Menu:")
        for code, item in menu.items():
            print(f"{code}: {item['name']} - {item['price']:.2f} AED")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted {amount:.2f} AED. Total balance: {self.balance:.2f} AED")

    def select_item(self, menu, code):
        if code in menu:
            item = menu[code]
            price = item['price']
            if self.balance >= price:
                self.balance -= price
                print(f"Dispensing {item['name']}. Enjoy!")
                print(f"Remaining balance: {self.balance:.2f} AED")
            else:
                print("Insufficient balance. Please insert more money.")
        else:
            print("Invalid code. Please select a valid item code.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: {self.balance:.2f} AED")
            self.balance = 0
        else:
            print("No balance to return.")

    def display_thankyou_message(self):
        print("Thank you for using the Awesome Vending Machine!")

# Main program
if __name__ == "__main__":
    vm = VendingMachine()

    # Allow user to add money at the start
    while True:
        try:
            initial_amount = float(input("Please insert money to start (in AED): "))
            if initial_amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid amount.")

    vm.insert_money(initial_amount)

    vm.display_menu(vm.drinks)
    vm.display_menu(vm.snacks)

    while True:
        choice = input("\nEnter the item code you want to purchase (or 'exit' to finish): ").upper()

        if choice == 'EXIT':
            break

        if choice in vm.drinks or choice in vm.snacks:
            if vm.balance == 0:
                print("Please insert money first.")
            else:
                if choice in vm.drinks:
                    vm.select_item(vm.drinks, choice)
                elif choice in vm.snacks:
                    vm.select_item(vm.snacks, choice)
        else:
            print("Invalid code. Please select a valid item code.")

    vm.return_change()
    vm.display_thankyou_message()
