import pygame 
#importujemy klasy:
from paddle import Paddle
from ball import Ball
pygame.init()

#KOLORKI DO GRY
BLACK = (0,0,0)
PINK = (255,192,203)

#OKNO GRY
size = (700,500)
screen = pygame.display.set_mode(size) #okno gry dostosuje się do wcześniej podanego rozmiaru
pygame.display.set_caption("berrpong")

#tworzymy paletki za pomoca klasy Paddle
paddleA = Paddle(PINK, 20, 100)
paddleA.rect.x = -10
paddleA.rect.y = 200

paddleB = Paddle(PINK, 20, 100)
paddleB.rect.x = 690
paddleB.rect.y = 200

#tworzymy pileczki za pomoca klasy Ball
ball = Ball(PINK,10,10)
ball.rect.x = 345
ball.rect.y = 195


all_sprites_list = pygame.sprite.Group()# lista na wszystkie spritey

#dodajemy paletki i pileczki do listy spritów
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#wynik na pocztku wuynosi 0:0
scoreA = 0
scoreB = 0

gameON = True
#glowna petla (bedize dzialala gdy gra jest odpalona: gameON)
while gameON:#jesli gra odpalona to....
    for event in pygame.event.get():#jesli uzytkownik kliknie...
        if event.type == pygame.QUIT:#..by wyjsc to wychodzi es
            gameON = False#wiec gra juz nie odpalona
        elif event.type==pygame.KEYDOWN:#...klawisz odpowiedni to wychodzi i  wsm to bardzo dobrze bo nwm czermu nie tworzy sie zaden x na gorze okienka od gry|||| update:JUZ SIE TWPORZY WSM NWM CZEMU ALE SIE TWORZY
            if event.key==pygame.K_x:#klawiszem tym jest "x"
                gameON = False#wiec gra juz nie odpalona
    
    #tu bedzie core calej gierki (backend hehe *smiech_sansa.mp3*):

    keys = pygame.key.get_pressed()#"keys" to klawisz ktory jest wcisniety

    if keys[pygame.K_w]:#jesli klawisz wcisniety to"w"...
        paddleA.moveUP(5)#...to idziemy w gore o 5 pikseli jej
    if keys[pygame.K_s]:#jesli klawisz wcisniety to"s"...
        paddleA.moveDOWN(5)#...to idziemy w dol o 5 pikseli jej

    if keys[pygame.K_UP]:#jesli klawisz wcisniety to"strzalka w gore"...
        paddleB.moveUP(5)#...to idziemy w gore o 5 pikseli jej
    if keys[pygame.K_DOWN]:#jesli klawisz wcisniety to"strzalka w dol"...
        paddleB.moveDOWN(5)#...to idziemy w dol o 5 pikseli jej

    all_sprites_list.update() #odswiezamy obiekty w liscie ze spritami (chyba wlasnie po to by przy ich kolejnym rysowaniu mialy swoje nowe pozycje)

    #sprawdzamy czy pileczka odbija sie od sciany jakiejs w tej "klatce"
    #wsm fun fact zauwaz ze robimy to po przemieszczeniu paletek bo to wlasnie gracz powinien miec pierwszenstwo a nie pileczka, inaczej moglo by to byc irytujace w przypdaku lagow
    if ball.rect.x>=690:#prawa sciana
        scoreA+=1#gracz po lewej zdobywa punkt
        ball.rect.x = 350
        ball.rect.y = 250
        ball.velocity[0] = -ball.velocity[0]#jesli pileczka zbliza sie do sciany(zauwaz ze mamy zapas 10 pikseli bo pileczka ma predkosc maksymalna bodajze 8 wiec tak jakby chcemy byc pewni ze nie wyleci poza mape jednym dlugim skokiem z np. 695 na 703) nadajemy jej przseciwnego kierunku/zwrotu (wsm to sazm juz nwm ktore to ktore xd)
    #anyway to co wyzej tyczy sie tez tych ponizej
    if ball.rect.x<=0:#lewa sciana
        scoreB+=1#gracz po prawej zdobywa punkt
        ball.rect.x = 350
        ball.rect.y = 250
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>=490:#sufit
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<=10:#podloga
        ball.velocity[1] = -ball.velocity[1]
    

    #jesli dojdzie do zderzenia z paletka:
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball,paddleB):#jesli polozenia dwoch podanych spritow sie pokrywaja to...
        ball.bounce()#...wywouljemy funkcje bounce z klasy Ball
        new_ball = ball.after_bounce()
        all_sprites_list.add(new_ball)
        all_sprites_list.update()
        if new_ball.rect.x>=690:#prawa sciana
            scoreA+=1#gracz po lewej zdobywa punkt
            new_ball.rect.x = 350
            new_ball.rect.y = 250
            new_ball.velocity[0] = -ball.velocity[0]#jesli pileczka zbliza sie do sciany(zauwaz ze mamy zapas 10 pikseli bo pileczka ma predkosc maksymalna bodajze 8 wiec tak jakby chcemy byc pewni ze nie wyleci poza mape jednym dlugim skokiem z np. 695 na 703) nadajemy jej przseciwnego kierunku/zwrotu (wsm to sazm juz nwm ktore to ktore xd)
    #anyway to co wyzej tyczy sie tez tych ponizej
        if new_ball.rect.x<=0:#lewa sciana
            scoreB+=1#gracz po prawej zdobywa punkt
            new_ball.rect.x = 350
            new_ball.rect.y = 250
            new_ball.velocity[0] = -ball.velocity[0]
        if new_ball.rect.y>=490:#sufit
            new_ball.velocity[1] = -ball.velocity[1]
        if new_ball.rect.y<=10:#podloga
            new_ball.velocity[1] = -ball.velocity[1]
  
    
  
    

    #"renderowanie"
    screen.fill(BLACK)#"restartujemy klatke"
    pygame.draw.line(screen, PINK, [349,0], [349, 500], 10)#rysujemy linię po srodku
    all_sprites_list.draw(screen)#rysujemy nasze spritey

    #wysywietlamy wynik:
    font= pygame.font.Font(None, 74)#czcionka
    text = font.render(str(scoreA),1,PINK)#"tworzymy"(ale jeszcze nie wysiwetlamy) wynik gracza lewego
    screen.blit(text, (250,10))#teraz go wyswietlamy dopiero
    text = font.render(str(scoreB),1,PINK)#tworzymy wynik gracza prawego...
    screen.blit(text, (420,10))# i go wsywietlamy


    pygame.display.flip()#teraz wyswietlamy wszystko na ekranie

    clock = pygame.time.Clock()
    clock.tick(60)#to powinno dac limit klatek nma 60 fps ale nwm czemu clock nie dziala :( ||||jednak dziala, trzeba bylo dac ta linijke wyzej by go tak jakby "stworzyc" :)

pygame.quit