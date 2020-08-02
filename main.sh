#!/bin/bash

echo "how long should the running intervals be?"
read runIntervals

echo "how many should there be?"
read intervalsCount

echo "how long should the breaks be?"
read walkIntervals

runMin=$(expr $runIntervals / 60)
walkMin=$(expr $walkIntervals / 60)

echo "Run for $runMin minutes" |espeak

#sleep 300
sleep 3

echo "Walk for $walkMin minutes" |espeak

#sleep 120
sleep 1

echo "Good job, you are done" |espeak
