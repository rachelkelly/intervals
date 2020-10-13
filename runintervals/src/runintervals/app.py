"""
Run Intervals.  Takes 3 values from user, counts down intervals.
"""
import time

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class RunIntervals(toga.App):
    """
    __init__ values in __init__.py
    """

    def startup(self):
        """
        Define box & visual elements.

        For each individual input, must have:
         a) toga.Label
         b) toga.TextInput
         c) toga.Button
         d) add the above attributes to main_box

        Take values from user or use defaults, add to main_box
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # intervals count
        runIntLabel = toga.Label(
                'How many intervals to run? Hit Submit to use default of 5 total: ',
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
            'How long should each running interval be?  Hit Submit to use default of 5 minutes: ',
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


        main_box.add(runIntBox)
        main_box.add(runIntButton)
        
        main_box.add(runLengthBox)
        main_box.add(runLengthButton)

        main_box.add(breakLengthBox)
        main_box.add(breakLengthButton)

        # would like to refresh and only display this once all 3 values have been entered
        main_box.add(startBox)
        main_box.add(startButton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
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

    def start(self, widget):
        pass
#        """
#        Iterate through intervals and breaks, as defined 
#        in runInt(), runLength(), & breakLength()
#        """
#        loopNum = runsNumber # needs to be self.runsNumber?
#        intSeconds = loopNum * 60 # seconds
#
#        walkinglength = breaksLength # needs to be self.breaksLength?
#        breakSeconds = walkinglength * 60 # seconds
#
#        while loopNum > 0:
#            print("run for {} minutes").format(loopNum)
#            time.sleep(intSeconds)
#            self.main_window.info_dialog(
#                'Message',
#                "Run for {} minutes.".format(loopNum)
#            )
#            if loopNum == 1:
#                print("you are done")
#            else:
#                print("walking")
#                time.sleep(breakSeconds)
#            loopNum -= 1

def main():
    return RunIntervals()
