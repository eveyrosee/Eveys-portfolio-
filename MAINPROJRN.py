GBP_TO_USD= 1.40
GBP_TO_EUR= 1.14
GBP_TO_REAL= 4.77
GBP_TO_YEN= 151.05
GBP_TO_LIRA= 5.68

E300_GBP_FEE= 0.035
OVER_300GBP_FEE= 0.03
OVER_750GBP_FEE=0.025
OVER_1000GBP_FEE=0.02
OVER_2000GBP_FEE=0.015
DISCOUNT_RATE= 0.95

name = input("Enter name: ")
address = input("Enter address: ")
phoneNumber = input("Enter phone number: ")

def validate_quantity_range(qty):
    while qty < 1 or qty > 2500:
        print("Not in range, please re-enter number of pizzas.")
        qty = int(input("Enter number between 1 and 2500:"))
    return qty

quantity = int(input("Enter number between 1 and 2500:"))
quantity = validate_quantity_range(quantity)


while True:
    currency = input("enter a currency (USD, EUR, BRL, JPY, TRY)") 
    if currency == "USD":
        moneyConv = quantity * GBP_TO_USD
        break
    elif currency == "EUR":
        moneyConv = quantity * GBP_TO_EUR
        break
    elif currency == "BRL":
        moneyConv = quantity * GBP_TO_REAL
        break
    elif currency == "JPY":
        moneyConv = quantity * GBP_TO_YEN
        break
    elif currency == "TRY":
        moneyConv = quantity * GBP_TO_LIRA
        break
    else:
        print("Invalid currency entered, please enter a currency")
        

if quantity <300 :
    transFee = quantity * E300_GBP_FEE
elif quantity <750 :
    transFee = quantity * OVER_300GBP_FEE
elif quantity <1000:
    transFee = quantity * OVER_750GBP_FEE
elif quantity <2000:
    transFee = quantity * OVER_1000GBP_FEE
else:
    transFee = quantity * OVER_2000GBP_FEE

totalCost= moneyConv + transFee 

staff= input("are you a staff member") 
if staff=="yes" :
    discount = totalCost * DISCOUNT_RATE
else:
    discount=totalCost
    
print("---Order Summary---")
print("Name:", name)
print("Address:", address)
print("Phone number:", phoneNumber)
print(moneyConv)
print(transFee)       
print(discount)
print("-----------------")
