def searchBinary(searchableList, item):
    rangeNumberLow = 0;
    rangeNumberHigh = len(searchableList) - 1;
    totalAttempts = 0;
    
    while (rangeNumberLow <= rangeNumberHigh):
        totalAttempts+= 1
        
        targetNumber = (rangeNumberLow + rangeNumberHigh) // 2
        hint = searchableList[targetNumber]

        if (hint == item):
            return totalAttempts, targetNumber
        
        if (hint > item):
            rangeNumberHigh = targetNumber - 1
        else:
            rangeNumberLow = targetNumber + 1
    
    return None

searchableList = [1, 3, 5, 7, 9, 11, 13, 14, 20, 30, 45, 66]
resultIndex, resultAttempts = searchBinary(searchableList, 66);

print("The number is located at the index {index} and was found in {attempts} attempts"
    .format(index=resultIndex, attempts=resultAttempts))