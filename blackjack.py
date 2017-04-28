import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits=['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for that specific card
    for suit in suits:
        # first the number cards 1-10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, ))

            #face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # deal next card off top of deck
    next_card = deck.pop(0)
    # the POP command is a way to retrieve a item from a list and remove it at the same time
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return the cards face value
    return next_card


def score_hand(hand):
    # calculate the total score of all cards in the list.
    # only one ace can have the value 11, and this would reduce to 1
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if bust, check for an ace and subtract 10 if one exists
        if score > 21 and ace:
            score -=10
            ace = False
    return score



def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("fuck yeah, seaking")
    elif dealer_score > player_score:
        result_text.set("the house always wins")
    else:
        result_text.set("draw!")


# use global keyword to tell the function to use the global variables instead of variables contained in the function
def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("dealer wins!")

    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract 10
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set('dealer wins!')
    # # use locals() to show which local variables are being used in a function
    # print(locals())


def opening_hand():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global player_card_frame
    global dealer_card_frame
    player_card_frame.destroy()
    dealer_card_frame.destroy()
    dealer_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="dealer", background="green", fg='white',).grid(row=0, column=0)
    tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
    # embedded frame that holds the dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="player", background='green', fg='white').grid(row=2, column=0)
    tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
    # embedded frame to hold the card images
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()




mainWindow = tkinter.Tk()

# set up the screen and frames for the dealer and player
mainWindow.title("black jack (and hookers)")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="dealer", background="green", fg='white',).grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
# embedded frame that holds the dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="player", background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button =tkinter.Button(button_frame, text='player', command=deal_player)
player_button.grid(row=0, column=1)

quit_button = tkinter.Button(button_frame, text='new game', command=new_game)
quit_button.grid(row=0, column=2)

# load cards
cards = []
load_images(cards)
# print(cards)
#create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# create the list to store the dealer's and players hand
dealer_hand = []
player_hand = []

opening_hand()



mainWindow.mainloop()