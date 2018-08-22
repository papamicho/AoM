#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Shot class

 by: gNrg
"""
import pygame

from spritesheet_functions import SpriteSheet

class Door(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        # Grab the images for the door
        sprite_sheet = SpriteSheet("Assets/Door.png")
        self.images = [sprite_sheet.get_image(0, 0, 174, 58), # Closed door
        				sprite_sheet.get_image(0, 58, 174, 116)] # Opened door
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def open_door(self):
    	self.image = self.images[1]