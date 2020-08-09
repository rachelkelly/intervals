"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # for each input, must have toga.Label, toga.TextInput, toga.Button, & then add to main_box
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


        main_box.add(runIntBox)
        main_box.add(runIntButton)
        
        main_box.add(runLengthBox)
        main_box.add(runLengthButton)

        #main_box.add(breakLengthBox)
        #main_box.add(breakLengthButton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def runInt(self, widget):
        if self.runIntInput.value:
            runsNumber = self.runIntInput.value
        else:
            runsNumber = 5

        self.main_window.info_dialog(
            'Hi there!',
            "You will be running {} intervals today.".format(runsNumber)
        )

    def runLength(self, widget):        
        if self.runLengthInput.value:
            runsLength = self.runLengthInput.value
        else:
            runsLength = 5

        self.main_window.info_dialog(
            'Hi there!',
            "You will be running each interval at {} minutes.".format(runsLength)
        )

def main():
    return HelloWorld()
