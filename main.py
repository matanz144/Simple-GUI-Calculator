"""
Implementation of a simple calculator using Python.
GUI build with PyQt5 package.
"""


import math
import sys
from PyQt5.QtWidgets import *


# Define Button class
class Button:
    def __init__(self, text, result):
        self.text = text
        self.result = result
        self.button = QPushButton(str(text))
        self.button.clicked.connect(lambda: self.handleInput(self.text))

    # Handling the input and operations that need to calculate
    def handleInput(self, value):
        if value == "AC":
            self.result.setText("")
        elif value == "=":
            res = eval(self.result.text())
            self.result.setText(str(res))
        elif value == "√":
            val = float(self.result.text())
            self.result.setText(str(math.sqrt(val)))
        elif value == "DEL":
            new_value = self.result.text()[:-1]
            self.result.setText(new_value)
        else:
            current_value = self.result.text()
            new_value = current_value + str(value)
            self.result.setText(new_value)


# Define the GUI of the application
class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.appPage()

    def appPage(self):
        # Initialize grid layout
        grid = QGridLayout()

        # Initialize Input line
        input_line = QLineEdit()

        # Define the buttons with the current order
        buttons = ["AC", "DEL", "√", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]
        row = 1
        col = 0

        # Adding input line to our grid
        grid.addWidget(input_line, 0, 0, 1, 4)

        # Adding buttons to grid
        for button in buttons:
            # Creating Button object for each button
            btn_object = Button(button, input_line)
            # Iterating over the buttons list and place them in 4 columns
            if col == 4:
                col = 0
                row += 1
            if button == 0:
                grid.addWidget(btn_object.button, row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(btn_object.button, row, col, 1, 1)
            col += 1


        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())

