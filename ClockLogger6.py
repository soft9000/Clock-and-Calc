#!/usr/bin/env python3

# File: LoggerClock6.py
# Mission: Demonstrate how to create a graphically distinctive clock using QT6. Accept + save 
# time-stamped entries into a daily, file-date-named UTF-8 ('zlog') format.

# Rev: 1.0

# NOTE: pip3 install PyQt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QInputDialog, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer, QDateTime, QTime, Qt

class LoggerClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time = None
        self.setWindowTitle("Log 'o Clock")
        self.resize(240,0)
        self.setStyleSheet("background-color: Gold")
        self.setWindowFlags(Qt.WindowType.Window|Qt.WindowType.WindowStaysOnTopHint)

        layout = QGridLayout()

        self.lblTmDisplay = QLabel()
        self.lblTmDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTmDisplay.setFont( QFont('Courier', 22))
        self.lblTmDisplay.setStyleSheet('Color: Green;font-weight: bold;')

        self.lblDateDisplay = QLabel()
        self.lblDateDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblDateDisplay.setFont( QFont('Helvetica', 12))
        self.lblDateDisplay.setStyleSheet('Color: Gold;background-color: Black')

        self.btnLog = QPushButton('Note')
        self.btnLog.setFont( QFont('Helvetica', 14))
        self.btnLog.setStyleSheet('Color: Blue;background-color: White')
        self.btnLog.clicked.connect(self.doLog)

        layout.addWidget(self.lblDateDisplay,1,0)
        layout.addWidget(self.lblTmDisplay,2,0)
        layout.addWidget(self.btnLog, 3,0)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # per second

        self.showTime()

    def showTime(self):
        self.time = QDateTime.currentDateTime()
        self.lblTmDisplay.setText(self.time.toString('hh:mm:ss A'))
        self.lblDateDisplay.setText(self.time.toString('MM/dd yyyy (dddd)'))
    
    def doLog(self):
        text, bok = QInputDialog.getText(self, self.lblTmDisplay.text(), "Log entry:")
        if bok:
            import logging
            dfn = self.time.toString('yyyy-MM-dd-dddd')
            logging.basicConfig(filename=f'{dfn}.zlog', encoding='utf-8', level=logging.INFO,
                format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.log(msg=text, level=logging.INFO)



if __name__ == '__main__':
    z_app = QApplication(sys.argv)
    a_clock = LoggerClock()
    a_clock.show()
    z_app.exit(z_app.exec())
