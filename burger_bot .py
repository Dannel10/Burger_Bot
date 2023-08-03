# burger Shop Bot
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
    print ("Is your order for Click and Collect or delivery")
    print ("For Click and Collect please enter 1") 
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and Collect")
                    Click_and_Collect_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print("Number must be 1 or 2")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 or 2 ")

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
        print("{} {} ${:.2f}"   .format(count+1,burger_names [count],burger_prices[count]))

        
# Choose total number of items
def order_burgers():
    
    while True:
        try:
            num_burgers = int(input("How many burgers do you want to order? "))
            if num_burgers >= 1:
                break
            else:
                print("Your order must be at least 1 burger.")
        except ValueError:
            print("That is not a valid number.")
            print("Please enter a number greater than or equal to 1.")

    for item in range(num_burgers):
        while num_burgers > 0:
            while True:
                try:
                    burgers_ordered = int(input("Please choose your burgers by entering the number from the list: "))
                    if 1 <= burgers_ordered <= len(burger_names):
                        break
                    else:
                        print("Your number must be between 1 and", len(burger_names))
                except ValueError:
                    print("That is not a valid number.")
                    print("Please enter a number between 1 and", len(burger_names))
            
            burgers_ordered = burgers_ordered - 1
            burger_names.append(burger_names[burgers_ordered])
            burger_prices.append(burger_prices[burgers_ordered])
            print("{} ${:.2f}".format(burger_names[burgers_ordered], burger_prices[burgers_ordered]))
            num_burgers = num_burgers - 1




# Item(s) ordered - from item list - print each ordered item with cost


# Print order out - including if the order is pickup or delivery and names and prices of each item - total cost including any delivery charge


# Ability to cancel or proceed with order


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
    order_type()
    list()
    order_burgers()


main()