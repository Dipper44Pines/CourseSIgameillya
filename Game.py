print('hello world')
import pygame as pg
import sys
BLACK=(255,255,255)
WHITE=(0,0,0)

SCREEN_WIDTH=600
SCREEN_HEIGHT=800
screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
Clock=pg.time.Clock()

PLATFORM_WIDTH=200
PLATFORM_HEIGHT=30
PLATFORM_X=(SCREEN_WIDTH+PLATFORM_WIDTH) //2
PLATFORM_Y=int(SCREEN_HEIGHT*0.75)
PLATFORM_SPEED=3

BALL_WIDTH=60
BALL_HEIGHT=60
BALL_X=50
BALL_Y=50
BALL_SPEED=3
BALL_DIRECTION=pg.math.Vector2(1,1).normalize()
TOP_BORDER = pg.Rect(0,0,SCREEN_WIDTH, 1)
BOTTOM_BORDER = pg.Rect(0,SCREEN_HEIGHT,SCREEN_WIDTH,1)
LEFT_BORDER = pg.Rect(0,0,1,SCREEN_HEIGHT)
RIGHT_BORDER = pg.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT)

FPS=120

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

    
    if ball.colliderect(platform):
        BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(0,1))
    if ball.colliderect(TOP_BORDER):
        BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(0,1))
    if ball.colliderect(BOTTOM_BORDER):
        BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(0,-1))
    if ball.colliderect(LEFT_BORDER):
        BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(1,0))
    if ball.colliderect(RIGHT_BORDER):
        BALL_DIRECTION=BALL_DIRECTION.reflect(pg.math.Vector2(1,0))

    if BALL_Y <0:
        BALL_SPEED =- BALL_SPEED

    if BALL_Y >750:
        BALL_SPEED =- BALL_SPEED
        sys.exit()

    pg.display.flip() 
    Clock.tick(FPS) 

    
