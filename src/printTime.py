import inputToHours
import hourAdder

def printTime(rawHours):
    for i in range(len(rawHours)):
        rawHours[i] = rawHours[i].replace(";", ":").replace(".", ">")

    timesWorked = inputToHours.convertInputToHours(rawHours)
    totalTimeWorked = hourAdder.addHours(timesWorked)

    for i in range(len(rawHours)):
        userEntry = rawHours[i]
        timeWorked = timesWorked[i]

        totalUpToNowHours = ""
        if i > 0:
            totalUpToNowHours += " => " + hourAdder.getHoursUpToIndex(timesWorked, i+1)
        print(userEntry + "\t=> " + timeWorked + totalUpToNowHours)
    
    print(totalTimeWorked)
    printTotalDecimalTime(totalTimeWorked)

def printTotalDecimalTime(string):
    totalTimeWorked = string.strip("m").split("h")

    minFraction = str(round(int(totalTimeWorked[1])/60, 2))
    if minFraction.startswith("0."):  
        minFraction = minFraction[1:]
        
    decimalTime = totalTimeWorked[0] + minFraction

    print(decimalTime)