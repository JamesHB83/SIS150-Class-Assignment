# Name: James
# Date: October 11, 2026
# Purpose: Create an online shopping cart program matching all zyBooks specifications

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        # Print all itemized metrics first
        for item in self.cart_items:
            item.print_item_cost()
            
        print() # Line separator exactly matching Test 10 and 12 expectations
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print(f"Total: ${self.get_cost_of_cart()}")


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("o - Output shopping cart")
    print("q - Quit")
    print()
def execute_menu(menuOp, theCart):
    if menuOp == 'a':
        print("ADD ITEM TO CART")
        name = input("Enter the item name:\n")
        price = int(input("Enter the item price:\n"))
        quantity = int(input("Enter the item quantity:\n"))
        new_item = ItemToPurchase(name, price, quantity)
        theCart.add_item(new_item)
        
    elif menuOp == 'r':
        print("REMOVE ITEM FROM CART")
        name = input("Enter name of item to remove:\n")
        theCart.remove_item(name)
        
    elif menuOp == 'c':
        print("CHANGE ITEM QUANTITY")
        name = input("Enter the item name:\n")
        quantity = int(input("Enter the new quantity:\n"))
        mod_item = ItemToPurchase(item_name=name, item_quantity=quantity)
        theCart.modify_item(mod_item)
        
    elif menuOp == 'o':
        print("OUTPUT SHOPPING CART")
        theCart.print_total()


if __name__ == "__main__":
    cust_name = input("Enter customer's name:\n")
    day_date = input("Enter today's date:\n")
    print()
    
    print(f"Customer name: {cust_name}")
    print(f"Today's date: {day_date}")
    print()
    
    my_cart = ShoppingCart(cust_name, day_date)
    print_menu()
    menu_choice = ' '
    while menu_choice != 'q':
        menu_choice = input("Choose an option:\n")
        if menu_choice in ['a', 'r', 'c', 'o']:
            execute_menu(menu_choice, my_cart)
            print_menu()