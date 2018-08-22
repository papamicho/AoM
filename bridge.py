#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Bridge class

 by: gNrg
"""
import pygame

from spritesheet_functions import SpriteSheet

class Bridge(pygame.sprite.Sprite):
 
    def __init__(self, direction):
        super().__init__()
 
        sprite_sheet = SpriteSheet("Assets/Bridge.png")
        self.images = [sprite_sheet.get_image(0, 0, 58, 58),
        				sprite_sheet.get_image(58, 0, 58, 58)]
        if direction == "VERTICAL":
        	self.image = self.images[0]
        else:
        	self.image = self.images[1]
        self.rect = self.image.get_rect()
