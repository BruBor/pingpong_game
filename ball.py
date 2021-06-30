
import pygame
from random import randint #bedzie potrzebne do nadania losowej predkosci poczatkowej dla pilki
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite): #tworzymy klase pileczka
    #sluzy do tworzenia pileczek
    def __init__(self, color, width, height):
        super().__init__() #odwolujemy sie do klasy wbudowanej w pygame: Sprite

        self.image = pygame.Surface([width, height]) #zbieramy dane na temat koloru pilki, jej polozenia, itp. Ano i tlo ma niby byc przezroczyte(?) ale nie rozumiem do konca tak szczerze o co chodzi w tym miejscu
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #wsm to wiekszosc z tego jest taka sama jak w przypadku paletki

        pygame.draw.rect(self.image, color, [0,0,width,height]) #tworzymy pileczke

        self.velocity = [randint(4,8),randint(-8,8)]#nadajemy predkosc początkową i zwrot(NIE KIERUNEK, FIZYKA MORDO PAMIOETAJ ZWROT TO NIE KIERUNEK) pileczce, losowane z podanych zakresow


        self.rect = self.image.get_rect() #dostosowujemy pileczke do romziarów okna *chyba*

    #sluzy do zmieniania pozycji pileczki zgodnie z podana predkoscia(velocity)
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    #sluzy do odbijania sie od paletek
    def bounce(self):
        self.velocity[0] = -self.velocity[0]#odbijamy się z ta sama predkoscia...
        self.velocity[1] = randint(-8,8)#...w losowym kierunku
    
    def after_bounce(self):
        nball = Ball((172,192,203),10,10)
        nball.rect.x = 345
        nball.rect.y = 195
        return nball
