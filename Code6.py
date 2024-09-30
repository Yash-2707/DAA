def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True) 

    totalUnits = 0
    boxesUsed = 0 

    for boxes, unitsPerBox in boxTypes:
        if boxes <= truckSize - boxesUsed:
            totalUnits += boxes * unitsPerBox
            boxesUsed += boxes
        else:
            remainingSpace = truckSize - boxesUsed
            totalUnits += remainingSpace * unitsPerBox
            boxesUsed += remainingSpace
            break 
    return totalUnits

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print("Maximum units:", maximumUnits(boxTypes, truckSize))