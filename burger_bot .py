# Burger Bot
# Bugs - Phone Number allows letters
#      - Name allows numbers
import random
from random import randint


#List of random names

names=["Mark", "Pheobe", "Sally", "Michael", "Denise","Ellen", "Eric", "Moana", "Lewis","Lara"]
def welcome():
    '''
    Purpose: to genrate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
#List of burger names
burger_names = ['The Classic Cheese Burger - The Classic juciy beef patty, lettuce tomato, pickles, cheese on seasame bun',
                'BBQ Bacon Burger - Grilled beef patty, bacon, cheader cheese and BBQ sause, onions','Mushroom Swiss Burger - Sauteed mushrooms with melted swis cheese',
                'Veggie Burger - With avocado slices and cilantro-lime mayo', 'Double Trouble - Double Chiken patty, lettuce, tomato, mayo, pickle, fried egg', 
                'Hawaiian Teriyaki Burger - Grilled chicken/beef,pinaple glaze with lettuce and mayo','Chipotle Burger - Seasoned beef patty, pepper black cheese, bacon and chipotle sause',
                'Breakfast Burger - Beef/pork patty, fried egg, with melted cheese, tomato and bacon','Blue Cheese Greeny Burger - With caramilzed onions and Dijon musturd', 
               'Mediterranean Falafel Burger - Falafal patty, pita/bun, lettuce cucumber, red onions and tahini sause','Surf n Turf Burger - Beef patty, grilled shrimp, garlic aioli, and tomatoes ',
               'Gourmet Burger - Premium beef patty, argula, onions, and trffel aioli',]
#Lists of burger prices
burger_prices = [7.50, 7.50, 7.50, 7.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50,13.50, 13.50]
customer_details = {}

#list to store ordered burgers
order_list = []


#list to store burger prices
order_cost = []


# Customer details dictionary
customer_details = {}


# validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")




# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name form the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to my burger Shop ***")
    print("*** my name is ",name, "***")
    print("*** I will be here to help you order the right and perfect burger for you ***")

# Menu for Pickup and Delivery
def order_type():
    del_pick = ""
    print ("Is your order for Click and Collect or Delivery")
    print ("For Click and Collect please enter 1") 
    print ("For Delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and Collect")
                    del_pick = "Click and Collect"
                    Click_and_Collect_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    del_pick = "Delivery"
                    delivery_info()
                    break
            else:
                print("Number must be 1 or 2")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 or 2 ")
    return del_pick



# Pickup information - Name and Phone
def Click_and_Collect_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    #print(customer_details['name'])
    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print(customer_details['phone'])
    print(customer_details)
# Delivery information - Name, Address and Phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])
    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])
    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])
    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])
    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])
    print(customer_details)




# Item List
def list():
    number_burgers = 12
    for count in range (number_burgers):
        print("{} {} ${:.2f}"   .format(count+1,burger_names[count],burger_prices[count]))
# Choose total number of items - max 20

# Item(s) ordered - from item list - print each ordered item with cost
def order_burgers():
    # ask for total number of burgers for order
   
    num_burgers = 0
    while True:
        try:
            num_burgers = int(input("How many burgers do you want to order? "))
            if num_burgers >= 1:
                break
            else:
                print("Your order must between 1 or more")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter number ")
    # Choose burgers from the list
    for item in range(num_burgers):
        while num_burgers > 0:
            while True:
                try:
                    burgers_ordered = int(input("Please choose your burgers by entering the number from the list "))
                    if burgers_ordered >= 1 and burgers_ordered <= 12:
                        break
                    else: 
                        print("Your number must be between 1 and 12")
                except ValueError:
                        print ("That is not a valid number")
                        print ("Please enter number enter between 1 and 12 ") 
            burgers_ordered = burgers_ordered -1
            order_list.append(burger_names[burgers_ordered])
            order_cost.append(burger_prices[burgers_ordered])    
            print("{} ${:.2f}" .format(burger_names[burgers_ordered],burger_prices[burgers_ordered]))
            num_burgers = num_burgers-1

# Print order out - including if the order is pickup or delivery and names and prices of each item - total cost including any delivery charge

# Print order out - including if the order is pickup or delivery and names and prices of each item - total cost including any delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_pick == "Click and Collect":
        print("Your order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "Delivery":
        print("Your order is for Delivery")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    if del_pick == "Delivery":
        if len(order_list) >= 5:
            print("Your order will be Delivered to you for free")
        elif len(order_list) < 5:
            print("Due to the fact that you have ordered less than 5 items, there is a $9.00 surcharge for delivery")
            total_cost = total_cost + 9
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

    
# Ability to cancel or proceed with order
def confirm_order():
    print ("Please Confirm Your Order")
    print ("To Confirm please enter 1") 
    print ("To Cancel please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Order Confirmed")
                    print ("Your burger is being made")
                    print ("It will be ready soon")
                    break

                elif confirm == 2:
                    print ("Order Cancelled")
                    print ("You can restart your order or exit the BOT")
                    break
            else:
                print("Number must be 1 or 2")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 or 2 ")

# Option for new order or to exit

# Main Function
def main():
    '''
    Purpose: To run all functions
    A welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    list()
    order_burgers()
    print_order(del_pick)
    confirm_order()

main()
