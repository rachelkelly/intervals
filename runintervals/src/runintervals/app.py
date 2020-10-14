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
        """
        Iterate through intervals and breaks, as defined 
        in runInt(), runLength(), & breakLength()
        """
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
            #self.main_window.info_dialog(
            #    'Message',
            #    "Run for {} minutes.".format(loopNum)
            #)
            # TODO: text to speech "Run for {} minutes.".format(loopNum)
            #   - would love to add two fast beeps before TTS
            print('\a')
            time.sleep(intSeconds)
            if loopNum == 1:
            #    self.main_window.info_dialog(
            #        'Message',
            #        "You're done!"
            #    )
            # TODO: text to speech "You're done!  Great job!"
                print() 
            else:
                #self.main_window.info_dialog(
                #    'Message',
                #    "You're walking"
                #)
                # TODO: TTS "You're walking"
                #  - ideally one long beep before TTS
                time.sleep(breakSeconds)
            loopNum -= 1

        # TTS: "Cool down, walk and chill out and stretch for 5 minutes.  Take it easy and eat something delicious that you love."

def main():
    return RunIntervals()
