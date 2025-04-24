import config
import inputToHours
import hourAdder

def printTime(rawHours):
    savedTimes = []

    for i in range(len(rawHours)):
        rawHours[i] = rawHours[i].replace(";", ":").replace(".", ">")

    timesWorked = inputToHours.convertInputToHours(rawHours)
    totalTimeWorked = hourAdder.addHours(timesWorked)

    for i in range(len(rawHours)):
        userEntry = rawHours[i]
        timeWorked = timesWorked[i]

        moneyGainedBeforeTaxes, moneyGainedAfterTaxes = getTotalCash(timeWorked)

        totalUpToNowHours = ""
        if i > 0:
            totalUpToNowHours += " => " + hourAdder.getHoursUpToIndex(timesWorked, i+1)
            
        timeWorkedStr = userEntry + "\t=> " + timeWorked + totalUpToNowHours + (i == 0 and "\t" or "") + "\t(Gross $" + moneyGainedBeforeTaxes + ", Net $" + moneyGainedAfterTaxes + ")"
        print(timeWorkedStr)
        savedTimes.append(timeWorkedStr)
    
    totalCashEarnedBeforeTaxes, totalCashEarnedAfterTaxes = getTotalCash(totalTimeWorked)
    totalEarned = f"Total earned: Gross ${totalCashEarnedBeforeTaxes}, Net ${totalCashEarnedAfterTaxes}"
    totalTimeWorkedStr = "Worked " + totalTimeWorked

    print(totalEarned)
    print(totalTimeWorkedStr)
    printTotalDecimalTime(totalTimeWorked)
    
    savedTimes.append(totalEarned)
    savedTimes.append(totalTimeWorkedStr)
    savedTimes.append("Total decimal time: " + getDecimalTime(totalTimeWorked) + "h")
    return savedTimes

def printTotalDecimalTime(string):
    print(getDecimalTime(string) + "h")

def getDecimalTime(string):
    totalTimeWorked = string.strip("m").split("h")

    minFraction = str(round(int(totalTimeWorked[1])/60, 2))
    if minFraction.startswith("0."):  
        minFraction = minFraction[1:]
        
    return totalTimeWorked[0] + minFraction
    
def getTotalCash(timeWorked):
    moneyGainedHelper = getDecimalTime(timeWorked)
    moneyGainedBeforeTaxes = round(float(moneyGainedHelper) * config.payPerHour, 2)
    moneyGainedAfterTaxes = round(moneyGainedBeforeTaxes * (1 - (config.averageTaxes / 100)), 2)
    return str(moneyGainedBeforeTaxes), str(moneyGainedAfterTaxes)