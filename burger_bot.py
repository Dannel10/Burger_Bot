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
    
    num = randint(0,9)
    name = (names[num])
    print("***Welcome to Burger Place***")
    print("**My name is",name, "***")
    print("***I will be here to help you order your delicious Burger*** ")
    


#Menu so that user can choose click and collect or delivery
def collect():
    print ("Do you want your order delivered or do you want to click and collect?")
    print ("For click and collect enter 1 ")
    print ("For delivery enter 2 ")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and Collect")
                    break
                    
                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print("Number must be 1 or 2")
        except ValueError:
            print("That was not a valid input")
            print("Please enter 1 or 2")

# Pickup information - Name and Phone




# Delivery information - Name, Address and Phone




# Choose total number of items




# Item List




# Item(s) ordered - from item list - print each ordered item with cost




# Print order out - including if the order is pickup or delivery and names and prices of each item - total cost including any delivery charge




# Ability to cancel or proceed with order




# Option for new order or to exit
    
    
    
    
    
    
    
#Main function
def main():
    '''
    Purpose: to run all functions
    a welcome message
    Parameters: None
    Returns:None
    '''
    welcome()
    collect()
    
   
main()