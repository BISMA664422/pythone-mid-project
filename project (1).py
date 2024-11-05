
#define the menu of restaurant
menu = {
     "chicken pizza":500,
     "veg pizza":300,
     "burger":250,
     "pasta":200,
     "coffee":100,
     "tea":80,
 }
#greet
print("Welcome to the RBS kitchen") 
print("chicken pizza:Rs500\nvegpizza:Rs300\nburger:Rs250\npasta:Rs200\ncoffee:Rs100\ntea:Rs80")

order_total = 0
#500+80=580

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0+500
    print(f"your item {item_1} has been added to your order")
    
else:
    print(f"order item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (yes/no) ")
if another_order == "Yes":
    item_2 = input("Enter the name of seconde item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")
  
print(f"The total amount of items to pay is {order_total}")
print("Thanks for coming in The RBS kitchen")
