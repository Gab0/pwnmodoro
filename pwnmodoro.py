#!/bin/python

from time import sleep
from random import choice
import curses
from ASCII_ART import *
import sys


def detectNumberSplits(NB):
    W = NB.split('\n')
    W = [x for x in W if x]
    SEPP = []
    for x in range(len(W[0])):
        G=True
        for z in range(len(W)):
            try:
                if W[z][x] != ' ':
                    G=False

            except:
                print("err "+str(x))

        if G:
            SEPP.append(x)
    print(SEPP)
    if SEPP[0] > 5:
        SEPP=[0]+SEPP
    MAP =[]
    for A in range(len(SEPP)-1):
        if SEPP[A+1] - SEPP[A] > 3:
            MAP.append([SEPP[A], SEPP[A+1]])
    return MAP

def constructNumbers(NB, MAP):
    Numbers = []
    W = NB.split('\n')
    W = [x for x in W if x]
    for K in range(len(MAP)):
        print(MAP[K][0])
        print(MAP[K][1])
        N = [ x[MAP[K][0]:MAP[K][1]] for x in W]
        Numbers.append(N)
    # numberbank input should be a great panel written "0123456789:" in ASCII;
    for C in Numbers:
        S(C)
    return Numbers

def S(q):
    for x in q:
        print(x)

def fix():
    import subprocess
    subprocess.call(['stty', 'sane'])

    


IMG = choice(imagebank).split('\n')


curses.setupterm()
graphictimer = curses.initscr()
graphictimer.refresh()
graphictimer.nodelay(1)

PAUSED = 0
PAUSE_BUTTONS = ['p', ' ', 'P']
PAUSE_BUTTONS = [ord(x) for x in PAUSE_BUTTONS]

QUIT_BUTTONS = ['c', 'q', 'C', 'Q']
QUIT_BUTTONS = [ord(x) for x in QUIT_BUTTONS]

def TIMER(stdscr, MINUTES, IMG, COLOR):
    global PAUSED
    for M in range(MINUTES-1, -1, -1):
        seconds = 60
        while seconds:
            JustPaused = False
            try:
                sleep(1)
            except KeyboardInterrupt:
                exit()

            KeyPressed = graphictimer.getch()
            if KeyPressed in PAUSE_BUTTONS:
                PAUSED = 1-PAUSED
                JustPaused = 1
            elif KeyPressed in QUIT_BUTTONS:
                exit()
            if PAUSED and not JustPaused:
                continue
                
            seconds -=1
            if not seconds % 1:
                screenH, screenW = graphictimer.getmaxyx()
                SHOW = "%i:%s" % (M, str(seconds).zfill(2))
                graphictimer.clear()

                if len(IMG) > screenH:
                    center = len(IMG)//2
                    V = screenH//2
                    LIM=[center-V, center+V]
                else:    
                    LIM = [0, len(IMG)]
                    
                LINE=0
                for K in range(LIM[0], LIM[1]):
                    imageline = IMG[K][:screenW]
                    if "%i:%s" in IMG[K]:
                        #print(z)
                        imageline = imageline % (M, str(seconds).zfill(2) )

                    if K - LIM[0] <= screenH:
                        try:
                            _color = 6 if PAUSED else COLOR
                            graphictimer.addstr(LINE, 0,
                                    imageline, curses.color_pair(_color))
                        except:
                            pass
                        LINE+=1
                graphictimer.refresh()
                # print (SHOW )


    print("*** TIME'S UP ***")



def TimerQueuer(times):
    Welcome = """ 
starting tomato timer;; 
                     for %i minutes.
%s
%sp or spacebar to pause;
%sq or c to quit;
""" % (times[0],
       "\n"*16, " "*28," "*32)
       


    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    try:        
        graphictimer.addstr(12,12, Welcome, curses.color_pair(4))
    except:
        pass
    graphictimer.refresh()

    COLORS=[2,3] #Red and Green
    for I in range(len(times)):
        curses.wrapper(TIMER, times[I], IMG, COLORS[I%2]) 

if __name__ == '__main__':

    # customized timer-values run.
    if len(sys.argv) > 1:
        try:
            T = [ int(G) for G in sys.argv[1:] ]
            TimerQueuer(T)
        except:
            if "r" in sys.argv:
                TimerQueuer([15,5])
                exit()

    # standard run.
    else:            
        TimerQueuer([25,5])

