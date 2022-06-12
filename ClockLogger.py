#!/usr/bin/env python3

# File: LoggerClock.py
# Mission: Demonstrate how to create a graphically distinctive clock using QT5. Accept + save 
# time-stamped entries into a daily, file-date-named UTF-8 ('zlog') format.

# Rev: 1.0

# NOTE: pip3 install PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QInputDialog, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QDateTime, QTime, Qt

class LoggerClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time = None
        self.setWindowTitle("Log 'o Clock")
        self.resize(0,0)

        layout = QGridLayout() # QVBoxLayout()

        self.lblTmDisplay = QLabel()
        self.lblTmDisplay.setAlignment(Qt.AlignCenter)
        self.lblTmDisplay.setFont( QFont('Open Sans', 22, QFont.Bold))
        self.lblTmDisplay.setStyleSheet('Color: Green')

        self.lblDateDisplay = QLabel()
        self.lblDateDisplay.setAlignment(Qt.AlignCenter)
        self.lblDateDisplay.setFont( QFont('Open Sans', 12))
        self.lblDateDisplay.setStyleSheet('Color: Blue')

        self.btnLog = QPushButton('Note')
        self.btnLog.setFont( QFont('Open Sans', 14))
        self.btnLog.setStyleSheet('Color: Blue')
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
            dfn = self.time.toString('dddd-yyyy-MM-dd')
            logging.basicConfig(filename=f'{dfn}.zlog', encoding='utf-8', level=logging.INFO,
                format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.log(msg=text, level=logging.INFO)



if __name__ == '__main__':
    z_app = QApplication(sys.argv)
    a_clock = LoggerClock()
    a_clock.show()
    z_app.exit(z_app.exec_())
