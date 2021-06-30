import pygame
BLACK = (0,255,0)

class Paddle(pygame.sprite.Sprite): #tworzymy klase paletki

    #sluzy do tworzenia paletek
    def __init__(self, color, width, height):
        super().__init__() #odwolujemy sie do klasy wbudowanej w pygame: Sprite

        self.image = pygame.Surface([width, height]) #zbieramy dane na temat koloru paletki, jej polozenia, itp. Ano i tlo ma niby byc przezroczyte(?) ale nie rozumiem do konca tak szczerze o co chodzi w tym miejscu
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0,width,height]) #tworzymy paletke

        self.rect = self.image.get_rect() #dostosowujemy paletke do romziarów okna *chyba*
    
    #sluzy do poruszania paletka w gore
    def moveUP(self, pixels):
        self.rect.y -= pixels*2 #im not sure ale chyba tak jakby przemieszczamy sie o wyznaczona ilosc pikseli (?)
        #sprawdzamy czy nie wypadamy poza mape
        if self.rect.y <0:
            self.rect.y =0

    #ten sluzy do poruszania paletka w dol
    def moveDOWN(self, pixels):
        self.rect.y += pixels*2 #im not sure ale chyba tak jakby przemieszczamy sie o wyznaczona ilosc pikseli (?) no to co wyzej oguem
        #i tez tak jak na gorze upewniamy sie ze nioe wypaodlismy poza mape
        if self.rect.y > 400:
            self.rect.y = 400
    
