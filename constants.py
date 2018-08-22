#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Gloabal Constants

 by: gNrg
"""
import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_SIZE = 754
MENU_SIZE = 870

# User events
BROKE_EGG = pygame.USEREVENT + 1
REMOVE_EGG = pygame.USEREVENT + 2
EGG_TIME = 4000

# Enemy status
# 0 = INIT, 1 = EGG, 2 = BREAKING EGG, 3 = DISAPPEAR, 4 = ATTACK
ENEMY_INIT = 0
ENEMY_EGG = 1
ENEMY_BREAKING_EGG = 2
ENEMY_DISAPPEAR = 3
ENEMY_ATTACK = 4

# Menus & Screens between leves
LOADING_SCREEN = 0
MAIN_MENU = 1
COMPLETED_LEVEL = 2
MANOLITO_DIED = 3

# Main menu buttons
# BUTTON  =  [ [ x min, x max ] , [ y min, y max ] ]
START_GAME = [[374, 749],[183, 280]]
MUST_DIE = [[374, 749],[295, 390]]
INSTRUCTIONS = [[374, 749],[407, 502]]
OPTIONS = [[374, 749],[520, 615]]
EXIT_GAME = [[374, 749],[633, 727]]

