#Menu so that user can choose click and collect or delivery\

# Bug - need it so that it only accepts 1 or 2

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
