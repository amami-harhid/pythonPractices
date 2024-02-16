# This is a sample Pygame script.
import asyncio
import pygame
import random
from pygame.locals import *
from ball import *
from mixer import *

# static variables
class Window_size :
    width = 1200
    height = 800


pygame.init()
soundPlay()

screen = pygame.display.set_mode( ( Window_size.width, Window_size.height ) )
pygame.display.set_caption('Jumping Ball!')
clock = pygame.time.Clock()

tmpSurface = pygame.Surface( ( Window_size.width, Window_size.height ) )

#print(display_window.get_width())

FPS = 60

x = 100
y = 700

ballArr = []

for i in range(50):
    ball = Ball(screen)
    _x = random.randint( 0, Window_size.width )
    _y = random.randint( 600, Window_size.height)
    _r = random.randint( 10, 30 )
    _power = random.randint( 10, 40 )
    ball.setXY( _x,  _y )
    ball.setPower( _power )
    ball.setRadius( _r )
    ballArr.append( ball )

screenColor = Color((100,0,100))

screen.fill( screenColor )
tmpSurface.blit(screen, ( 0, 0 ))

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        # transfer from screen to tmpSurface
        tmpSurface.blit(screen, (0,0))
        # cover the tmpSurface with a white square
        pygame.draw.rect( tmpSurface, screenColor, Rect(0,0, Window_size.width, Window_size.height)  )
        
        # make blur-effect, set alpha = 150 ( alpha : 0 ～ 255 )
        tmpSurface.set_alpha(20)
        
        # transfer from tmpSurface to screen
        screen.blit(tmpSurface, (0,0))
        
        # draw balls on the screen
        for ball in ballArr:
            ball.draw(screen)
        pygame.display.flip()

        #         
        clock.tick( FPS )
        
        # sleep to avoid browser freezes
        await asyncio.sleep(0)
    
asyncio.run(main())
