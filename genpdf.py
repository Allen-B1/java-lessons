from selenium import webdriver
import time
from selenium.webdriver import firefox
from evdev import uinput, ecodes
import threading
import os

class PrintBrowser:
    def __init__(self): pass

    def print(self, url, output):
        try:
            os.remove(output)
        except: pass

        opts = firefox.options.Options()
        opts.set_preference("print.print_to_file", True)
        opts.set_preference("print.print_to_filename", output)
        for option in ["print.print_footerleft", "print.print_footerright", "print.print_footercenter", "print.print_headerleft", "print.print_headerright"]:
            opts.set_preference(option, "")

        driver = webdriver.Firefox(options=opts)
        driver.get(url)

        time.sleep(1)

        threading.Thread(target=driver.execute_script, args=("window.print()",)).start()

        with uinput.UInput() as ui:
            ui.write(ecodes.EV_KEY, ecodes.KEY_TAB, 1)
            ui.write(ecodes.EV_KEY, ecodes.KEY_TAB, 0)
            for i in range(12):
                ui.write(ecodes.EV_KEY, ecodes.KEY_UP, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_UP, 0)
            ui.syn()

            time.sleep(0.5)

            ui.write(ecodes.EV_KEY, ecodes.KEY_ENTER, 1)
            ui.write(ecodes.EV_KEY, ecodes.KEY_ENTER, 0)
            ui.syn()
        
        time.sleep(3)

        driver.close()

import pathlib

folder = str(pathlib.Path(__file__).parent.absolute())
files = os.listdir(folder + "/html")

browser = PrintBrowser()
for file in files:
    browser.print("file://" + folder + "/html/" + file, folder + "/pdf/" + file[:-5] + ".pdf")
