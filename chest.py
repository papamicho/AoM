#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Chest class

 by: gNrg
"""
import pygame

from spritesheet_functions import SpriteSheet

class Chest(pygame.sprite.Sprite):
 
    def __init__(self, hearts_needed):
        super().__init__()
 
        # Grab the images for the chest
        sprite_sheet = SpriteSheet("Assets/Chest.png")
        self.images = [ sprite_sheet.get_image(0, 0, 58, 58), # Closed chest
        				sprite_sheet.get_image(58, 0, 58, 58), # Opened chest
        				sprite_sheet.get_image(116, 0, 58, 58)] # Empty chest
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.hearts_needed = hearts_needed
        self.status = "CLOSED"

    def open_chest(self):
    	self.image = self.images[1]

    def empty(self):
    	self.image = self.images[2]