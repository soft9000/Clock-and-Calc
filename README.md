# Clock-and-Calc

This project offers wee geeks a place to "grow" some clock & calculator ideas.

The effort began with sharing my classic / previously shared [Tkinter clock](https://github.com/soft9000/Clock-and-Calc/blob/main/BasicClock.py):

![BASELINE](https://github.com/soft9000/Clock-and-Calc/blob/main/_graphics/Baseline.png)

Notes:
* Tkinter is usually part of Python's Core 'battery pack.'
* This `BasicClock` simply shows the same. Logging (like the below) comming soon?
* Tkinter is presently problematic (read: "Yikes") on macOS.

Since Qt5 presently works better than Tkinter on the macOS, I cobbled [LoggerClock](https://github.com/soft9000/Clock-and-Calc/blob/main/ClockLogger.py) for us all to enjoy:

![BASELINE](https://github.com/soft9000/Clock-and-Calc/blob/main/_graphics/LoggerClock.png)

Notes: The above `ClockLogger`:
* Uses Qt5 (`pip3 install PyQt5`)
* Uses Python's core logging facility.
* Belogs time-stamped notes in UTF-8 Format.
* The default log file is pw-day date-named.
* Log files are suffixed with a `.zlog` to help with aggregation(s.)

Notes: The `ClockLogger6`:
* Uses Qt6 (`pip3 install PyQt6`)
* Demonstrates why PyQt6 is easier, yet breaks PyQt5.
* Font-mapper carps a lot on macOS!

-- Enjoy!




