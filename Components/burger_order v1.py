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


#Item List
def list():
    number_burgers = 12

    for count in range (number_burgers):
            print("{} {} ${:.2f}"  .format(count+1,burger_names[count],burger_prices[count]))











#Countdown until all burger are ordered



#print order
