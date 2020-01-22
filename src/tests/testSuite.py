import sys

class testSuite:
    testsToRun = []
    shouldStop = False

    def __init__(self):
        self.testsToRun = []
        self.shouldStop = False

    def add(self, expected, actual):
        self.testsToRun.append([expected, actual])

    def run(self):
        for test in self.testsToRun:
            try:
                assert(test[0] == test[1])
            except:
                print("Error! Values were not equal: " + test[0] + " & " + test[1])
                self.shouldStop = True

        if self.shouldStop:
            sys.exit(1)

