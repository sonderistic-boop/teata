import pygame as pg


pg.init() # initialises pg


themeColours = {
    "RED" : "#d14242",
    "GREEN" : "#52d142",
    "BLUE" : "#52d142",
    "YELLOW" : "#e1c16e",
    "CYAN" : "#03b9b9",
    "MAGENTA" : "#674ea7",
    "ORANGE" : "#e69138"

}

maxTicks = 60
(WIDTH,HEIGHT) = (600,600)
window = pg.display.set_mode((WIDTH,HEIGHT)) # width, height
pg.display.set_caption("PyBall")

clock = pg.time.Clock()

def runtime():

    running = True
    while running:
        clock.tick(maxTicks)

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    running = False
            
        window.fill((themeColours["GREEN"]))
        pg.display.flip()

runtime()