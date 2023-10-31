import pygame as pg
from sys import exit
pg.init()

width, height = 800, 400

win = pg.display.set_mode((width, height))
pg.display.set_caption("Snail")

clock = pg.time.Clock()
font = pg.font.Font("Pixeltype.ttf", 50) #font type, font size | None is default

sky = pg.image.load("Sky.png")
ground = pg.image.load("ground.png")
textSurface = font.render("Snail", False, "#000000")   #text, antialias, color

snail = pg.image.load("snail1.png")
snailX = 600

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    win.blit(sky, (0, 0))
    win.blit(ground, (0, 300))
    win.blit(textSurface, (300, 50))
    snailX -= 4
    if snailX < -100: snailX = 800
    win.blit(snail, (snailX, 265))
    
    pg.display.update()
    clock.tick(60)
