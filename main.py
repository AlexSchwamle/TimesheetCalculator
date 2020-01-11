import inputToHours

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

hours = inputToHours.convertInputToHours(rawHours)

print(hours)