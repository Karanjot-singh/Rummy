import pygame

class Card():
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value

class button():
    def __init__(self,  x,y, text='',width=90,height=50,color=(255,255,255)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def make_button(self,screen,outline=(0,0,0)):
        pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont(None, 25)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class Textbox:

    def __init__(self, x, y, w=40, h=35, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color =(255,255,255)
        self.text = text
        self.maintext = ""        
        font = pygame.font.SysFont(None, 25)
        self.txt_surface = font.render(text,1,(255,255,255))
        self.active = False

    def handle_event(self, event):
        font = pygame.font.SysFont(None, 25)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (0,90,0) if self.active else (255,255,255)

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.maintext = self.text
                    self.text=''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = font.render(self.text,1, (255,255,255))
    
    

    # def update(self):
    #     width = max(200, self.txt_surface.get_width()+10)
    #     self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        

