from pygame import *
import colors
class Button(sprite.Sprite):
    def __init__(self, text:str, position:set, font_name=None, size=None, color=None):
        super().__init__()
        self.btn_text = text
        self._pos = position
        self._btn_font = "Corbel" if isinstance(font_name, type(None)) else font_name #Default if None
        self._btn_size = 45 if isinstance(size, type(None)) else size #Default if None
        self._btn_color = colors.white if isinstance(color, type(None)) else color #Default if None
        self._sized_font = font.SysFont(self._btn_font, self._btn_size)
        self.final_btn = self._sized_font.render(self.btn_text, 1, self._btn_color) # Render
        self.rect = self.final_btn.get_rect()
        self.rect.x, self.rect.y = self._pos[0], self._pos[1]

    def check_click(self, mouse_pos) -> bool:
        """ Return True if mouse clicked on button """
        if self.rect.collidepoint(mouse_pos):
            return True
        return False 

    def draw_rect(self, surface, rect_color=None):
        """ Draw rect for button in surface which given. Default color is colors.blue """

        if isinstance(rect_color, type(None)): # default color
            rect_color = colors.blue
        draw.rect(surface, rect_color, [self._pos, self.rect[2:4]])

    def update(self, surface):
        """ Draw button on the surface which given """
        surface.blit(self.final_btn, self._pos)

def intro_buttons_init():
    """ Initialization of main buttons for intro menu """
    btn_start_game = Button("Начать игру", (405,200)) 
    btn_exit_game = Button("Выйти из игры", (380, 320))
    btn_shop = Button("Магазин", (439, 260))
    btn_add_player = Button("+", (240, 200))
    btn_substract_player = Button("-", (270, 200))
    return (btn_start_game, btn_exit_game, btn_shop, btn_add_player, btn_substract_player)