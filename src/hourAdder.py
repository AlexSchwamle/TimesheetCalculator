def addHours(hours):
	totalHours = 0
	totalMinutes = 0
	for timeWorked in hours:
		time = timeWorked.strip("m")
		time = time.split("h")
		
		totalHours += int(time[0])
		totalMinutes += int(time[1])

	hoursWorkedViaMinutes = totalMinutes // 60
	totalHours += hoursWorkedViaMinutes
	totalMinutes = totalMinutes % 60

	completeTotal = str(totalHours) + "h"
	completeTotal += totalMinutes < 10 and "0" or ""
	completeTotal += str(totalMinutes) + "m"
	return completeTotal