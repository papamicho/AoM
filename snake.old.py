#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Snake class

 by: gNrg
"""
import pygame
import constants
from spritesheet_functions import SpriteSheet

class Snake(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
        self.player = None
        self.direction = None
        self.status = constants.ENEMY_INIT
        self.change_status_time = 0

        # Grab the images for the snake
        sprite_sheet0 = SpriteSheet("Assets/Snake.png")
        sprite_sheet1 = SpriteSheet("Assets/Egg.png")
        self.snake_images = [sprite_sheet0.get_image(0, 0, 58, 58), # Medium Left
        				sprite_sheet0.get_image(58, 0, 116, 58), # Left
                        sprite_sheet0.get_image(0, 58, 58, 116), # Medium Right
                        sprite_sheet0.get_image(58, 58, 116, 116)] #Right
        self.egg_images = [sprite_sheet1.get_image(0, 0, 58, 58), # Medium Left
                        sprite_sheet1.get_image(58, 0, 116, 58)] # Left
        
        self.image = self.snake_images[0]

        self.rect = self.image.get_rect()


    def update(self):
        # Move the snake (ATTACK STATUS)
        if self.status = constants.ENEMY_EGG:

        if self.status == constants.ATTACK:
            if self.player.rect.x < self.rect.x:
                self.image = self.snake_images[1]
            elif self.player.rect.x > self.rect.x:
                self.image = self.snake_images[2]
            elif self.player.rect.y < self.rect.y:
                self.image = self.snake_images[0]
            else:
                self.image = self.snake_images[3]
        elif self.status == 1:
            self.image = self.egg_images[0]
        elif self.status == 2:
            self.image = self.egg_images[1]
        else:
            self.image = self.snake_images[0]

    def set_egg(self):
        """ Called when the player shots the snake. """
        self.image = self.egg_images[0]
        self.status = constants.ENEMY_EGG
        self.change_status_time = pygame.time.get_ticks()
        pygame.time.set_timer(constants.BROKE_EGG, constants.EGG_TIME)

    def broke_egg(self):
        """ Called when broke egg event is throwed. """
        self.image = self.egg_images[1]
        self.status = constants.ENEMY_BREAKING_EGG
        self.change_status_time = pygame.time.get_ticks()
        pygame.time.set_timer(constants.BROKE_EGG, 0)
        pygame.time.set_timer(constants.REMOVE_EGG, constants.EGG_TIME)

    def remove_egg(self):
        """ Called when remove egg event is throwed. """
        self.image = self.egg_images[1]
        self.status = constants.ENEMY_INIT
        self.change_status_time = 0
        pygame.time.set_timer(constants.REMOVE_EGG, 0)

    def get_status(self):
        return self.status