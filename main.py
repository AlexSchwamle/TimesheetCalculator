def convertInputToHours(userInp):
	allHoursWorked = []
	for hour in userInp:
		workedHours = hour.split(" -> ")
		assert(len(workedHours) == 2)

		leftTime = workedHours[0].split(":")
		rightTime = workedHours[1].split(":")

		leftHour = int(leftTime[0])
		leftMin = int(leftTime[1])

		rightHour = int(rightTime[0])
		rightMin = int(rightTime[1])

		minutesWorked = rightMin - leftMin
		if minutesWorked < 0:
			minutesWorked = 60 + minutesWorked
			leftHour += 1

		hoursWorked = rightHour - leftHour

		timeWorked = str(hoursWorked) + "h" + str(minutesWorked) + "m"
		allHoursWorked.append(timeWorked)

	return allHoursWorked

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

hours = convertInputToHours(rawHours)

print(hours)