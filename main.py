import sys
import inputToHours
import hourAdder
sys.path.insert(1, "tests/")
import test

print("Enter hours worked throughout each shift in the format 5:12 -> 9:32:\n");

hours = []
rawHours = []
userInput = "n/a"

activeShift = 1
userInput = input("Shift " + str(activeShift) + ": ")
while (userInput != ""):
	activeShift += 1
	rawHours.append(userInput)
	userInput = input("Shift " + str(activeShift) + ": ")

timesWorked = inputToHours.convertInputToHours(rawHours)
totalTimeWorked = hourAdder.addHours(timesWorked)

for i in range(len(rawHours)):
	userEntry = rawHours[i]
	timeWorked = timesWorked[i]

	print("\n\n" + userEntry + "\t=> " + timeWorked)
	
print(totalTimeWorked)