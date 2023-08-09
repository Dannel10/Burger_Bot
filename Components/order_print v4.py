#List to store ordered pizzas
order_list = ['The Classic Cheese Burger - The Classic juciy beef patty, lettuce tomato, pickles, cheese on seasame bun',
                'BBQ Bacon Burger - Grilled beef patty, bacon, cheader cheese and BBQ sause, onions',
                'Mushroom Swiss Burger - Sauteed mushrooms with melted swis cheese',
                'Veggie Burger - With avocado slices and cilantro-lime mayo',]
#List to store pizzas prices
order_cost = [7.50, 7.50, 7.50, 7.50,]

cust_details = {'Name':'Mark', 'Phone':'0214635678', 'House':'34', 'Street':'Dragon', 'Surburb':'Flat Bush'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {cust_details['Name']} \nCustomer Phone: {cust_details['Phone']} \nCustomer Address: {cust_details['House']} {cust_details['Street']} {cust_details['Surburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"${total_cost:.2f}")

print_order()