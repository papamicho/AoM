#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Enemy class

 by: gNrg
"""
import pygame
import constants
from spritesheet_functions import SpriteSheet
from collisionManager import CollisionManager

class Enemy(pygame.sprite.Sprite):
 
    def __init__(self, player, level):
        super().__init__()
        self.player = player
        self.level = level
        self.direction = None
        self.status = constants.ENEMY_INIT
        self.change_status_time = 0

        self.collisionManager = CollisionManager(self)

        # Grab the images for the snake
        self.sprite_sheet0 = None
        self.sprite_sheet1 = None

        # Egg images
        self.sprite_sheet1 = SpriteSheet("Assets/Egg.png")
        self.egg_images = [self.sprite_sheet1.get_image(0, 0, 58, 58),
                        self.sprite_sheet1.get_image(58, 0, 116, 58)]
        
        self.image = None
        self.rect = None

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.collisionManager.fixed_objects(self.level.walls_list)
        self.collisionManager.fixed_objects(self.level.door_list)
        self.collisionManager.fixed_objects(self.level.artifact_list)
        self.collisionManager.fixed_objects(self.level.water_list)
        self.collisionManager.fixed_objects(self.level.block_list)
        self.collisionManager.fixed_objects(self.level.chest_list)

    def set_egg(self):
        """ Called when the player shots the enemy. """
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