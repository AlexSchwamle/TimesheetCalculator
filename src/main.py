import printTime
import tests.test
from saveTime import savePrintedTimes

def run():
    nameOfLog = input("Enter the name of the project to save this time under: ") 

    print("Enter hours worked throughout each shift in the format 5:12 -> 9:32:\n")

    rawHours = []
    userInput = "n/a"

    activeShift = 1
    userInput = input("Shift " + str(activeShift) + ": ")
    while (userInput != ""):
        activeShift += 1
        rawHours.append(userInput)
        userInput = input("Shift " + str(activeShift) + ": ")

    print()
    printedTimes = printTime.printTime(rawHours)
    savePrintedTimes(printedTimes, nameOfLog)

    input("Press Enter or the upper right X to terminate script.\n")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nCtrl+C pressed, exiting...")