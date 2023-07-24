#Bugs
#Will only work for vaild input "d" and "c"
#Invaild input triggers else statement but program does not ask for input agian

#Menu so that user can choose click and collect or delivery


print ("Do you want your order delivered or do you want to click and collect?")

print ("For click and collect enter 1 ")
print ("For delivery enter 2 ")

delivery = int(input())

if delivery == 1:
    print ("Click and Collect")
           
elif delivery == 2:
    print ("Delivery")

else:
    print("That was not a vaild input")
    
