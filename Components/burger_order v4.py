burger_names = ['The Classic Cheese Burger - The Classic juicy beef patty, lettuce, tomato, pickles, cheese on sesame bun',
                'BBQ Bacon Burger - Grilled beef patty, bacon, cheddar cheese and BBQ sauce, onions',
                'Mushroom Swiss Burger - Sauteed mushrooms with melted Swiss cheese',
                'Veggie Burger - With avocado slices and cilantro-lime mayo',
                'Double Trouble - Double Chicken patty, lettuce, tomato, mayo, pickle, fried egg',
                'Hawaiian Teriyaki Burger - Grilled chicken/beef, pineapple glaze with lettuce and mayo',
                'Chipotle Burger - Seasoned beef patty, pepper jack cheese, bacon and chipotle sauce',
                'Breakfast Burger - Beef/pork patty, fried egg, with melted cheese, tomato and bacon',
                'Blue Cheese Greeny Burger - With caramelized onions and Dijon mustard',
                'Mediterranean Falafel Burger - Falafel patty, pita/bun, lettuce cucumber, red onions and tahini sauce',
                'Surf n Turf Burger - Beef patty, grilled shrimp, garlic aioli, and tomatoes',
                'Gourmet Burger - Premium beef patty, arugula, onions, and truffle aioli']

burger_prices = [7.50, 7.50, 7.50, 7.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50]

order_list = []
order_cost = []

def menu():
    number_burgers = len(burger_names)

    for count in range(number_burgers):
        print("{} {} ${:.2f}".format(count + 1, burger_names[count], burger_prices[count]))

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
            order_list.append(burger_names[burgers_ordered])
            order_cost.append(burger_prices[burgers_ordered])
            print("{} ${:.2f}".format(burger_names[burgers_ordered], burger_prices[burgers_ordered]))
            num_burgers = num_burgers - 1

menu()
order_burgers()
