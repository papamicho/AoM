#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Snake class

 by: gNrg
"""
import pygame
import constants
from spritesheet_functions import SpriteSheet
from enemy import Enemy

class Snake(Enemy):
 
    def __init__(self, player, level):
        super().__init__(player, level)
        self.direction = None
        self.status = constants.ENEMY_INIT

        # Grab the images for the snake
        self.sprite_sheet0 = SpriteSheet("Assets/Snake.png")

        self.images = [self.sprite_sheet0.get_image(0, 0, 58, 58), # Medium Left
        				self.sprite_sheet0.get_image(58, 0, 116, 58), # Left
                        self.sprite_sheet0.get_image(0, 58, 58, 116), # Medium Right
                        self.sprite_sheet0.get_image(58, 58, 116, 116)] #Right

        self.image = self.images[0]
        self.rect = self.image.get_rect()


    def update(self):
        super().update()
        if self.status == constants.ENEMY_ATTACK:
            if self.player.rect.x < self.rect.x:
                self.image = self.images[1]
            elif self.player.rect.x > self.rect.x:
                self.image = self.images[2]
            elif self.player.rect.y < self.rect.y:
                self.image = self.images[0]
            else:
                self.image = self.images[3]
        elif self.status == 1:
            self.image = self.egg_images[0]
        elif self.status == 2:
            self.image = self.egg_images[1]
        else:
            self.image = self.images[0]