import sys
import printTime
sys.path.insert(1, "tests/")
import test

if __name__ == "__main__":
    print("Enter hours worked throughout each shift in the format 5:12 -> 9:32:\n");

    rawHours = []
    userInput = "n/a"

    activeShift = 1
    userInput = input("Shift " + str(activeShift) + ": ")
    while (userInput != ""):
        activeShift += 1
        rawHours.append(userInput)
        userInput = input("Shift " + str(activeShift) + ": ")

    print()
    printTime.printTime(rawHours)