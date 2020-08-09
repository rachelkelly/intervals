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
        self.name_input = toga.TextInput(style=Pack(flex=1))

        runIntBox = toga.Box(style=Pack(direction=ROW, padding=5))
        runIntBox.add(runIntLabel)
        runIntBox.add(self.name_input)

        runIntButton = toga.Button(
            'Submit',
            on_press=self.runInt,
            style=Pack(padding=5)
        )

        main_box.add(runIntBox)
        main_box.add(runIntButton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def runInt(self, widget):
        if self.name_input.value:
            runsNumber = self.name_input.value
        else:
            runsNumber = 5

        self.main_window.info_dialog(
            'Hi there!',
            "You will be running {} intervals today.".format(runsNumber)
        )

def main():
    return HelloWorld()
