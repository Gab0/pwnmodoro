#!/bin/python

from time import sleep
from random import choice

import curses
import sys


numberbank = """
   _                  _             _                 _                  _______             _          _               _               _                _                
  / /\              /\ \          /\ \            _  /\ \               / ___  /\          /\ \       / /\            / /\            / /\             / /\          _    
 / /  \            /  \ \        /  \ \          /\_\\ \ \             / /\__\ \ \        /  \ \     / /  \          / /  \          / /  \           / /  \        /\_\  
/_/ /\ \          / /\ \ \      / /\ \ \        / / / \ \ \           / / /   \_\/       / /\ \_\   / / /\ \        / / /\ \        / / /\ \         / / /\ \       \/_/  
\_\/\ \ \         \/_/\ \ \    / / /\ \ \      / / /   \ \ \         / / /              / / /\/_/  / / /\ \ \      /_/ /\ \ \      /_/ /\ \ \       / / /\ \ \            
     \ \ \            / / /    \/_//_\ \ \     \ \ \____\ \ \        \ \ \             / /_/_     /_/ /  \ \ \     \ \ \_\ \ \     \ \ \_\ \ \     /_/ /  \ \ \           
      \ \ \          / / /       __\___ \ \     \ \________\ \        \ \ \           / /___/\    \_\/    \ \ \     \ \/__\ \ \     \ \/__\ \ \    \ \ \   \ \ \          
       \ \ \        / / /  _    / /\   \ \ \     \/________/\ \        \ \ \         / /\__ \ \            \ \ \     \_____\ \ \     \_____\ \ \    \ \ \   \ \ \     _   
      __\ \ \___   / / /_/\_\  / /_/____\ \ \              \ \ \   ____/ / /        / / /__\ \ \            \ \ \     \ \ \_\ \ \           \ \ \    \ \ \___\ \ \  /_/\  
     /___\_\/__/\ / /_____/ / /__________\ \ \              \ \_\ /_____/ /        / / /____\ \ \            \ \ \     \ \___\ \ \           \ \ \    \ \/____\ \ \ \_\/  
     \_________\/ \________/  \_____________\/               \/_/ \_____\/         \/__________\/             \_\/      \_______\/            \_\/     \_________\/       """

imagebank = ["""
               \                                     
               |.       /                            
   /|         ###.     /                             
  | \         `###._                                 
 /   \        / /|\ \     ___                        
/     `-._    | ~~   |                               
| ,-._    `|   `\___/                                
\/  | `-.__/            \         _     ,-.          
    /  /      /          \       / |   /  /          
 |\/  /\     /                  /  /  /  /   _       
 \ \_/ |        __             |   `-"   `.-" >      
.-`    .      ,'  `-.         /           _,-"       
`-.     `.    \   () `.   _,-'         ,-'           
 /` _     `-._ \ () /"\:-'              `-.._        
_/-/ `-._     `-+._(_ /     _,--.__,--,_.--._>       
\_/      `.        `-'   _."                         
           `\           |                            
             \          \     WHAT                   
              |  %i:%s   |                           
              \           \                          
               \           `.                        
                |    /`=._   \     THE               
                 \   \    `\  \                      
                  |   \      \/                      
                   `\  \_     A.                     
                     `\ _\    Hh.       FUCK         
                       ` A,   `HHh.                  
                         HH.   `HHHh                 
                         qHHb   `HHH.                
                          qHH.   HHHh                
                           qHHb.dHHH.                
                            "HHHHHHHHh               
                             ,HHHHHHHH.        dHD   
                            ,dHHHHHHHHHh.    ,dP     
                          ,dHHHHHHHHHHHHHHHHHHHHHHHHP
                         dHHP  `HHHH"   `HHHHHHHb.   
                    db  dHHP   dHHH'     :HH   `Hh.  
                    `HHHHH'   `HHHP       HH.   `Hh  
                      HHHH'     `"'        `HD     ` 
                      `HHHh.                `        
                          `Hh.,.                     
                            `HHHH                    
                       \.  ,dHHH'                    
                        HHHHHHH'                     
                         HHHHH'                      
                          "HHH                       
                      S-v   "V                       
""",
"""
                                                     .....
                                                    ..:-:....
                                                   ...:%+:::-..
                                                 .....:::**-:...
                                               .....::::**=-::...
                                            .......:=#=#@##+-*:....
                                         .........:::=#######-::......
                                       .......::::::-+#######=:::........
                                    .....:-==-:::=---=*#####=--::#::::::=..
                                  ......::+*#*#-=#################-::-:-=:..
                         %i:%s .........:::########################*####==..
                      ................:::--=%###########################::...
                   .................:::@##@###########################@-::...
                 ....:-::::::::::::::::-=###############################-:::.
                ....::%-:@::==::::::::-@##################################%:.
               .....:::-+##==##+*=-::-###################################-:..
            .......::::=*##########===####################################+:.
        ........:::::-+#############@+###################################-:..
    ...........::-=-==%##################################################:...
 ....:-::::::::::=*#####################################################::...
:::-::#-:-=-=-=%+@####################################################-::....
 .....:....::::::-+#####################################################::...
     ..........::=---=%##############@###################################::..
         ........::::++*############*+###################################-:..
             ......::::**##########=-=####################################+:.
               .....:::-**#==*#=#-:::-+##################################-::.
                 ...:==:::::-=::::::::=###################################@*.
                  ...:=::...::::.::::::-*###############################-:::.
                   ..................::+#@+###########################+-::...
                        ..............::::-=############################*:...
                                ........:::########################=%#@#+:..
                                  .......:-#*==-=##############+##-::::-=:..
                                     ....:::--::::::-=######=-::::::...::..
                                       .........::::=@#######=:::........
                                          ........:::+######%=::.....
                                             ......::=-=@##=:::....
                                                .....:::-*=:::...
                                                  ....::-=@=:...
                                                   ...::%::.:..
                                                    ..:-:...
                                                      ...
""",
"""
                           _ooOoo_
                          o8888888o
                          88     88
                          (| -_- |)
                          O\  =  /O
                       ____/`---'\____
                     .'  \\|     |//  `.
                    /  \\|||  :  |||//  \\
                   /  _||||| -:- |||||_  \\
                   |   | \\\\  -  /'| |   |
                   | \\_|  `\\`---'//  |_/ |
                   \  .-\__ `-. -'__/-.  /
                 ___`. .'  /--.--\  `. .'___
              ."" '<  `.___\_<|>_/___.' _> \\"".
             | | :  `- \`. ;`. _/; .'/ /  .' ; |
             \  \ `-.   \_\_`. _.'_/_/  -' _.' /    %i:%s
   ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
                           `=--=-'                    
""",
"""
                                                                      ..;===+.
                                                                  .:=iiiiii=+=
                                                               .=i))=;::+)i=+,
                                                            ,=i);)I)))I):=i=;
                                                         .=i==))))ii)))I:i++
                          %i:%s                        +)+))iiiiiiii))I=i+:'
                                  .,:;;++++++;:,.       )iii+:::;iii))+i='
                               .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                             ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                           ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                          ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                        ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                       ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                      ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                      =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                     +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                     =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                    .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                    :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                    :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                    .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                    =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                  +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
                +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
               =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
             +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
           :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
         .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
        ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
       +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
     .+=:))iiiiiiii)))+ii;
    .+=;))iiiiii)));ii+
   .+=i:)))))))=+ii+
  .;==i+::::=)i=;
  ,+==iiiiii+,
  `+=+++;`
"""
]

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
