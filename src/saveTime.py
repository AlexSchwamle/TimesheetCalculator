from time import strftime
from os import makedirs

def savePrintedTimes(printedTimes, nameOfLog):
    currentDayForFile = strftime("%Y-%m-%d")
    currentTimeForProjectHeader = strftime("%I:%M %p")
    makedirs("../savedLogs", exist_ok=True)
    with open(f"../savedLogs/{currentDayForFile}.txt", "a") as file:
        file.write(f"Project: {nameOfLog} ({currentTimeForProjectHeader})\n")
        for printedLine in printedTimes:
            file.write("\t" + printedLine + "\n")