#List of burger names
burger_names = ['Asus 14" burger - Intel Celeron 4GB-RAM 128GB','Asus 15.6" burger - Intel Core i7 16GB-RAM 512GB-SSD',
'Asus TUF 15.6" Gaming burger - Intel Core i5 8GB-RAM 512GB-SSD','Apple MacBook Air 13" with M1 Chip 512GB',
'Apple MacBook Pro 13" with M1 Chip 512GB','HP 15.6" burger - Intel Core i5 8GB-RAM 256GB-SSD',
'HP Pavilion 15.6" burger - AMD Ryzen5 16GB-RAM 512GB-SSD','HP Spectre x360 13.5" 2-in-1 burger - Intel Core i7 16GB-RAM 512GB-SSD',
'HP Envy x360 15.6" 2-in-1 burger - AMD Ryzen5 16GB-RAM 512GB-SSD','Acer Swift 3 14" burger - Intel Core i5 8GB-RAM 512GB-SSD',
'Acer TravelMate Spin B3 11.6" 2-in-1 burger with Pen - Intel Pentium 4GB-RAM 128GB-SSD',
'Acer Aspire 5 15.6" burger - AMD Ryzen5 8GB-RAM 256GB-SSD','Microsoft Surface burger 4 15" - AMD Ryzen7 8GB-RAM 256GB-SSD',
'Microsoft Surface burger 4 13.5" - Intel i5 16GB-RAM 512GB-SSD','Microsoft Surface burger Studio 14.4" - Intel i5 16GB-RAM 256GB-SSD',
'Lenovo IdeaPad 3 15.6" burger - Intel Pentium Silver 8GB-RAM 128GB-SSD','Lenovo Yoga 7i 14" 2-in-1 burger - Intel Core i5 16GB-RAM 512GB-SSD',
'Lenovo IdeaPad Flex 5 14" 2-in-1 burger - AMD Ryzen5 16GB-RAM 512GB-SSD']
#List of burger prices
burger_prices = [688,1884,1994,2149,2549,1584,1994,3997,3128,1698,836,1298,2499,2549,2699,994,2388,1984]

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
print("Please choose your burgers by entering the number from the menu")
for item in range(num_burgers):
    while num_burgers > 0:
        burger_ordered = int(input())
        order_list.append(burger_names[burger_ordered])
        order_cost.append(burger_prices[burger_ordered])    
        num_burgers = num_burgers-2

print(order_list)
print(order_cost)













