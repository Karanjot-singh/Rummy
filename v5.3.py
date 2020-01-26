import pygame
import random
from f import *

SCREEN_SIZE = (1300, 760) 


pygame.init()
#add icon
deck=[]
player1_obj=[]
computer_obj=[]
discard_pile=['04s']
player1_deck=[]
computer_deck=[]
player_win=[]
computer_win=[]
y=False
k=0
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)#SCREEN_SIZE, FULLSCREEN, 32)
pygame.display.set_caption("Rummy 101 by Karanjot Singh")


cardd = pygame.image.load('Image/'+discard_pile[0]+'.gif').convert()
def display():
    global cardd
    # screen.fill((30,190,90))
    largeText = pygame.font.Font(None,45)
    TextSurf, TextRect = text_objects("~ RUMMY ~", largeText,(255,255,255))
    TextRect.center = (650,50)    
    screen.blit(TextSurf, TextRect)
    global player1_deck
    card1= pygame.image.load('Image/'+player1_deck[0]+'.gif').convert()
    card2= pygame.image.load('Image/'+player1_deck[1]+'.gif').convert()
    card3= pygame.image.load('Image/'+player1_deck[2]+'.gif').convert()
    card4= pygame.image.load('Image/'+player1_deck[3]+'.gif').convert()
    card5= pygame.image.load('Image/'+player1_deck[4]+'.gif').convert()
    card6= pygame.image.load('Image/'+player1_deck[5]+'.gif').convert()
    card7= pygame.image.load('Image/'+player1_deck[6]+'.gif').convert()
    card8= pygame.image.load('Image/'+player1_deck[7]+'.gif').convert()
    card9= pygame.image.load('Image/'+player1_deck[8]+'.gif').convert()
    card10= pygame.image.load('Image/'+player1_deck[9]+'.gif').convert()
    card11= pygame.image.load('Image/'+player1_deck[10]+'.gif').convert()
    card12= pygame.image.load('Image/'+player1_deck[11]+'.gif').convert()
    card13= pygame.image.load('Image/'+player1_deck[12]+'.gif').convert()
    cardd = pygame.image.load('Image/'+discard_pile[0]+'.gif').convert()


    card_stock= pygame.image.load('Image/back111.gif').convert()

    w = card1.get_width()
    h= card1.get_height()
    gap= 10
    screen.blit(card1,(1*(w+gap),760-2*h))
    screen.blit(card2,(2*(w+gap),760-2*h))    
    screen.blit(card3,(3*(w+gap),760-2*h))
    screen.blit(card4,(4*(w+gap),760-2*h))
    screen.blit(card5,(5*(w+gap),760-2*h))
    screen.blit(card6,(6*(w+gap),760-2*h))
    screen.blit(card7,(7*(w+gap),760-2*h))
    screen.blit(card8,(8*(w+gap),760-2*h))
    screen.blit(card9,(9*(w+gap),760-2*h))
    screen.blit(card10,(10*(w+gap),760-2*h))
    screen.blit(card11,(11*(w+gap),760-2*h))
    screen.blit(card12,(12*(w+gap),760-2*h))
    screen.blit(card13,(13*(w+gap),760-2*h))
    screen.blit(card_stock,(6.35*(w+gap),760-4.5*h))
    screen.blit(cardd,(7.35*(w+gap),760-4.5*h))

    b1.make_button(screen)
    b2.make_button(screen)
    b3.make_button(screen)
    b4.make_button(screen)
    b5.make_button(screen)

    pygame.display.update()
    # moves()


def build_deck():
    suit=['club','diamond','heart','spade']
    rank = ['01','02','03','04','05','06','07','08','09','09','10','11','12','13']

    global deck,player1_obj
    for i in suit:
        for j in rank:
        	obj = Card(i,int(j))
        	t=j+i[0]
        	deck.append(t)
            # player1_obj.append(obj) 
    cards_dist()

def cards_dist():
    ''' To handle random distribution of cards for computer and player
    '''
    global deck,player1_deck,discard_pile
    random.shuffle(deck)
    for i in range(13):
        c=random.choice(deck)
        deck.remove(c)
        player1_deck.append(c)

    for i in range(13):
        c=random.choice(deck)
        deck.remove(c)
        computer_deck.append(c)
    
    d = random.choice(deck)
    discard_pile[0]=d
    # print(discard_pile)
    deck.remove(d)
    pygame.display.update()


def discard_card():
    global player1_deck
    global discard_pile
    s=input_box2.maintext
    for i in player1_deck:
        if(i==s):
            player1_deck.remove(i)
            discard_pile.append(i)
            break
    discard_card_comp()

def discard_card_comp():
    global computer_deck
    global discard_pile
    global deck
    a=[0,1]
    rem = random.choice(computer_deck)
    c = random.choice(a)
    if(c==0):
        random.shuffle(deck)
        c=random.choice(deck)
        computer_deck.append(c)

    else:
        c=discard_pile[0]
        computer_deck.append(c) 
    computer_deck.remove(rem)
    discard_pile[0]=rem

def text_objects(text, font,color=(0,0,0)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def choose_card():
    global player1_deck
    global deck
    global discard_pile
    clock.tick(15)
    s= input_box1.maintext
    if s== '1' :
        print('f')
        random.shuffle(deck)
        c=random.choice(deck)
        player1_deck.append(c)
        discard_card()
    else:
        print('d')
        c=discard_pile[0]
        player1_deck.append(c)
        discard_card()

def sort_cards(l):
	l.sort()
def swap_cards(card1,card2):
    for i in range(len(player1_deck)):
        if(player1_deck[i])==card1:
            c=i
        if (player1_deck[i]==card2):
            d=i
    player1_deck[c],player1_deck[d]=player1_deck[d],player1_deck[c]


def moves(): 
    global y
    while y:
        print('move')
        # screen.blit(cardd,(800,400))
        choose_card()
        discard_card_comp()
        y=False
    return None


play = True
n=1

b1= button(650,400,'Sort')
b2= button(550,400,'Declare')
b3 = button(350,255,'Move')
b4 = button(850,255,'Swap')
b5= button(1100,30,'Restart')
b0= button(650,450,'Go')

clock = pygame.time.Clock()
input_box1 = Textbox(350, 400)
input_box2 = Textbox(400, 400)
input_box3 = Textbox(850, 400)
input_box4 = Textbox(900, 400)
input_boxes = [input_box1, input_box2,input_box3,input_box4]

def game_intro():
    k=0
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos()        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (b0.isOver(pos)):
                    k=1
                    break
        if(k==1):
            break
                
        screen.fill((0,0,0))
        largeText = pygame.font.Font(None,80)
        TextSurf, TextRect = text_objects("Rummy: CSE101", largeText,(255,255,255))
        TextRect.center = (650,380)
        b0.make_button(screen)
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        # clock.tick()

game_intro()

def handle_obj():
	sort_cards(player1_deck)
	sort_cards(computer_deck)
	for i in player1_deck:
		a = Card(i[2],int(i[0:2]))
		player1_obj.append(a)
	for i in computer_deck:
		a = Card(i[2],int(i[0:2]))
		computer_obj.append(a)

def check_set(obj_list):
	p=0
	for i in range(len(obj_list)-4):
		if(obj_list[i].value == obj_list[i+1].value==obj_list[i+2].value==obj_list[i+3].value ):

			p+=1
		elif(obj_list[i].value == obj_list[i+1].value==obj_list[i+2].value ):
			p+=1
		else:
			player_win.append(i)
			player_win.append(i+1)
			player_win.append(i+2)
			player_win.append(i+3)

	return p

def check_set_c(obj_list):
	p=0
	for i in range(len(obj_list)-4):
		if(obj_list[i].value == obj_list[i+1].value==obj_list[i+2].value==obj_list[i+3].value ):

			p+=1
		elif(obj_list[i].value == obj_list[i+1].value==obj_list[i+2].value ):
			p+=1
		else:
			computer_win.append(i)
			computer_win.append(i+1)
			computer_win.append(i+2)
			computer_win.append(i+3)

	return p

def check_run(obj_list):
	p=0
	for i in range(len(obj_list)-4):
		if(obj_list[i].value == obj_list[i+1].value-1==obj_list[i+2].value-2==obj_list[i+3].value-3 ):

			p+=1
		elif(obj_list[i].value == obj_list[i+1].value-1==obj_list[i+2].value-2 ):
			p+=1
		else:
			player_win.append(i)
			player_win.append(i+1)
			player_win.append(i+2)
			player_win.append(i+3)

	return p



while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        pos = pygame.mouse.get_pos()        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (b3.isOver(pos)):
                y=True
            if (b4.isOver(pos)):
                swap_cards(input_box3.maintext,input_box4.maintext)
            if (b1.isOver(pos)):
                sort_cards(player1_deck)
            if (b2.isOver(pos)):
                play,y = False,False
                k=1
                break
            if(b5.isOver(pos)):
            	game_intro()            	
            	n=1
        if event.type == pygame.MOUSEMOTION:
            if b1.isOver(pos):
                b1.color = (100,000,250)
            else:
                b1.color=(255,255,255)
            if b2.isOver(pos):
                b2.color = (100,000,250)
            else:
                b2.color=(255,255,255)
            if b3.isOver(pos):
                b3.color = (100,000,250)
            else:
                b3.color=(255,255,255)
            if b4.isOver(pos):
                b4.color = (100,000,250)
            else:
                b4.color=(255,255,255)
        for box in input_boxes:
            box.handle_event(event)
    screen.fill((40,170,40))
    for box in input_boxes:
        box.draw(screen)
    if n==1:
        build_deck()
    moves()
    display()
    pygame.display.update()
    n=n+1
#to check winner
handle_obj()
check_set(player1_obj)
check_set_c(computer_obj)
check_run(player1_obj)

if(len(player_win)==13):
	x=0
else:
	x=1

if x==0:
    screen.fill((0,0,0))
    largeText = pygame.font.Font(None,80)
    TextSurf, TextRect = text_objects("Player Wins", largeText,(255,255,255))
    TextRect.center = (650,380)
    b0.make_button(screen)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
if x==1:
    screen.fill((0,0,0))
    largeText = pygame.font.Font(None,80)
    TextSurf, TextRect = text_objects("Computer Wins", largeText,(255,255,255))
    TextRect.center = (650,380)
    b0.make_button(screen)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

pygame.quit()