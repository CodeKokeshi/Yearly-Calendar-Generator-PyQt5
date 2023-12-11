from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

import random

import os

import calendar

import sys

os.chdir(sys._MEIPASS) if getattr(sys, 'frozen', False) else os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CalendarUI(QMainWindow):

    def __init__(self):
        super(CalendarUI, self).__init__()
        uic.loadUi("Calendar.ui", self)

        self.setWindowIcon(QIcon('this.ico'))

        self.show()

        self.Field: QLineEdit = self.findChild(QLineEdit, 'Field')
        self.Show: QPushButton = self.findChild(QPushButton, 'Show')
        self.Random: QPushButton = self.findChild(QPushButton, 'Random')

        self.Field.textChanged.connect(self.checkField)
        self.Show.clicked.connect(self.showYear)
        self.Random.clicked.connect(self.Randomize)

    def Randomize(self):
        self.clearField()
        randomized = random.randint(100, 4000)
        self.Field.setText(str(randomized))

    def showYear(self):
        currentYear = self.Field.text()
        customDialog = QDialog()

        try:
            year_calendar = calendar.calendar(int(currentYear))
            text_edit = QTextEdit()
            text_edit.setFont(QFont("Courier New", 9))  # Use a monospaced font
            text_edit.setReadOnly(True)

            text_edit.setPlainText(year_calendar)

            layout = QVBoxLayout()
            layout.addWidget(text_edit)

            customDialog.setLayout(layout)
            customDialog.setWindowTitle("Year Calendar")

            # Set the fixed size for the custom dialog
            customDialog.setFixedSize(700, 700)

            self.clearField()
            customDialog.exec_()
        except ValueError:
            errorDialog = QMessageBox()
            errorDialog.setText("Please enter a valid year (integer).")

            self.clearField()
            errorDialog.exec_()

    def clearField(self):
        self.Field.clear()

    def checkField(self):
        if self.Field.text():
            self.enableShow()
        else:
            self.disableShow()

    def enableShow(self):
        self.Show.setEnabled(True)

    def disableShow(self):
        self.Show.setEnabled(False)

def main():
    app = QApplication([])
    app.setWindowIcon(QIcon('this.ico'))
    window = CalendarUI()
    app.exec_()

if __name__ == '__main__':
    main()