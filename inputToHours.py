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
		if hoursWorked == 0 and (rightMin - leftMin) < 0:
			hoursWorked = 12
		elif hoursWorked < 0:
			rightHour = 12 + rightHour
			hoursWorked = rightHour - leftHour
		
		hoursStr = str(hoursWorked)
		minsStr = minutesWorked < 10 and "0" or ""
		minsStr += str(minutesWorked)
		timeWorked = hoursStr + "h" + minsStr + "m"
		allHoursWorked.append(timeWorked)
	return allHoursWorked
