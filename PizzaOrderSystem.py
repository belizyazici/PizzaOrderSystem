import csv
import datetime

# Menu.txt file is created and content is written in it
menu = open("Menu.txt", "w")
menu.write('* Please Choose a Pizza Base: \n1: Classic \n2: Margherita \n3: Turkish Pizza \n4: Plain Pizza'
           ' \n* and sauce of your choice: \n5: Olives \n6: Mushrooms \n7: Goat Cheese \n8: Meat '
           '\n9: Onions \n10: Corn \n* Thank you!')

menu.close()


# superclass Pizza is created with the cost and description arguments
class Pizza:
    # initializing method and using self to create object that takes description and cost as arguments
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# subclass Classic is created for ordering classic pizza and see their descriptions
# and info of the cost
class Classic(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Classic Pizza is garnished with tomatoes, basil and mozzarella cheese.", 50)


# subclass Margherita is created for ordering margherita pizza and see their descriptions
# and info of the cost
class Margherita(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pizza Margherita,typically made with tomatoes, mozzarella cheese," 
              "garlic, fresh basil, and extra-virgin olive oil.", 60)


# subclass TurkPizza is created for ordering Turk pizza and see their descriptions
# and info of the cost
class TurkPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Turk Pizza - perfectly thin, crispier pizza (or flatbread), topped with a spiced minced meat mixture", 40)


# subclass PlainPizza is created for ordering plain pizza and see their descriptions
# and info of the cost
class PlainPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Plain pizza is simply another way to refer to the standard issue pie without additional toppings."
              " If you want a pizza without cheese, you would order sauce only, no cheese.", 30)


# superclass Decorator is created
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        super().__init__(description, cost)
        self.component = component

    # This function returns the total cost
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    # This function returns the recent description of order
    def get_description(self):
        return self.component.get_description() + ' and ' + Pizza.get_description(self)


class Olives(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component, "Olives", 4)


class Mushrooms(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component, "Mushrooms", 2)


class GoatCheese(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component, "Goat Cheese", 5)


class Meat(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component, "Meat", 10)


class Onions(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component, "Onions", 1)


class Corn(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component, "Corn", 3)


def main():
    print("************** Welcome to the Pizza Ordering System **************")

    with open("Menu.txt") as menu1:
        for i in menu1:
            print(i)

        pizza_dict = {1: Classic(),
                      2: Margherita(),
                      3: TurkPizza(),
                      4: PlainPizza()}

        p_choice = input("Which pizza you would like to order?(1 to 4): ")
        while p_choice not in ["1", "2", "3", "4"]:
            choice = input("Please try again: ")

        p_order = pizza_dict[int(p_choice)]

        sauce_dict = {5: Olives(p_order),
                      6: Mushrooms(p_order),
                      7: GoatCheese(p_order),
                      8: Meat(p_order),
                      9: Onions(p_order),
                      10: Corn(p_order)}

        s_choice = input("Which sauce you would like on your pizza?(5 to 10): ")
        while s_choice not in ["5", "6", "7", "8", "9", "10"]:
            s_choice = input("Please try again:")

        last_order = sauce_dict[int(s_choice)]

        print("Order description: " + last_order.get_description() + "\nTotal cost: " + str(last_order.get_cost()) + "$")

        print("**************** ORDER INFO ******************")
        name = input("Enter your name: ")
        id_number = input("Enter your ID number: ")
        card_no = input("Enter your Card No: ")
        card_password = input("Enter your password: ")
        order_date = datetime.datetime.now()

        field_names = ['Name', 'ID Number', 'Credit Card Info', 'Credit Card Password', 'Order Description', 'Order Date']

        # data rows of csv file
        rows = ([name, id_number, card_no, card_password, last_order.get_description(), last_order.get_cost(),
                 order_date])

        file_name = "Orders_Database.csv"

        with open(file_name, 'a') as order_data:
        # csv writer object is created, delimiter is used to specify the boundary between data
            order_data = csv.writer(order_data, delimiter=',', lineterminator='\n')
            order_data.writerow(rows)

        print("Name: " + name + "\nID Number: " + id_number + "\nCard No: " + card_no + "\nCard Password: "
              + card_password + "\nOrder Date: " + str(order_date))


main()
print("Your order is completed successfully, bon appetit!")