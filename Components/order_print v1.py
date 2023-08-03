#List to store ordered pizzas
order_list = ['The Classic Cheese Burger - The Classic juciy beef patty, lettuce tomato, pickles, cheese on seasame bun',
                'BBQ Bacon Burger - Grilled beef patty, bacon, cheader cheese and BBQ sause, onions',
                'Mushroom Swiss Burger - Sauteed mushrooms with melted swis cheese',
                'Veggie Burger - With avocado slices and cilantro-lime mayo',]
#List to store pizzas prices
order_cost = [7.50, 7.50, 7.50, 7.50,]

cust_details = {'Name':'Mark', 'Phone':'0214635678', 'House':'32', 'Street':'fars', 'Surburb':'Flat Bush'}

#print("\n",cust_details['Name'], "\n",cust_details['Phone'], "\n",cust_details['House'], "\n",cust_details['Street'], "\n",cust_details['Surburb'])

print("\n Customer Name: {} Customer Phone:\n{} Customer House:\n{} Customer Street:\n{} Customer Surburb:\n{}" .format(cust_details['Name'],cust_details['Phone'],cust_details['House'],cust_details['Street'],cust_details['Surburb']))

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1