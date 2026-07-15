from common import init_graphic, clear_window, display_text, wait_clic
from common import Button
from common import PYGAME_GRAY, PYGAME_WHITE
from typing import Callable # just for avoid typing warning

from le_mot.game import choose_menu as playLeMot
from le_nombre.game import play as playLeNombre

import pygame
pygame.init()

# REFS
GAMES:list[tuple[str,Callable]] = [
    ('Le Mot',playLeMot),
    ('Le Nombre',playLeNombre)
] # further games to come
CURRENT_GAME = None

# global booleans
RUNNING = True
MAIN_MENU = True

# ===== MAIN MENU ONLY FUNCTIONS =====
def build_main_menu():
    display_text("Le Pack",('Comic sans MS',90),(85,50),text_bold=True)

    # create the buttons to play games
    buttons = []
    for i in range(len(GAMES)):
        b = Button(i,(250,225+50*i,pygame.Color(75,75,75)),(300,30),(GAMES[i][0],150,200+50*i,PYGAME_WHITE))
        b.display()
        buttons.append(b)
    return buttons

def choice_game(buttons,pos):
    for b in buttons:
        x = b.is_clicked(pos)
        if x!=-1:
            return x
    return -1


# DA GAME ==========================================
init_graphic(500,500,"Le Pack")
clear_window(PYGAME_GRAY)
choose_your_game = build_main_menu()

while RUNNING:
    if MAIN_MENU:
        CURRENT_GAME = None
        pos = wait_clic()
        game_nb = choice_game(choose_your_game,pos)
        if game_nb!=-1:
            MAIN_MENU = False
            CURRENT_GAME = GAMES[game_nb]

    if not MAIN_MENU:
        clear_window(PYGAME_GRAY)
        MAIN_MENU = GAMES[game_nb][1]()
        clear_window(PYGAME_GRAY)
        choose_your_game = build_main_menu()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            RUNNING = False
            pygame.quit()
