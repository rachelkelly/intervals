"""
Run Intervals.  Takes 3 values from user, counts down intervals.

wanted: Data class that holds state
"""
from datetime import timedelta
import time

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class RunIntervals(toga.App):
    """
    __init__ values in __init__.py:
    runsNumber=5, runsLength=5, breakLength=1, 
    currentStatus='inactive', displayTime=0, runStartTime=0
    """

    def startup(self):
        """
        Define box & visual elements.

        For each individual input, must have:
         a) toga.Label
         b) toga.TextInput
         c) toga.Button
         d) add the above attributes to mainBox

        Take values from user or use defaults, add to mainBox
        """
        mainBox = toga.Box(style=Pack(direction=COLUMN))

        # intervals count
        runIntLabel = toga.Label(
                "How many intervals to run? Hit Submit to use default of 5 total:",
            style=Pack(padding=(0, 5))
        )
        self.runIntInput = toga.TextInput(style=Pack(flex=1))

        runIntBox = toga.Box(style=Pack(direction=ROW, padding=5))
        runIntBox.add(runIntLabel)
        runIntBox.add(self.runIntInput)

        runIntButton = toga.Button(
            'Submit',
            on_press=self.runInt,
            style=Pack(padding=5)
        )


        #how long each interval  
        runLengthLabel = toga.Label(
            'How long should each running interval be?  Hit Submit to use default of 5 minutes:',
            style=Pack(padding=(0, 5))
        )
        self.runLengthInput = toga.TextInput(style=Pack(flex=1))

        runLengthBox = toga.Box(style=Pack(direction=ROW, padding=5))
        runLengthBox.add(runLengthLabel)
        runLengthBox.add(self.runLengthInput)

        runLengthButton = toga.Button(
            'Submit',
            on_press=self.runLength,
            style=Pack(padding=5)
        )


        #how long are breaks
        breakLengthLabel = toga.Label(
            'How long should breaks between runs be?  Hit Submit to use default of 1 minute: ',
            style=Pack(padding=(0, 5))
        )
        self.breakLengthInput = toga.TextInput(style=Pack(flex=1))

        breakLengthBox = toga.Box(style=Pack(direction=ROW, padding=5))
        breakLengthBox.add(breakLengthLabel)
        breakLengthBox.add(self.breakLengthInput)

        breakLengthButton = toga.Button(
            'Submit',
            on_press=self.breakLength,
            style=Pack(padding=5)
        )

        #Start button
        # if values for all of the above, then Start button
        startLabel = toga.Label(
            'Start!',
            style=Pack(padding=(0, 5))
        )
        startBox = toga.Box(style=Pack(direction=ROW, padding=5))
        startBox.add(startLabel)

        startButton = toga.Button(
            'Start!',
            on_press=self.start,
            style=Pack(padding=5)
        )


        mainBox.add(runIntBox)
        mainBox.add(runIntButton)
        
        mainBox.add(runLengthBox)
        mainBox.add(runLengthButton)

        mainBox.add(breakLengthBox)
        mainBox.add(breakLengthButton)

        # would like to refresh and only display this once all 3 values have been entered
        mainBox.add(startBox)
        mainBox.add(startButton)

        if currentStatus == "active":
            # only start displaying timer stuff if currentStatus is valid
            mainBox.add(timeBox)
            pass


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = mainBox
        self.main_window.show()


    def runInt(self, widget):
        """
        Output number of intervals
        """
        runsNumber = self.runIntInput.value
        self.main_window.info_dialog(
            'Hi there!',
            "You will be running {} intervals today.".format(runsNumber)
        )

    def runLength(self, widget):
        """
        Output length of intervals
        """
        runsLength = self.runLengthInput.value
        self.main_window.info_dialog(
            'Hi there!',
            "You will be running each interval at {} minutes.".format(runsLength)
        )

    def breakLength(self, widget):
        """
        Output length of breaks
        """
        breaksLength = self.breakLengthInput.value
        self.main_window.info_dialog(
            'Hi there!',
            "Your breaks will be {} minute(s) long.".format(breaksLength)
        )

    def mainTimer(self, toWait):
        """
        Timer to display to window.  Does not care what kind of timer it is.
        this will output a time, calculated dynamically based on runStartTime
        """
        return timedelta(seconds='toWait')

    def displayTimer(self):
        """
        just to display mainTimer output, not calculate it
        does this need mainBox?
        """
        timeLabel = toga.Label(
            "Seconds left: {}".format(mainTimer(displayTime)),
            style=Pack(padding=(0, 5))
        )
        timeBox = toga.Box(style=Pack(direction=ROW, padding=5))
        timeBox.add(timeLabel)
       

    def start(self, widget):
        """
        Iterate through intervals and breaks, as defined 
        in runInt(), runLength(), & breakLength()
        """
        runStartTime = time.time()
        currentStatus = "active"

        runsNumber = int(self.runIntInput.value) # should not have to repeat this.

        runsLength = int(self.runLengthInput.value)
        loopNum = runsNumber
        intSeconds = runsLength * 60 # seconds

        breaksLength = self.breakLengthInput.value # ibid 152
        walkinglength = int(breaksLength)
        breakSeconds = walkinglength * 60 # seconds

        # TTS: "Warm up, brisk walk for 5 minutes"

        # DELETE
        print("loopNum: {}".format(loopNum))
        print("interval seconds: {}".format(intSeconds))
        print("break seconds: {}".format(breakSeconds))

        while loopNum > 0:
            runLabel = toga.Label(
                   "You are running",
                style=Pack(padding=(0, 5))
                )
            runLabelBox = toga.Box(style=Pack(direction=ROW, padding=5))
            runLabelBox.add(runLabel)
            mainBox.add(runLabelBox)
 
            mainTimer(intSeconds)

           
            if loopNum == 1:
                # create Label that says "you're done!" and add it to mainBox
                # TODO: text to speech "You're done!  Great job!"
                print() 
            else:
                # create Label that says "you're walking" and add it to mainBox
                mainTimer(breakSeconds)
                # TODO: TTS "You're walking"
                #  - ideally one long beep before TTS
                time.sleep(breakSeconds)
            loopNum -= 1

        # TTS: "Cool down, walk and chill out and stretch for 5 minutes.  Take it easy and eat something delicious that you love."

def main():
    return RunIntervals()
