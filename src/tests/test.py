import sys
import testSuite
sys.path.insert(1, "../")
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

tests.run()