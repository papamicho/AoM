#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 by: gNrg
"""
 
import pygame

import constants
import levels
from manolito import Manolito

pygame.init()

# Loading
screen = pygame.display.set_mode([1366, 768])
pygame.display.set_caption('Adventures of Manuel (by gNrg)')
clock = pygame.time.Clock()
background = pygame.image.load("Assets/Screens/Loading.png").convert()
screen.blit(background, [0, 0])
pygame.display.flip()
pygame.time.delay(1000)

# Start Menu
background = pygame.image.load("Assets/Screens/MainMenu.png").convert()
screen.blit(background, [0, 0])
pygame.display.flip()
pygame.mixer.music.load("Sounds/menu.mp3")
pygame.mixer.music.play(-1)
option = [True, 1]
while not option[0]:
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.QUIT:
			pygame.quit()
		# Check if any button is clicked
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if pos[0] >= constants.START_GAME[0][0] and pos[0] <= constants.START_GAME[0][1]:
				if pos[1] >= constants.START_GAME[1][0] and pos[1] <= constants.START_GAME[1][1]:
					option = [True, 1]
				elif pos[1] >= constants.MUST_DIE[1][0] and pos[1] <= constants.MUST_DIE[1][1]:
					option = [True, 2]
				elif pos[1] >= constants.INSTRUCTIONS[1][0] and pos[1] <= constants.INSTRUCTIONS[1][1]:
					option = [True, 3]
				elif pos[1] >= constants.OPTIONS[1][0] and pos[1] <= constants.OPTIONS[1][1]:
					option = [True, 4]
				elif pos[1] >= constants.EXIT_GAME[1][0] and pos[1] <= constants.EXIT_GAME[1][1]:
					pygame.quit()
pygame.mixer.music.stop()

screen = pygame.display.set_mode([constants.MENU_SIZE, constants.SCREEN_SIZE])
pygame.display.set_caption('Adventures of Manuel (by gNrg)')

# Hide the mouse cursor
pygame.mouse.set_visible(0)
# Player 
player = Manolito()

 # Create all the levels
level_list = []
level_list.append(levels.Level_01(player))
level_list.append(levels.Level_02(player))
 
# Set the current level
current_level_no = 0
current_level = level_list[current_level_no]

# Sprites
sprites = pygame.sprite.Group()
sprites.add(player)
current_level.set_player_position(current_level.posx, current_level.posy)

# Music & sounds
pygame.mixer.music.load("Sounds/levels.mp3")
pygame.mixer.music.play(-1)
manolito_shot_sound = pygame.mixer.Sound("Sounds/manolitosShot.ogg")

done = False
while not done:
	if player.level_end == True:
		current_level.completed(screen)
		current_level_no = current_level_no + 1
		current_level = level_list[current_level_no]
		current_level.set_player_position(current_level.posx, current_level.posy)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == constants.BROKE_EGG:
			current_level.broke_egg()
		if event.type == constants.REMOVE_EGG:
			current_level.remove_egg()

	keys = pygame.key.get_pressed()  #checking pressed keys
	if keys[pygame.K_ESCAPE]: 
		done = True
	if keys[pygame.K_UP]:
		if player.rect.y > 0: 
			player.go_up()
	if keys[pygame.K_DOWN]:
		if player.rect.y <= constants.SCREEN_SIZE - ((58*2)+1): 
			player.go_down()
	if keys[pygame.K_LEFT]:
		if player.rect.x > 58: 
			player.go_left()
	if keys[pygame.K_RIGHT]:
		if player.rect.x <= constants.SCREEN_SIZE - ((58*2)+1): 
			player.go_right()
	if keys[pygame.K_SPACE]:
		player.shot(manolito_shot_sound)


	player.level = current_level

	sprites.update()
	current_level.update(screen)
    
	current_level.draw(screen)
	sprites.draw(screen)
    
	pygame.display.flip()
	clock.tick(9)
 
pygame.quit()