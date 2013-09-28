#! /usr/bin/env python2
#--------------------------------------------------------------------
#
# Programmed By:  Sophia Castellarin, 
#                 Ji Won (Veronica) Kim
# Program Description: A silly game made using python and pygame.
#                      If you want a lot more info, you should read
#                      the README (we made that for a reason) or make
#                      up yourselves!
#
#----------------------------------------------------------------------- 

import pygame as pg

white = (255, 255, 255)
green = (0,255,0)
black = (0,0,0)
game = True	    # flag
score = 0	    # player score

# Class for creating sprites 
class blob(pg.sprite.Sprite):
    def __init__(self, colour, width, height):
	pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.image.fill(colour)

# A class that defines the food objects
class eat(pg.sprite.Sprite):
    val = 0;

    def __init__(self, x_pos, y_pos, value):
	pg.sprite.Sprite.__init__(self)

	self.image = pg.Surface([20, 20])
	self.rect = self.image.get_rect()
	self.rect.x = x_pos
	self.rect.y = y_pos
	self.image.fill(green)

	val = value


pg.init()   # initialize pygame

# set up the screen
pg.display.set_caption('Jungle Adventure')
size = [600, 600]
scr = pg.display.set_mode(size)

clock = pg.time.Clock()

# Creates a list of players/items/obst so that they can be rendered
player = pg.sprite.RenderPlain() 
items = pg.sprite.RenderPlain()
  
slash = blob(black, 25, 25)	    # Creates a player
cookie = eat(10, 10, 10)	    # Creates a food object

# Creates font object so that we can show the user the score
font = pg.font.Font(None, 25)   # Creates font object

# Adds player to the list sprites
player.add(slash)
items.add(cookie)

# Key repeating
pg.key.set_repeat(100, 1)

# Checks for collisions between the player and obst or items
def check_collisions():
    global score
    pl_it = pg.sprite.groupcollide(player, items, False, True, None)  

    if pl_it != {}:
	score += 1
	print "collided with " + str(pl_it)
    else:
	pass
	


# main game loop
while (game):
    player.draw(scr)	# draws the sprites to the screen
    items.draw(scr)
    clock.tick(60)	# refreshes the screen
    pg.display.flip()
    scr.fill(white)	# fills the screen background to white

    check_collisions()

    # Checks for keyboard input
    for event in pg.event.get():	# checks pygame events
	if event.type == pg.KEYDOWN:	# in the case of a keydown event
	    if event.key == pg.K_q:	# if the key is q
		game = False		# quit the current game
            elif event.key == pg.K_UP:
                slash.rect.y -= 12
            elif event.key == pg.K_DOWN:
                slash.rect.y += 12
            elif event.key == pg.K_RIGHT:
                slash.rect.x += 12
            elif event.key == pg.K_LEFT:
                slash.rect.x -= 12

    output = "Score: " + str(score) 
    dis_score = font.render(output, True, black)
    scr.blit(dis_score, [450, 0]) 
pg.quit()
