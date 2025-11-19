import math

#declaring constants
METER_PER_LITRE=5
DOOR_AREA=2.5
LABOUR_COST_PER_METER=3
TIN_5L_COST=50
TIN_3L_COST=35
TIN_2L_COST=25
TIN_1L_COST=15

while True:
    wallsNum=int(input("how many walls are there?"))
    if wallsNum>0 and wallsNum<=20:
        break

    else:
        print("data must be between 1 and 20") 
for i  in range (0,wallsNum) :
    wallLength = float(input("enter the length of the wall"))
    wallWidth = float(input("enter the width of the wall")) 
    wallArea = wallLength*wallWidth

    windowLength = float(input("enter the length of the window"))
    windowWidth = float(input("enter the width of the window"))
    windowArea = windowLength*windowWidth

    isDoor= input("Is there a door on the wall?")
    if isDoor == "True":
        doorArea=2.5
    else:
        doorArea=0

    paintArea = wallArea-windowArea-doorArea
    totalPaintArea = paintArea

print ("total paint area: " , totalPaintArea)
litresNeeded=  math.ceil(totalPaintArea/METER_PER_LITRE)
print ("litres needed: " , litresNeeded)
tin5l= litresNeeded//5
print("the amount of 5l tins you need are" , tin5l)
remainder= litresNeeded % 5
tin3l= remainder // 3
print("the amount of 3l tins you need are" , tin3l)
remainder=remainder % 3
tin2l= remainder // 2
print ("the amount of 2l tins you need are", tin2l)
remainder=remainder % 2
tin1l= remainder // 1
print ("the amount of 1l tins you need are" , tin1l)
remainder= remainder % 1
tinCost = ( TIN_5L_COST * tin5L ) + ( TIN_3L_COST * tin3L ) + ( TIN_2L_COST * tin2L ) + ( TIN_1L_COST * tin1L )
print("Cost of tins: " , tinCost)
litresNeeded = math.ceil(totalPaintArea / METRE_PER_LITR)
print("Litres needed: " , litresNeeded)
labourCost = totalPaintArea * LABOUR_COST_PER_METRE
print("Labour cost: " , labourCost)
totalCost = tinCost + labourCost
print("Total cost: " , totalCost)
