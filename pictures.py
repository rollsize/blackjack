from pygame import *
import images
class Picture(sprite.Sprite):
    def __init__(self, pic_path:str, position:set, pic_size:set=None):
        super().__init__()
        if isinstance(pic_size, type(None)):
            self.image = image.load(pic_path)
        else:
            self.image = transform.scale(image.load(pic_path), pic_size) # if pic_size != None

        self.rect = self.image.get_rect()
        self._pos = position
        self.rect.x, self.rect.y = self._pos[0], self._pos[1]
    
    def change_pic(self, pic_path:str, pic_size:set=None):
        """ Change picture for already initialized Picture object """
        if isinstance(pic_size, type(None)):
            self.image = image.load(pic_path)
        else:
            self.image = transform.scale(image.load(pic_path), pic_size)

    def check_click(self, mouse_pos) -> bool:
        """ Return True if mouse clicked on picture """
        if self.rect.collidepoint(mouse_pos):
            return True
        return False

    def draw_rect(self, surface, rect_color:set):
        """ Draw rect for picture in surface which given. Default color is colors.blue """
        draw.rect(surface, rect_color, [self._pos, self.rect[2:4]])

def main_game_pic_init():
    """ Initialization of main pictures for game (hit, double, etc.) """
    pic_hit = Picture(images.hitg_path, (680, 345))
    pic_deal = Picture(images.deal_path, (680, 385))
    pic_stand = Picture(images.standg_path, (680, 315))
    pic_double = Picture(images.doubleg_path, (680, 285))
    pic_up_bet = Picture(images.bet_up_path, (680, 225))
    pic_down_bet = Picture(images.bet_down_path, (730, 225))
    return (pic_deal, pic_double, pic_down_bet, pic_hit, pic_stand, pic_up_bet)