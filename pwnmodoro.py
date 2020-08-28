#!python3

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
                pass
                #print("err "+str(x))

        if G:
            SEPP.append(x)
    if SEPP[0] > 3:
        SEPP=[0]+SEPP
    SEPP += [len(W[0])]
    MAP =[]
    for A in range(len(SEPP)-1):
        if SEPP[A+1] - SEPP[A] > 2:
            MAP.append([SEPP[A], SEPP[A+1]])
    return MAP

def constructNumbers(NB, MAP):
    Numbers = []
    W = NB.split('\n')
    W = [x for x in W if x]
    for K in range(len(MAP)):
        N = [ x[MAP[K][0]:MAP[K][1]] for x in W]
        Numbers.append(N)
    # numberbank input should be a great panel,
    # written "0123456789:" in ASCII;
    # a full column of spaces should stand between each
    # number!
    
    #for C in Numbers:
    #    S(C)
    #numbers = ['\n'.join(x) for x in Numbers]
    return Numbers

def mountASCIIClock(NB, TIME="12:13"):
    MOUNT = ["" for x in range(len(NB[0])) ]
    for DIG in TIME:
        try:
            DIG=int(DIG)
        except:
            DIG=10
        for W in range(len(NB[DIG])):
            num=NB[DIG]
            MOUNT[W] += num[W]


    #return '\n'.join(MOUNT)
    return MOUNT

def selectMinimalWidthAmongFonts(nbBANK, screenWidth):
    nblens = [0] + list(nbBANK.keys())
    nblens.sort()
    for w in range(1, len(nblens)):
        if screenWidth < nblens[w]:
            return nblens[w-1]
    return nblens[-1]
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

def TIMER(stdscr, MINUTES, IMG, COLOR, BigClockMode=True):
    global PAUSED
    if BigClockMode:
        NUMBs = {} #final structure:  {<min width>: NUMBERLIST, ... }
        for nBANK in numberbank:
            NumberKit = nBANK
            MAP = detectNumberSplits(NumberKit)
            NUMB = constructNumbers(NumberKit, MAP)
            # length of four digits and ':' of a font.
            pxWidth = len(NUMB[0][0]) * 4 + len(NUMB[-1][0]) 
            NUMBs.update({pxWidth: NUMB})
            
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
            screenH, screenW = graphictimer.getmaxyx()
            if BigClockMode:
                SHOW = "%i:%s" % (M, str(seconds).zfill(2))
                nbSIZE = selectMinimalWidthAmongFonts(NUMBs, screenW)
                if screenW > 5:
                    if nbSIZE:
                        IMG = mountASCIIClock(NUMBs[nbSIZE], TIME=SHOW)
                    else:
                        IMG = [SHOW]
                else:
                    IMG = SHOW
                    
            IMGsize = len(IMG[0]), len(IMG)
            
            # UPDATE SCREEN ROUTINES;
            if not seconds % 1:
                graphictimer.clear()
                    
                # CENTER IMAGE ON TERMINAL WINDOW;
                center = len(IMG)//2
                if len(IMG) > screenH:
                    V = screenH//2
                    LIM=[center-V, center+V]
                    centerize= 0,0

                else:
                    centerize = (screenW-IMGsize[0])//2,\
                                (screenH-IMGsize[1])//2
                    LIM = [0, len(IMG)]
                    
                # DRAW METHOD;
                drawImageStandard(graphictimer, IMG, LIM,
                                  [screenW, screenH], centerize, COLOR)
                
    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OLD METHOD ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    LINE=centerizeH
    for K in range(LIM[0], LIM[1]):
        imageline = IMG[K][:screenW-centerizeW]
        if "%i:%s" in IMG[K]:
            imageline = imageline % (M, str(seconds).zfill(2) )

        if K - LIM[0] <= screenH:
            try:
                _color = 6 if PAUSED else COLOR
                graphictimer.addstr(LINE, centerizeW,
                        imageline, curses.color_pair(_color))
            except:
                for S in range(len(imageline)): # PANIC ROTATE 90ºCCW ;}
                    try:
                        graphictimer.addstr(centerizeW+K, centerizeH+S,
                                        imageline[S], curses.color_pair(6))
                    except:
                        pass
                pass
            LINE+=1
    graphictimer.refresh()
    # print (SHOW )
    '''

    print("*** TIME'S UP ***")

def drawImageStandard(SCREEN, IMAGE, lineInterval,
                      screenSize, offset, color):
    LINE = offset[1]
    for K in range(*lineInterval):
        imageline = IMAGE[K][:screenSize[0]-offset[0]]
        if "%i:%s" in IMAGE[K]: #DEPRECATED
            pass
            #imageline = imageline % (M, str(seconds).zfill(2) )

        if K - lineInterval[0] <= screenSize[1]:
            try:
                _color = 6 if PAUSED else color
                SCREEN.addstr(LINE, offset[0],#<????
                        imageline, curses.color_pair(_color))
            except:
                pass

            LINE+=1
    SCREEN.refresh()   

def drawImageSkewed():
    # TODO; ROTATE 90ºCCW/VERTICAL CLOCK.
    pass

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

