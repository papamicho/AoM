#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Water class

 by: gNrg
"""
import pygame

from spritesheet_functions import SpriteSheet

class Water(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        # Grab the images for the door
        sprite_sheet = SpriteSheet("Assets/Water.png")
        self.images = [sprite_sheet.get_image(0, 0, 58, 58),
        				sprite_sheet.get_image(58, 0, 58, 58),
        				sprite_sheet.get_image(116, 0, 58, 58),
        				sprite_sheet.get_image(174, 0, 58, 58)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
