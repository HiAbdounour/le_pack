from common import *
from random import choice as ch

# LEVEL BUILDING

VALID_WORDS = []
alpha = alison("ALPHA")
CLR_LETTERS = {chr:PYGAME_GRAY for chr in alpha}

def build_specific_level(lvl):
    for j in range(6):
        for i in range(lvl):
            draw_rectangle(Point(100+i*55,50+j*55),50,50,pygame.Color(60,60,60),1)
    return

def build_check_letters():
    global alpha
    for i in range(len(alpha)):
        draw_rectangle(Point(80+(i%13)*30,400+(i//13)*30),25,25,PYGAME_GRAY,1)
        display_text(alpha[i],coord=(80+(i%13)*30-8,375+(i//13)*30+10),font=("Verdana",20),text_bold=True)

def choose(lvl):
    global VALID_WORDS
    with open(f"ressources/mots{lvl}.txt",'r') as file:
        data = file.readlines()
        data = [elem[:len(elem)-1] for elem in data]
    VALID_WORDS = data
    return ch(data)

def build_level(lvl):
    clear_window(PYGAME_GREY)
    build_specific_level(lvl)
    build_check_letters()
    return choose(lvl)

def print_menu():
    display_text("Le Mot",("Comic sans MS",90),(95,80),text_bold=True)
    buttons_list = []
    for i in range(3,7):
        display_text("Jouer avec des mots de",("Comic sans MS",25),(105,230),text_bold=True)
        display_text("lettres",("Comic sans MS",25),(205,330),text_bold=True)
        b = Button(i,(100*(i-2),300,pygame.Color(60,60,60)),(50,50),(str(i),100*(i-2)-13,275,PYGAME_WHITE))
        buttons_list.append(b)
        b.display()
    return buttons_list

def choice_level(list_buttons,pos):
    for b in list_buttons:
        if b.is_clicked(pos)!=-1:
            return b.is_clicked(pos)
    return -1

# PLAYING

def update_status(letter,clr):
    global CLR_LETTERS,alpha
    if CLR_LETTERS[letter]==PYGAME_GRAY:
        CLR_LETTERS[letter] = clr
    elif CLR_LETTERS[letter]==PYGAME_ORANGE and clr!=PYGAME_GRAY:
        CLR_LETTERS[letter] = clr
    else:
        return
    i = alpha.index(letter)
    draw_rectangle(Point(80+(i%13)*30,400+(i//13)*30),25,25,CLR_LETTERS[letter],1)
    display_text(alpha[i],coord=(80+(i%13)*30-8,375+(i//13)*30+10),font=("Verdana",20),text_bold=True)
    return

def check(guess,real,ongoing_try):
    dico = {elem:real.count(elem) for elem in real}
    ongoing_try-=1
    n = len(real)
    for i in range(n):
        if guess[i]==real[i]:
            dico[guess[i]]-=1
            draw_rectangle(Point(100+i*55,50+(ongoing_try//n)*55),50,50,PYGAME_GREEN,1)
            display_text(guess[i],("Verdana",32),(100-10+(i%n)*55,50-20+(ongoing_try//n)*55),text_bold=True)
            update_status(guess[i],PYGAME_GREEN)

    for i in range(n):
        if guess[i]==real[i]:
            continue
        elif guess[i]!=real[i] and guess[i] in real and dico[guess[i]]>0:
            clr = PYGAME_ORANGE
            dico[guess[i]]-=1
            update_status(guess[i],PYGAME_ORANGE)
        else:
            clr = pygame.Color(60,60,60)
            update_status(guess[i],pygame.Color(60,60,60))
        draw_rectangle(Point(100+i*55,50+(ongoing_try//n)*55),50,50,clr,1)
        display_text(guess[i],("Verdana",32),(100-10+(i%n)*55,50-20+(ongoing_try//n)*55),text_bold=True)
    
    del dico
    if guess==real:
        return True
    return False

# GAME :: Le Mot
def choose_menu():
    lvl_choices = print_menu()
    lvl = -1
    while lvl==-1:
        lvl = choice_level(lvl_choices,wait_clic())
    play(build_level(lvl))
    return False

def play(chosen_word):
    global alpha, VALID_WORDS, CLR_LETTERS
    actual_word = ""
    i = 0
    n = len(chosen_word)
    finished = False
    found = False
    while not finished:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # in case of
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                k = pygame.key.name(event.key).upper()
                # normal flow
                if k in alpha and len(actual_word)!=n:
                    display_text(k,("Verdana",32),(100+(i%n)*55-10,50-20+(i//n)*55),text_bold=True)
                    i+=1
                    actual_word += k
                # erase a letter
                elif k == "BACKSPACE" and actual_word!="":
                    i-=1
                    draw_rectangle(Point(100+(i%n)*55,50+(i//n)*55),50,50,pygame.Color(60,60,60),1)
                    actual_word = actual_word[:len(actual_word)-1]
                # verify a word
                elif k == "RETURN" and len(actual_word)==len(chosen_word):
                    if actual_word in VALID_WORDS:
                        found = check(actual_word,chosen_word,i)
                        actual_word=""
                    else:
                        display_text("Mot non reconnu",("Verdana",32),(50,450),text_bold=True,clr=PYGAME_RED)
                        pygame.time.delay(2000)
                        display_text("Mot non reconnu",("Verdana",32),(50,450),text_bold=True,clr=PYGAME_GRAY)
                # others
                else:
                    continue
        
        # found
        if found:
            finished = True
        # all tries used
        if i//n==6 and actual_word=="":
            finished = True
            # reveal word
            display_text(chosen_word,("Verdana",32),(100,450),clr=PYGAME_BLUE,text_bold=True)
    
    # end
    pygame.time.delay(3000)
    # reset for next match
    VALID_WORDS = []
    CLR_LETTERS = {chr:PYGAME_GRAY for chr in alpha}

    return
