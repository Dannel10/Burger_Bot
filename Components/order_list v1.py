#List of burger names
burger_names = ['The Classic Cheese Burger - The Classic juciy beef patty, lettuce tomato, pickles, cheese on seasame bun',
                'BBQ Bacon Burger - Grilled beef patty, bacon, cheader cheese and BBQ sause, onions','Mushroom Swiss Burger - Sauteed mushrooms with melted swis cheese',
                'Veggie Burger - With avocado slices and cilantro-lime mayo', 'Double Trouble - Double Chiken patty, lettuce, tomato, mayo, pickle, fried egg', 
                'Hawaiian Teriyaki Burger - Grilled chicken/beef,pinaple glaze with lettuce and mayo','Chipotle Burger - Seasoned beef patty, pepper black cheese, bacon and chipotle sause',
                'Breakfast Burger - Beef/pork patty, fried egg, with melted cheese, tomato and bacon','Blue Cheese Greeny Burger - With caramilzed onions and Dijon musturd', 
               'Mediterranean Falafel Burger - Falafal patty, pita/bun, lettuce cucumber, red onions and tahini sause','Surf n Turf Burger - Beef patty, grilled shrimp, garlic aioli, and tomatoes ',
               'Gourmet Burger - Premium beef patty, argula, onions, and trffel aioli',]
#List of burger prices
burger_prices = [7.50, 7.50, 7.50, 7.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50,13.50, 13.50]

#list to store ordered burgers
order_list = []
#list to store burger prices
order_cost = []



def menu():
    number_burgers = 12

    for count in range (number_burgers):
        print("{} {} ${:.2f}"   .format(count+1,burger_names[count],burger_prices[count]))

menu()

# ask for total number of burgers for order
num_burgers = 0

num_burgers = int(input("How many burgers do you want to order? "))

print(num_burgers)

# Choose burgers from the list
print("Please choose your burgers by entering the numbe1r from the menu")
for item in range(num_burgers):
    while num_burgers > 0:
        burger_ordered = int(input())
        order_list.append(burger_names[burger_ordered])
        order_cost.append(burger_prices[burger_ordered])    
        num_burgers = num_burgers-1

print(order_list)
print(order_cost)
