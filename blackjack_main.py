from pygame import *
import os
import random
import images
import colors
from buttons import *
from pictures import *
import cards
import collections

window_size = (800,500)
main_window = display.set_mode(window_size)
img_background_path = os.path.join(os.getcwd(), images.background_path)
background = transform.scale(image.load(img_background_path), window_size)
img_game_backghround_path = os.path.join(os.getcwd(), images.game_background_path)
game_background = transform.scale(image.load(img_game_backghround_path), window_size)
display.set_caption("Blackjack")
#display.set_icon(os.path.join(os.getcwd(), images.icon_path))
font.init()
#modes = {"Classic": ("Классика", colors.green), "Custom": ("Кастом", colors.red)} # Declare game modes
player = {"chips": 100, "check_buffs": None}
bf_costs = {25: "250 chips", 50: "500 chips", 75: "1000 chips"}
def intro_menu():
    """ Show intro menu in which you can read about rules, change game mode, go to shop or quit """
    btn_start_game, btn_exit_game, btn_shop, btn_add_player, btn_substract_player = intro_buttons_init() # Main buttons for menu
    #current_mode, mode_rect_color = modes["Classic"] # gives here name of mode and color for btn_change_mode color rect
    #current_players = 1
    intro = True
    while intro:
        #btn_change_mode = Button(f"Режим: {current_mode}", (25, 260))
        #btn_number_of_players = Button(f"Игроков: {str(current_players)}", (25, 200))
        for ev in event.get():
            if ev.type == QUIT:
                os._exit(0)

            if ev.type == MOUSEBUTTONDOWN:
                if btn_exit_game.check_click(ev.pos):
                    os._exit(0)
                if btn_start_game.check_click(ev.pos):
                    intro = False
                    main_game_loop()
                #if btn_change_mode.check_click(ev.pos): # Change mode to custom or classic
                    #mode_change = {modes["Classic"][0]: modes["Custom"], modes["Custom"][0]: modes["Classic"]} # less then if/else
                    #current_mode, mode_rect_color = mode_change[current_mode] # gives here name of mode and color for btn_change_mode color rect
                #Add\substract players
                if btn_add_player.check_click(ev.pos) and current_players < 4:
                    current_players += 1
                if btn_substract_player.check_click(ev.pos) and current_players > 1:
                    current_players -= 1
                if btn_shop.check_click(ev.pos):
                    intro = False
                    shop()
        #Blit
        main_window.blit(background, (0, 0))
        btn_start_game.draw_rect(main_window)
        btn_start_game.update(main_window)
        btn_shop.draw_rect(main_window)
        btn_shop.update(main_window)
        btn_exit_game.draw_rect(main_window)
        btn_exit_game.update(main_window)
        btn_change_mode.draw_rect(main_window, mode_rect_color)
        btn_change_mode.update(main_window)
        btn_number_of_players.draw_rect(main_window)
        btn_number_of_players.update(main_window)
        btn_add_player.update(main_window)
        btn_substract_player.update(main_window)
        display.update()
        time.delay(33)

def shop():
    shop = True
    img_shop_background = os.path.join(os.getcwd(), images.background_path)
    shop_background = transform.scale(image.load(img_background_path), window_size)
    money = player["chips"]
    m_font = font.SysFont("Arial", 28)
    money_on_screen = (40, 70)
    btn_buff_checks = Button("Check dealer face down card with some chance", (55, 145), "Arial", 30)
    btn_back_to_menu = Button("Menu", (690, 450), size=35)
    warn_font = font.SysFont("arial", 28)
    warning_message1 = warn_font.render("Buff's working only in custom mode", 1, colors.white)
    warning_message2 = warn_font.render("Use them before you click on deal", 1, colors.white)
    buff = False
    while shop:
        money_font = m_font.render(f"Chips: {money}", 1, colors.white)
        for ev in event.get():
            if ev.type == QUIT:
                os._exit(0)

            if ev.type == MOUSEBUTTONDOWN:
                if btn_back_to_menu.check_click(ev.pos):
                    shop = False
                    intro_menu()
                if btn_buff_checks.check_click(ev.pos):
                    check_cards_pos = (80, 200)
                    btn_25_check_card = Button(f"- 25% is {bf_costs[25]}", check_cards_pos, "Arial", 30)
                    btn_50_check_card = Button(f"- 50% is {bf_costs[50]}", (check_cards_pos[0], check_cards_pos[1]+50), "Arial", 30)
                    btn_75_check_card = Button(f"- 75% is {bf_costs[75]}", (check_cards_pos[0], check_cards_pos[1]+100), "Arial", 30)
                    if buff: # If alredy show
                        buff = False # hide
                    else: # else
                        buff = True #show
                if buff and btn_25_check_card.check_click(ev.pos):
                    if player["check_buffs"] == None:
                        money -= bf_costs[25]
                        player["check_buffs"] = "1/4"
                if buff and btn_50_check_card.check_click(ev.pos):
                    if player["check_buffs"] == None:
                        money -= bf_costs[50]
                        player["check_buffs"] = "1/2"
                if buff and btn_75_check_card.check_click(ev.pos):
                    if player["check_buffs"] == None:
                        money -= bf_costs[75]
                        player["check_buffs"] = "1/3"

        main_window.blit(shop_background, (0, 0))
        draw.rect(main_window, colors.blue, [(400, 50), warning_message1.get_rect()[2:4]])
        main_window.blit(warning_message1, (400, 50))
        draw.rect(main_window, colors.blue, [(420, 90), warning_message2.get_rect()[2:4]])
        main_window.blit(warning_message2, (420, 90))
        draw.rect(main_window, colors.blue, [money_on_screen, money_font.get_rect()[2:4]])
        main_window.blit(money_font, money_on_screen)
        btn_buff_checks.draw_rect(main_window)
        btn_buff_checks.update(main_window)
        btn_back_to_menu.draw_rect(main_window)
        btn_back_to_menu.update(main_window)
        if buff: # show buttons
            btn_25_check_card.draw_rect(main_window, colors.eat_color)
            btn_25_check_card.update(main_window)
            btn_50_check_card.draw_rect(main_window, colors.eat_color)
            btn_50_check_card.update(main_window)
            btn_75_check_card.draw_rect(main_window, colors.eat_color)
            btn_75_check_card.update(main_window)
        display.flip()
        time.delay(33)

def main_game_loop():
    game = True
    #btn_back_to_menu = Button("Menu", (670, 450), size=35)
    pic_deal, pic_double, pic_down_bet, pic_hit, pic_stand, pic_up_bet = main_game_pic_init() # Main pictures (for hit, stand, etc)
    pictures = sprite.Group(pic_deal, pic_double, pic_down_bet, pic_hit, pic_stand, pic_up_bet)
    deck = cards.generate_deck()
    p_cards_pos = (510, 320)
    d_cards_pos = (20, 20)
    dealer_hand, player_hand = [], []
    dealer_cards, player_cards = sprite.Group(), sprite.Group()
    start_round, double_down, game_over = False, False, False
    chips = player["chips"]
    bet = 10
    pounds_font = font.SysFont("Arial", 28)
    text_font = font.SysFont("Arial", 28)
    msg_to_player = "Click on arrows to declare your bet, then deal to start the game." #Say to player
    while game:
        chips_font = pounds_font.render(f"Chips: {chips}", 1, colors.white)
        bet_font = pounds_font.render(f"Bet: {bet}", 1, colors.white)
        if chips <= 5:
            game_over = True 
        for ev in event.get():
            if ev.type == QUIT:
                os._exit(0)
            
            if ev.type == MOUSEBUTTONDOWN:
               # if btn_back_to_menu.check_click(ev.pos):
               #     game = False
               #     intro_menu()
                if not start_round and not game_over and pic_deal.check_click(ev.pos):
                    chips -= bet
                    msg_to_player = "" # We shouldn't say something
                    pic_deal.change_pic(images.dealg_path) # Paint deal into grey color
                    dealer_cards.empty() # Clear cards on table
                    player_cards.empty()
                    cards_to_deal = 4
                    while cards_to_deal > 0:
                        if len(deck) == 0:
                            deck = cards.generate_deck()

                        if cards_to_deal % 2 == 0: # Every odd to player
                            player_hand.append(deck[0])
                            player_cards.add(Picture(images.cards_path + f"{deck.get_image(deck[0])}.png", p_cards_pos))
                            p_cards_pos = (p_cards_pos[0] - 80, p_cards_pos[1])
                        else: #If even
                            dealer_hand.append(deck[0])
                        
                        del deck[0] # Del card from deck
                        cards_to_deal -= 1
                    dealer_cards.add(Picture(images.cards_path + "back.png", d_cards_pos)) # One card is face down
                    d_cards_pos = (d_cards_pos[0] + 80, d_cards_pos[1])
                    dealer_cards.add(Picture(images.cards_path + f"{deck.get_image(dealer_hand[1])}.png", d_cards_pos))
                    d_cards_pos = (d_cards_pos[0] + 80, d_cards_pos[1])
                    start_round = True # we are ready to go
                #Declare player bet
                if pic_up_bet.check_click(ev.pos) and not start_round:
                    if bet < chips:
                        bet += 5
                
                if pic_down_bet.check_click(ev.pos) and not start_round:
                    if bet > 5:
                        bet -= 5

                if len(player_hand) == 2 and pic_double.check_click(ev.pos) and start_round: # If player can double
                    if bet*2 < chips: # If player can afford it
                        chips -= bet
                        bet *= 2 # Total bet is bet*2 
                        deck, player_hand, card, p_cards_pos = cards.hit(deck, player_hand, p_cards_pos)
                        player_cards.add(card)
                        double_down = True
                    else:
                        msg_to_player = "Your chips isn't enough"
                if pic_hit.check_click(ev.pos) and start_round and not double_down: # If player hit
                    deck, player_hand, card, p_cards_pos = cards.hit(deck, player_hand, p_cards_pos)
                    player_cards.add(card)
                if pic_stand.check_click(ev.pos) and start_round or double_down: # if player stand
                    start_round = False # End round
                    double_down = False 
                    dealer_cards.empty()
                    dealer_cards.add(Picture(images.cards_path + f"{deck.get_image(dealer_hand[0])}.png", (d_cards_pos[0]-160, d_cards_pos[1])))
                    dealer_cards.add(Picture(images.cards_path + f"{deck.get_image(dealer_hand[1])}.png", (d_cards_pos[0]-80, d_cards_pos[1]))) # show both dealer cards
                    while dealer_value < 17: # While dealer hand less then 17 take a card and show for player
                        deck, dealer_hand, card, d_cards_pos = cards.hit(deck, dealer_hand, d_cards_pos)
                        dealer_cards.add(card)
                        dealer_value = cards.check_hand(dealer_hand)
                    chips, msg_to_player, p_cards_pos, d_cards_pos, player_hand, dealer_hand  = cards.compare_hands(player_hand, dealer_hand, chips, bet)

        if start_round: # if round is started, then paint buttons
            pic_hit.change_pic(images.hit_path)
            pic_stand.change_pic(images.stand_path)
            pic_double.change_pic(images.double_path)
        else: # if not, then only deal is painted
            pic_deal.change_pic(images.deal_path)
            pic_hit.change_pic(images.hitg_path)
            pic_double.change_pic(images.doubleg_path)
            pic_stand.change_pic(images.standg_path)

        main_window.blit(game_background, (0, 0))
       # btn_back_to_menu.draw_rect(main_window)
       # btn_back_to_menu.update(main_window)
        main_window.blit(chips_font, (665, 150))
        main_window.blit(bet_font, (665, 190))
        pictures.draw(main_window)
        if game_over: # If player lose = show message
            msg_to_player = "You are out of chips. Exit to menu for continue"
        if msg_to_player: # if we have what to say for player
            msg_font = text_font.render(msg_to_player, 1, colors.white)
            main_window.blit(msg_font, (10, 455))
        if len(dealer_cards): # If we have cards to show
            dealer_cards.draw(main_window)
            player_cards.draw(main_window)
            dealer_value = cards.check_hand(dealer_hand) # sum of hand
            player_value = cards.check_hand(player_hand) # sum of hand

            if player_value > 21: # if player busts
                start_round = False # End round
                dealer_cards.empty() # For show both dealer cards
                dealer_cards.add(Picture(images.cards_path + f"{deck.get_image(dealer_hand[0])}.png", (d_cards_pos[0]-160, d_cards_pos[1])))
                dealer_cards.add(Picture(images.cards_path + f"{deck.get_image(dealer_hand[1])}.png", (d_cards_pos[0]-80, d_cards_pos[1]))) 
                chips, msg_to_player, p_cards_pos, d_cards_pos, player_hand, dealer_hand  = cards.compare_hands(player_hand, dealer_hand, chips, bet) # Round results

        display.update()
        time.delay(33)

if __name__ == "__main__":
    #intro_menu()
    main_game_loop()
