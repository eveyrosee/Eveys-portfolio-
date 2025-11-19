SMALL_PIZZA_PRICE=3.25
MEDIUM_PIZZA_PRICE=5.50
LARGE_PIZZA_PRICE=7.15

DELIVERY_CHARGE=2.50

EXTRA_TOPPINGS_PRICE1=0.75
EXTRA_TOPPINGS_PRICE2=1.35
EXTRA_TOPPINGS_PRICE3=2
EXTRA_TOPPINGS_PRICE4=2.5

DISCOUNT=0.1

def get_pizza_cost(size,extraToppings) :
    price=0
    if size=="small":
        price=price+SMALL_PIZZA_PRICE
    elif size=="medium":
        price=price+MEDIUM_PIZZA_PRICE
    else:
        price=price+LARGE_PIZZA_PRICE
    print (price)

if extraToppings==1:
    price=price+EXTRA_TOPPINGS_PRICE1
elif extraToppings==2:
    price=price+EXTRA_TOPPINGS_PRICE2
elif extraToppings==3:
    price=price+EXTRA_TOPPINGS_PRICE3
else:
    price=price=EXTRA_TOPPINGS_PRICE4
return price

name=input("customer name: ")
address=input("address: ")
phone=input("phone number: ")
print("\nname: " , name , "\naddress: ", adress , "\nphone: " , phone )

delivery=input("do you want delivery? ")
if delivery=="yes" :
    print("delivery charge: ", DELIVERY_CHARGE) 
