import inputToHours
import hourAdder

def printTime(rawHours):
    timesWorked = inputToHours.convertInputToHours(rawHours)
    totalTimeWorked = hourAdder.addHours(timesWorked)

    for i in range(len(rawHours)):
        userEntry = rawHours[i]
        timeWorked = timesWorked[i]

        print("\n\n" + userEntry + "\t=> " + timeWorked)
    
    print(totalTimeWorked)