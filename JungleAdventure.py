#! /usr/bin/env python2

import pygame as pg

white = (255, 255, 255)
black = (0,0,0)
game = True;	    # flag

pg.init()   # initialize pygame

# set up the screen
pg.display.set_caption('Jungle Adventure')
size = [600, 400]
scr = pg.display.set_mode(size)

# main game loop
while (game):

    # Checks for keyboard input
    for event in pg.event.get():	# checks pygame events
	if event.type == pg.KEYDOWN:	# in the case of a keydown event
	    if event.key == pg.K_q:	# if the key is q
		game = False		# quit the current game

