import tests.testSuite as testSuite
import inputToHours
import hourAdder

hoursForTesting1 = [
    "3:23 -> 4:08",
    "4;50 -> 5:28",
    "5:31 -> 5;46",
    "6:51 -> 7;23"
]
hoursForTesting2 = [
    "8;41 -. 10;18",
    "10;36 -> 1;07"
]
hoursForTesting3 = [
    "4:16 -> 4:54",
    "5:02 -> 5:39",
    "5:40 -> 5:47",
    "7:01 -> 8:22",
    "9:29 -> 11:44"
]

totalTimeWorkedResults = [
    .00,
	.02,
	.03,
	.05,
	.07,
	.08,
	.10,
	.12,
	.13,
	.15,
	.17,
	.18,
	.20,
	.22,
	.23,
	.25,
	.27,
	.28,
	.30,
	.32,
	.33,
	.35,
	.37,
	.38,
	.40,
	.42,
	.43,
	.45,
	.47,
	.48,
	.50,
	.52,
	.53,
	.55,
	.57,
	.58,
	.60,
	.62,
	.63,
	.65,
	.67,
	.68,
	.70,
	.72,
	.73,
	.75,
	.77,
	.78,
	.80,
	.82,
	.83,
	.85,
	.87,
	.88,
	.90,
	.92,
	.93,
	.95,
	.97,
	.98,
	1
]

print("Running tests...")

tests = testSuite.testSuite()

timesWorked = inputToHours.convertInputToHours(hoursForTesting1)
totalTimeWorked = hourAdder.addHours(timesWorked)
tests.add(totalTimeWorked, "2h10m")

timesWorked = inputToHours.convertInputToHours(hoursForTesting2)
totalTimeWorked = hourAdder.addHours(timesWorked)
tests.add(totalTimeWorked, "4h08m")

timesWorked = inputToHours.convertInputToHours(hoursForTesting3)
totalTimeWorked = hourAdder.addHours(timesWorked)
tests.add(totalTimeWorked, "4h58m")

for i in range(0, 61):
    expect = totalTimeWorkedResults[i]
    algorithm = round(i/60.0, 2)
    tests.add(expect, algorithm)    

tests.run()