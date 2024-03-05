# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import *
from PySide6.QTCore import Slot

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_Widget



#class Widget(QWidget):
#    def __init__(self, parent=None):
#        super().__init__(parent)
#        self.ui = Ui_Widget()
#        self.ui.setupUi(self)


#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    widget = Widget()
#    widget.show()
#    sys.exit(app.exec())

#Greetings

@Slot()
def sayHello():
    print("Hello Button Clicker!")

# Create Application
app = QApplication(sys.argv)

# Create Button
QPushButton("Click Me!! ")

# Connect the button to the function
button.clicked.connect(sayHello)

# Show the button
button.show()

# Run the main QT Loop
app.exec()

