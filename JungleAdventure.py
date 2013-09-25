#! /usr/bin/env python2

import pygame as pg

white = (255, 255, 255)
green = (0,255,0)
black = (0,0,0)
game = True;	    # flag

# Creates the 
class blob(pg.sprite.Sprite):
    def __init__(self, colour, width, height):
	pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.image.fill(colour)

pg.init()   # initialize pygame

# set up the screen
pg.display.set_caption('Jungle Adventure')
size = [600, 400]
scr = pg.display.set_mode(size)

clock = pg.time.Clock()

# Creates a list of players so that they can be rendered
sprites = pg.sprite.RenderPlain()
# Creates a player
slash = blob(black, 25, 25)
# Adds player to the list sprites
sprites.add(slash)

# Key repeating
pg.key.set_repeat(100, 5)

# main game loop
while (game):
    sprites.draw(scr)
    clock.tick(20)
    pg.display.flip()
    scr.fill(white)

    # Checks for keyboard input
    for event in pg.event.get():	# checks pygame events
	if event.type == pg.KEYDOWN:	# in the case of a keydown event
	    if event.key == pg.K_q:	# if the key is q
		game = False		# quit the current game
            elif event.key == pg.K_w:
                slash.rect.y -= 3
            elif event.key == pg.K_s:
                slash.rect.y += 3
            elif event.key == pg.K_d:
                slash.rect.x += 3
            elif event.key == pg.K_a:
                slash.rect.x -=3

pg.quit()
