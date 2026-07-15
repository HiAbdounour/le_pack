### Note :
# These functions and classes are extracted from my personal
# local library named noormi (with some local modifications).
# ===========================================================

from typing import Literal
import pygame
pygame.init()

# ============= COLORS ================
PYGAME_GRAY = pygame.Color(128,128,128)
PYGAME_GREY = PYGAME_GRAY
PYGAME_GREEN = pygame.Color(0,255,0)
PYGAME_ORANGE = pygame.Color(255,127,0)
PYGAME_RED = pygame.Color(255,0,0)
PYGAME_WHITE = pygame.Color(255,255,255)
PYGAME_BLACK = pygame.Color(0,0,0)
PYGAME_BLUE = pygame.Color(0,0,255)

# ============= WINDOW CONSTANTS ============
PYGAME_WINDOW = None
PYGAME_WIDTH = None
PYGAME_HEIGHT = None

# ========== WINDOW MANAGEMENT ===============
def init_graphic(width:int,height:int,name:str="Default name",fullscreen:bool=False,resizable:bool=False)-> None:
    """
    Init the graphic window for a PyGame project
    The initial size of the window is given by width (integer) and height (integer) but can be resizable (if resizable
    is set as True) OR inited as fullscreen (if fullscreen is set as True)
    name is the name of the window (must be a string)

    NB : A window cannot be both resizable and fullscreen. If both are set as True,
    the fullscreen statement will be applied (the window won't be resizable).

    Note that the fullscreen window may encounter some stability problems
    (things to fix)
    """
    if not isinstance(width,int) or not isinstance(height,int):
        raise TypeError("width and height must be integers")
    if not isinstance(name,str):
        raise TypeError("name must be a string")
    if width<0: width=0
    if height<0: height=0
    if fullscreen:
        flags = pygame.FULLSCREEN
    elif resizable:
        flags = pygame.RESIZABLE
    else:
        flags = 0

    global PYGAME_WINDOW, PYGAME_HEIGHT, PYGAME_WIDTH
    PYGAME_WINDOW = pygame.display.set_mode((width,height),flags)
    PYGAME_WIDTH = width
    PYGAME_HEIGHT = height
    pygame.display.set_caption(name)
    pygame.display.flip()

def clear_window(fill_color:pygame.Color=PYGAME_BLACK)-> None:
    """
    Clear the graphic window with a fill color
    By default, the color is black
    """
    global PYGAME_WINDOW,PYGAME_WIDTH,PYGAME_HEIGHT
    if PYGAME_WINDOW is None:
        raise ValueError("the graphic window must be initialized before using clear_window()")
    if not isinstance(fill_color, pygame.Color):
        raise TypeError("fill_color must be a pygame.Color")

    pygame.draw.rect(PYGAME_WINDOW,fill_color,(0,0,PYGAME_WIDTH,PYGAME_HEIGHT),0)
    pygame.display.flip()

# ============= UTILS ================
def alison(key:Literal['alpha','ALPHA','num','alphanum','ALPHANUM','all','allnum']='allnum')-> str:
    """
    Create a special string which contains all ordered alphanumerical characters and return it

    By default, return a string which contains all letters from 'A' to 'Z' then from 'a' to 'z'
    and finally from '0' to '9'

    The key parameter controlls what especially the alison function will return :
        "alpha" -> all letters from 'a' to 'z'
        "ALPHA" -> all letters from "A" to "Z"
        "num" -> all digits as string from '0' to '9'
        "alphanum" -> combine "alpha" and "num"
        "ALPHANUM" -> combine "ALPHA" and "num"
        "all" -> combine "ALPHA" and "alpha"
        "allnum" -> combine "all" and "num"
    """
    if key not in ['alpha','ALPHA','num','alphanum','ALPHANUM','all','allnum']:
        raise Exception(f"{key} keyword isn't allowed. The key argument muss be one of these :"
                        f"'alpha', 'ALPHA', 'num', 'alphanum', 'ALPHANUM', 'all' or 'allnum'")
    if key=='alpha': return 'abcdefghijklmnopqrstuvwxyz'
    if key=='ALPHA': return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if key=='alphanum': return 'abcdefghijklmnopqrstuvwxyz0123456789'
    if key=='num': return '0123456789'
    if key=='ALPHANUM': return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if key=='all': return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


# ============== PYGAME UTILS ================
class Point:
    def __init__(self,x:int|float,y:int|float):
        if (not isinstance(x,int) and not isinstance(x,float)) or (not isinstance(y,int) and not isinstance(y,float)):
            raise TypeError("Point only works with numeric values (int or float)")
        self.x = x
        self.y = y
    def __eq__(self, other):
        if isinstance(other,Point):
            return self.x==other.x and self.y==other.y
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return f"Point({self.x},{self.y})"
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def get_values(self):
        return (self.x,self.y)

    def convert_center(self,dim:tuple[int,int],flag=False):
        """
        Center a Point into a case of dimensions given by dim
        dim should be a tuple of two positive integers, dim = (width,height)
        Return the centered Point (does not affect the original point)
        WARNING : The centered Point will have INTEGER values not float. It is thus recommended to give even values.

        This warning as a reminder will be shown if flag equals False :
        WARNING : If you use this method, consider the Pixel submodule instead of the Point submodule
        """
        if not flag:
            print("\nWARNING : If you use this method, consider the Pixel submodule instead of the Point submodule ")
        if not isinstance(dim,tuple) or len(dim)!=2:
            raise TypeError("dim should be a tuple of 2 elements")
        if not isinstance(dim[0],int) or not isinstance(dim[1],int) or dim[0]<=0 or dim[1]<=0:
            raise ValueError("dim must contain only positive integers")

        i,j = self.x//dim[0],self.y//dim[1]
        return Point(i*dim[0]+(dim[0]//2),(j*dim[1]+(dim[1]//2)))

    def draw(self,clr:pygame.Color)-> None:
        """
        Draw the point P in the graphic window with the color clr
        """
        global PYGAME_WINDOW
        if not isinstance(clr,pygame.Color):
            raise TypeError("clr must be a pygame.Color")
        pygame.draw.line(PYGAME_WINDOW,clr,self.get_values(),self.get_values(),1)
        pygame.display.flip()

def wait_clic()-> Point|None:
    """
    Wait for an action from the user : mouse click
    Return the coordinates of the click as a Point
    Freeze the program until the user clicks somewhere into the graphic window

    Note that the user can close the window during the waiting session.
    """
    pygame.event.clear()
    while True:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return Point(event.pos[0],event.pos[1])

def draw_rectangle(P:Point,w:int|float,h:int|float,clr:pygame.Color,fillval:Literal[0,1]=0)-> None:
    """
    Draw a rectangle from dimensions lxh with P being the center of the rectangle
    l -> length (int or float)
    h -> height (int or float)
    clr -> color of the border (pygame.Color)
    fillval -> =0 if empty rectangle with border / =1 if fill rectangle
    """
    if not isinstance(P,Point):
        raise TypeError("P must be a Point")
    if not isinstance(clr,pygame.Color):
        raise TypeError("clr must be a pygame.Color")
    if (not isinstance(w, int) and not isinstance(w, float)) or (not isinstance(h, int) and not isinstance(h, float)):
        raise TypeError("w and h must be integers or floats")
    if w<=0 or h<=0:
        raise ValueError("w and h must be greater than zero")
    if not isinstance(fillval,int):
        raise TypeError("fillval must be an integer")
    if fillval not in (0,1):
        raise ValueError("fillval must be equal to 0 or 1")
    fillval = (fillval+1)%2

    global PYGAME_WINDOW
    x,y = P.get_values()
    pygame.draw.rect(PYGAME_WINDOW, clr, (int(x-w/2), int(y-h/2), w, h), fillval)
    pygame.display.flip()

def display_text(txt:str,font:tuple[str,int]=("Verdana",12),coord:tuple[int|float,int|float]=(0,0),
                 clr:pygame.Color=PYGAME_WHITE,text_bold:bool=False,text_italic:bool=False)-> None:
    """
    Display the text txt (string) in the graphic window at the coordinates coord (by default, (0,0) )
    font is a tuple configured as (font_name,font_size). By default : ("Verdana", 12)
    clr is the color of the text. By default : white color
    text_bold and text_italic are bool that activates respectively boldness and italic
    """
    if not isinstance(txt,str):
        raise TypeError("txt must be a string")
    if not isinstance(font,tuple):
        raise TypeError("font must be a tuple of two elements : font_name and font_size")
    if not isinstance(font[0],str) or not isinstance(font[1],int) or font[1]<=0:
        raise TypeError("font must be a tuple of two elements : font_name (string) and font_size (positive integer)")
    if not isinstance(coord,tuple):
        raise TypeError("coord must be a tuple")
    if (not isinstance(coord[0],int) and not isinstance(coord[0],float)) or \
        (not isinstance(coord[1],int) and not isinstance(coord[1],float)):
        raise TypeError("coord must contain numeric values (integers or floats)")
    if not isinstance(clr,pygame.Color):
        raise TypeError('clr must be a pygame.Color')
    if not isinstance(text_bold,bool) or not isinstance(text_italic,bool):
        raise TypeError("Expected booleans for text_bold / text_italic")

    global PYGAME_WINDOW
    font = pygame.font.SysFont(font[0],font[1],bold=text_bold,italic=text_italic)
    rtxt = font.render(txt,1,clr)
    PYGAME_WINDOW.blit(rtxt,(coord[0],coord[1]))
    pygame.display.flip()

def draw_line(P:Point,Q:Point,clr:pygame.Color)-> None:
    """
    Draw a line between two points P and Q with the color clr in the graphic window
    """
    if not isinstance(P,Point) or not isinstance(Q,Point):
        raise TypeError("P and Q must be a Point")
    if not isinstance(clr,pygame.Color):
        raise TypeError("clr must be a pygame.Color")

    global PYGAME_WINDOW
    pygame.draw.line(PYGAME_WINDOW,clr,P.get_values(),Q.get_values(),1)
    pygame.display.flip()

class Button:
    def __init__(self,info:int,rect:tuple[int,int,pygame.Color],
                 size:tuple[int,int],txt_rect:tuple[str,int,int,pygame.Color]):
        self.info = info
        self.rect = rect
        self.size = size
        self.txt_rect = txt_rect
    def display(self):
        draw_rectangle(Point(self.rect[0],self.rect[1]),self.size[0],self.size[1],self.rect[2],1)
        display_text(self.txt_rect[0],('Comic sans MS',32),(self.txt_rect[1],self.txt_rect[2]),
                     clr=self.txt_rect[3],text_bold=True)
    def is_clicked(self,pos:Point)-> int:
        if (self.rect[0]-(self.size[0]//2)<=pos.x<=self.rect[0]+(self.size[0]//2)
                and self.rect[1]-(self.size[1]//2)<=pos.y<=self.rect[1]+(self.size[1]//2)):
            return self.info
        return -1

# ============== NOT IN NOORMI ================
def add_pts(pts):
    """
    Add points to the existing score
    """
    with open('ressources/points.txt','r') as file:
        actualpts = int(file.read())
    try:
        with open('ressources/points.txt','w') as file:
            file.write(str(actualpts+pts))
    except:
        with open('ressources/points.txt','w') as file:
            file.write(str(actualpts))