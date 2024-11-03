print('hello world')
import pygame as pg
import sys

pg.init()

BLACK=(255,255,255)
WHITE=(0,0,0)

SCREEN_WIDTH=600
SCREEN_HEIGHT=800

def_font = pg.font.Font(pg.font.get_default_font(),30)

TOP_BORDER = pg.Rect(0,0,SCREEN_WIDTH, 1)
BOTTOM_BORDER = pg.Rect(0,SCREEN_HEIGHT,SCREEN_WIDTH,1)
LEFT_BORDER = pg.Rect(0,0,1,SCREEN_HEIGHT)
RIGHT_BORDER = pg.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT)
PLATFORM_WIDTH=200
PLATFORM_HEIGHT=30


def game(screen, Clock):


    PLATFORM_X=(SCREEN_WIDTH+PLATFORM_WIDTH) //2
    PLATFORM_Y=int(SCREEN_HEIGHT*0.75)
    PLATFORM_SPEED=3
    BALL_WIDTH=40
    BALL_HEIGHT=40 

    FPS=120

    BALL_X=50
    BALL_Y=50
    BALL_SPEED=5
    BALL_DIRECTION=pg.math.Vector2(1,1).normalize()

    COUNTER = 0


    


    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                sys.exit()

        keys=pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            PLATFORM_X-=PLATFORM_SPEED
            PLATFORM_X=max(0,PLATFORM_X)
        if keys[pg.K_RIGHT]:
            PLATFORM_X+=PLATFORM_SPEED
            PLATFORM_X=min(SCREEN_WIDTH-PLATFORM_WIDTH,PLATFORM_X)


        speed_vector = BALL_DIRECTION*BALL_SPEED
        BALL_Y+=speed_vector.y
        BALL_X+=speed_vector.x

        screen.fill(WHITE)

        platform=pg.Rect(PLATFORM_X,PLATFORM_Y,PLATFORM_WIDTH,PLATFORM_HEIGHT)
        pg.draw.rect(screen,BLACK,platform)
        ball=pg.Rect(BALL_X,BALL_Y,BALL_WIDTH,BALL_HEIGHT)
        pg.draw.rect(screen, (255,0,0),ball)


        ball_centre = (BALL_X + BALL_WIDTH/2,BALL_Y + BALL_HEIGHT/2)
        platform_centre =(PLATFORM_X + PLATFORM_WIDTH/2, PLATFORM_Y + PLATFORM_HEIGHT/2)
        text_surface = def_font.render(str(COUNTER),False,(0,255,0))

        
        if ball.colliderect(platform):
            collision_vector = (ball_centre[0] - platform_centre[0],ball_centre[1] - platform_centre[1])
            BALL_DIRECTION=pg.math.Vector2(collision_vector).normalize()
            COUNTER += 1
        if ball.colliderect(TOP_BORDER):
            BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(0,1))
        if ball.colliderect(BOTTOM_BORDER):
            BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(0,-1))
            break
        if ball.colliderect(LEFT_BORDER):
            BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(1,0))
        if ball.colliderect(RIGHT_BORDER):
            BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(-1,0))
        

        screen.blit(text_surface,(20,20))
        pg.display.flip() 
        Clock.tick(FPS)



if __name__ == '__main__':
    screen_out=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Clock_out=pg.time.Clock()
    while True:
        game(screen_out, Clock_out)

        finish_text = def_font.render('Game over', False, (0, 255 ,0))
        screen_out.blit(finish_text, (SCREEN_WIDTH/2-30, SCREEN_HEIGHT/2))
        pg.display.flip()
        while True:
            for event in pg.event.get(): 
                if event.type==pg.QUIT:
                    sys.exit()
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                break