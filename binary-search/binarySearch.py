class BinarySearch(object):
    def calculateIndex(searchableList, item):
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