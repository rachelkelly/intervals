#!/bin/python3

import time
import os

runIntervals = int(input("how long should the running intervals be?\n > "))

intervalsCount = int(input("how many should there be?\n > "))

walkIntervals = int(input("how long should the breaks be?\n > "))

runMin = runIntervals/60
walkMin = walkIntervals/60

while intervalsCount > 0:
    #running = "Run for {0} minutes".format(runMin)
    os.system('echo "Running" | espeak')
    #print(running)
    time.sleep(runIntervals)

    #walking = "Walk for {0} minutes".format(walkMin)
    os.system('echo "Walking" | espeak')
    #print(walking)
    time.sleep(walkIntervals)

    intervalsCount -= 1
