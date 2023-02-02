import pygame as pg
import math
#import twisted
#import numpy as np

import sys # for sys.exit()


from entities.pawn import Pawn
from entities.ball import Ball
import logic.collisions as collisions

pg.init() # initialises pg

#the colours used in the game

themeColours = {
    "red" : "#d14242",
    "green" : "#52d142",
    "blue" : "#426ad1",
    "yellow" : "#e1c16e",
    "cyan" : "#03b9b9",
    "magenta" : "#674ea7",
    "orange" : "#e69138"

}
#the maximum number of ticks per second
maxTicks = 120

screen = pg.display.set_mode((1200,600),pg.SRCALPHA) # width, height
pg.display.set_caption("PyBall")


#need to set up a stadium class for future stadiums
field = pg.image.load("./assets/tiles/fieldtiles/fieldtile.jpg")

#the clock object
clock = pg.time.Clock()

def runtime():
    #the main function
    running = True
    newball = Ball(screen,(200,200),(40,40))
    newguy = Pawn("bigboyo","red",True,screen,(400,400),(93.75,93.75))
    newguy2 = Pawn("bigbayo","blue",True,screen,(800,400),(93.75,93.75))
    guygroup =  (pg.sprite.GroupSingle(newguy))
    ballgroup = (pg.sprite.GroupSingle(newball))
    guygroup2 = (pg.sprite.GroupSingle(newguy2))
    while running:
        #while running is true, the game will run
       
        clock.tick(maxTicks)

        for event in pg.event.get():
            #event handling loop
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    sys.exit()


                
        keys = pg.key.get_pressed()
        newguy.velocity[0] += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 0.1
        newguy.velocity[1] += (keys[pg.K_DOWN] - keys[pg.K_UP]) * 0.1

        newguy2.velocity[0] += (keys[pg.K_d] - keys[pg.K_a]) * 0.1
        newguy2.velocity[1] += (keys[pg.K_s] - keys[pg.K_w]) * 0.1

        
        collide = pg.sprite.spritecollide(newball, guygroup, False, pg.sprite.collide_mask)

        if keys[pg.K_l] and collide:
            collisions.thrust(newball,newguy)

        if collide:
            collisions.collision_ball(newguy,newball)

        collide2 = pg.sprite.spritecollide(newball, guygroup2, False, pg.sprite.collide_mask)
        
        if keys[pg.K_x] and collide2:
            collisions.thrust(newball,newguy2)
        if collide2:
            collisions.collision_ball(newguy2,newball)

        collide3 = pg.sprite.spritecollide(newguy, guygroup2, False, pg.sprite.collide_mask)
        
        if collide3:
            collisions.collision_ball(newguy2,newguy)
            
        screen.fill((themeColours["green"]))
        #screen.fill((255, 0, 0) if collide else (255, 255, 255))
        
        #screen.blit(field,(20,20))
        newguy.updatePhysics()
        newball.updatePhysics()
        newguy2.updatePhysics()
        newball.render()
        print(newguy.velocity)
        newguy.render()
        newguy2.render()
        
        pg.display.flip()
       

#def collisionHandler():
    
    



if __name__ == "__main__":
    runtime()
