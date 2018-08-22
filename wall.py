#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Wall class

 by: gNrg
"""
import pygame

from spritesheet_functions import SpriteSheet

class Wall(pygame.sprite.Sprite):
 
    def __init__(self, index):
        super().__init__()
 
        # Grab the images for the door
        sprite_sheet = SpriteSheet("Assets/Wall.png")
        self.images = [sprite_sheet.get_image(0, 0, 58, 58), # Shadow wall
        				sprite_sheet.get_image(58, 0, 58, 58)] # Normal wall
        self.image = self.images[index]
        self.rect = self.image.get_rect()
