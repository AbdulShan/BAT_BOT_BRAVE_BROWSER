import time
import os
import webbrowser
from easygui import *
from pynput.keyboard import Key, Controller

keyboard = Controller()

from pynput.mouse import Button, Controller

mouse = Controller()

def scroll():
    l=0
    while l<15:
        time.sleep(0.1)
        mouse.scroll(0,-1)
        l=l+1
    time.sleep(1)

def maximise():
    time.sleep(0.7)
    keyboard.press(Key.cmd)
    keyboard.press(Key.up)
    keyboard.release(Key.cmd)
    keyboard.release(Key.up)

def close_brow():
    time.sleep(1)
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)
    time.sleep(1)
    keyboard.press(Key.alt_l)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.f4)

def tab():
    time.sleep(0.04)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

def del_tab():
    time.sleep(0.7)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)

def new_tab():
    time.sleep(1)
    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)

def reload_n_noti():
    i=0
    time.sleep(1)
    while i<35:
        time.sleep(0.2)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.2)
        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        time.sleep(0.2)
        keyboard.press(Key.cmd_l)
        keyboard.press(Key.shift_l)
        keyboard.press('v')
        keyboard.release(Key.cmd_l)
        keyboard.release(Key.shift_l)
        keyboard.release('v')
        time.sleep(0.2)
        keyboard.press(Key.delete)
        keyboard.release(Key.delete)
        i=i+1
    time.sleep(1)
    
def enter():
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def new_prof():
    time.sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift_l)
    keyboard.press('m')
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift_l)
    keyboard.release('m')
    time.sleep(1)

def refresh():
    new_tab()
    reload_n_noti()
    mouse.position = (1049, 538)
    scroll()
    scroref()
    del_tab()

def en_re_clo():
    enter()
    maximise()
    refresh()
    close_brow()

def action():
    time.sleep(3)
    webbrowser.open('www.duckduckgo.com')#0
    del_tab()
    maximise()
    refresh()

    new_prof()#1
    maximise()
    en_re_clo()

    new_prof()#2
    maximise()
    tab()
    en_re_clo()

    new_prof()#3
    maximise()
    for i in range(2):
        tab()
    en_re_clo()

    new_prof()#4
    maximise()
    for i in range(3):
        tab()
    en_re_clo()

    new_prof()#5
    maximise()
    for i in range(4):
        tab()
    en_re_clo()

    new_prof()#6
    maximise()
    for i in range(5):
        tab()
    en_re_clo()

    new_prof()#7
    maximise()
    for i in range(6):
        tab()
    en_re_clo()

    new_prof()#8
    maximise()
    for i in range(7):
        tab()
    en_re_clo()

    new_prof()#9
    maximise()
    for i in range(8):
        tab()
    en_re_clo()

    new_prof()#10
    maximise()
    for i in range(9):
        tab()
    en_re_clo()

    new_prof()#11
    maximise()
    for i in range(10):
        tab()
    en_re_clo()

    new_prof()#12
    maximise()
    for i in range(11):
        tab()
    en_re_clo()

    new_prof()#13
    maximise()
    for i in range(12):
        tab()
    en_re_clo()

    new_prof()#14
    maximise()
    for i in range(13):
        tab()
    en_re_clo()

    new_prof()#15
    maximise()
    for i in range(14):
        tab()
    en_re_clo()

    new_prof()#16
    maximise()
    for i in range(15):
        tab()
    en_re_clo()

    new_prof()#17
    maximise()
    for i in range(16):
        tab()
    en_re_clo()

    new_prof()#18
    maximise()
    for i in range(17):
        tab()
    en_re_clo()

    new_prof()#19
    maximise()
    for i in range(18):
        tab()
    en_re_clo()

    new_prof()#20
    maximise()
    for i in range(19):
        tab()
    en_re_clo()

    new_prof()#21
    maximise()
    for i in range(20):
        tab()
    en_re_clo()

    new_prof()#22
    maximise()
    for i in range(21):
        tab()
    en_re_clo()

    new_prof()#23
    maximise()
    for i in range(22):
        tab()
    en_re_clo()

    new_prof()#24
    maximise()
    for i in range(23):
        tab()
    en_re_clo()

    new_prof()#25
    maximise()
    for i in range(24):
        tab()
    en_re_clo()

    new_prof()#26
    maximise()
    for i in range(25):
        tab()
    en_re_clo()

    new_prof()#27
    maximise()
    for i in range(26):
        tab()
    en_re_clo()

    new_prof()#28
    maximise()
    for i in range(27):
        tab()
    en_re_clo()

    new_prof()#29
    maximise()
    for i in range(28):
        tab()
    en_re_clo()

    new_prof()#30
    maximise()
    for i in range(29):
        tab()
    en_re_clo()

    new_prof()#31
    maximise()
    for i in range(30):
        tab()
    en_re_clo()

    new_prof()#32
    maximise()
    for i in range(31):
        tab()
    en_re_clo()

    new_prof()#33
    maximise()
    for i in range(32):
        tab()
    en_re_clo()

    new_prof()#34
    maximise()
    for i in range(33):
        tab()
    en_re_clo()

    new_prof()#35
    maximise()
    for i in range(34):
        tab()
    en_re_clo()

    new_prof()#36
    maximise()
    for i in range(35):
        tab()
    en_re_clo()

    new_prof()#37
    maximise()
    for i in range(36):
        tab()
    en_re_clo()

    new_prof()#38
    maximise()
    for i in range(37):
        tab()
    en_re_clo()

    new_prof()#39
    maximise()
    for i in range(38):
        tab()
    en_re_clo()

    new_prof()#40
    maximise()
    for i in range(39):
        tab()
    en_re_clo()

    new_prof()#41
    maximise()
    for i in range(40):
        tab()
    en_re_clo()

    new_prof()#42
    maximise()
    for i in range(41):
        tab()
    en_re_clo()

    new_prof()#43
    maximise()
    for i in range(42):
        tab()
    en_re_clo()

    new_prof()#44
    maximise()
    for i in range(43):
        tab()
    en_re_clo()

    new_prof()#45
    maximise()
    for i in range(44):
        tab()
    en_re_clo()

    new_prof()#46
    maximise()
    for i in range(45):
        tab()
    en_re_clo()

    new_prof()#47
    maximise()
    for i in range(46):
        tab()
    en_re_clo()

    new_prof()#48
    maximise()
    for i in range(47):
        tab()
    en_re_clo()

    new_prof()#49
    maximise()
    for i in range(48):
        tab()
    en_re_clo()

    new_prof()#50
    maximise()
    for i in range(49):
        tab()
    en_re_clo()

msg = "BAT BOT"
title = "Choose an Option"
choices = ["Refresh Only", "2-4 Ads and Refresh","4-6 Ads and Refresh", "10 Ads and Refresh"]
choice = choicebox(msg, title, choices)
if choice == choices[0]:           
    def scroref():
        i=0
    action()
elif choice == choices[1]:
    def scroref():
        i=0
        time.sleep(0.2)
        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        time.sleep(15)
        scroll()
        while i<4:
            time.sleep(2)
            keyboard.press(Key.ctrl)
            keyboard.press('r')
            keyboard.release('r')
            keyboard.release(Key.ctrl)
            i=i+1
        time.sleep(1)                         
    action()
elif choice == choices[2]:
    def scroref():
        i=0
        time.sleep(0.2)
        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        time.sleep(15)
        scroll()
        while i<6:
            time.sleep(2)
            keyboard.press(Key.ctrl)
            keyboard.press('r')
            keyboard.release('r')
            keyboard.release(Key.ctrl)
            i=i+1
        time.sleep(1)     
    action()
elif choice == choices[3]: 
    def scroref():
        i=0
        time.sleep(0.2)
        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        time.sleep(15)
        scroll()
        while i<10:
            time.sleep(2)
            keyboard.press(Key.ctrl)
            keyboard.press('r')
            keyboard.release('r')
            keyboard.release(Key.ctrl)
            i=i+1
        time.sleep(1)                              
    action()

#time.sleep(10)
#close_brow()
#close_brow()
#os.system('shutdown -s')