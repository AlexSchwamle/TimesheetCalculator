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