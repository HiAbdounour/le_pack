import pygame

from common import *
from random import randint as rdt

DIFFICULTY = 4
MEMO_I,MEMO_J = 5,0

def change_difficulty(diff):
    global DIFFICULTY
    DIFFICULTY = diff
    return

def reset_memos():
    global MEMO_I,MEMO_J
    MEMO_I,MEMO_J = 5,0
    return

def build_level():
    for i in range(DIFFICULTY):
        draw_rectangle(Point(70+i*120,200),100,100,pygame.Color(60,60,60),1)
    return

def choice_level(list_buttons,pos):
    for b in list_buttons:
        if b.is_clicked(pos)!=-1:
            return b.is_clicked(pos)
    return -1

def build_menu():
    display_text("Le Nombre",("Comic sans MS",90),(15,80),text_bold=True)
    display_text("Chercher des nombres de",("Comic sans MS",25),(105,230),text_bold=True)
    display_text("chiffres",("Comic sans MS",25),(205,330),text_bold=True)
    buttons_list = []
    for i in range(3,7):
        b = Button(i-2,(100*(i-2),300,pygame.Color(60,60,60)),(50,50),(str(i-2),100*(i-2)-13,275,PYGAME_WHITE))
        buttons_list.append(b)
        b.display()
    bq = Button(0,(250,400,pygame.Color(60,60,60)),(50,50),('<-',230,375,PYGAME_WHITE))
    bq.display()
    buttons_list.append(bq)
    return buttons_list

def choose_number():
    return rdt(1,10**DIFFICULTY-1)


def press_key(k):
    if k=="backspace": # for erasing
        return 10
    if k=="return": # for validating
        return 20
    try:
        k = int(k) # if works, means key is CAPS LOCK NUMBER
        # after testing, it seems to work regardless CAPS LOCK activation
        return k
    except Exception:
        try:
            k = int(k[1]) # if works, means key is a NUMBER from NUMPAD
            return k
        except Exception:
            return -1
        
def print_key_at_i(nb,i):
    if 0<=nb<=9 and i<DIFFICULTY:
        display_text(str(nb),('Verdana',96),(35+i*120,140),text_bold=True)
        return i+1
    if nb==10 and i!=0:
        erase_at_i(i-1)
        return i-1
    return -1 # means do nothing

def erase_at_i(i):
    draw_rectangle(Point(70+i*120,200),100,100,PYGAME_GRAY,1)


# GAME : Le Nombre
def play():
    lvl_list = build_menu()
    lvl = -1
    while lvl==-1:
        lvl = choice_level(lvl_list,wait_clic())
    if lvl==0:
        return True
    change_difficulty(lvl)
    clear_window(PYGAME_GRAY)
    reset_memos()

    nb = choose_number()
    found = False
    cpt = 0
    while not found:
        found = logic(nb)
        cpt+=1
    add_pts((lvl-1)*10+3-cpt)
    pygame.time.delay(1000)
    return False


def logic(chosen_nb):
    guess_nb = ""
    i=0
    check = False
    while not check:

        for event in pygame.event.get():
            # in case of
            if event.type==pygame.QUIT:
                pygame.quit()
                return

            if event.type==pygame.KEYDOWN:
                k = press_key(pygame.key.name(event.key))
                if k!=-1 and k!=20:
                    i_ = print_key_at_i(k,i)
                    # something wrong happened
                    if i_==-1:
                        pass
                    # erasing
                    elif i_<i:
                        i = i_
                        guess_nb = guess_nb[:len(guess_nb)-1]
                    # completing
                    elif i_>i:
                        i = i_
                        guess_nb = guess_nb+str(k)
                    # otherwise
                    else:
                        pass
                elif k==20 and i==DIFFICULTY:
                    for m in range(DIFFICULTY):
                        erase_at_i(m)
                    check = True
    memorise(guess_nb,chosen_nb)
    return int(guess_nb)==chosen_nb

def memorise(guess_nb,chosen_nb):
    global MEMO_I,MEMO_J
    clr = PYGAME_GREEN
    if int(guess_nb)<chosen_nb:
        clr = PYGAME_RED
    elif int(guess_nb)>chosen_nb:
        clr = PYGAME_BLUE

    display_text(guess_nb,("Verdana",18),(MEMO_I,MEMO_J),clr,True)
    MEMO_I += 55
    if MEMO_I>=455:
        MEMO_I = 5
        MEMO_J+=20
    if 130<=MEMO_J<=250:
        MEMO_J = 270   