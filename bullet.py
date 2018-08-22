#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Bullet class

 by: gNrg
"""
import pygame
from collisionManager import CollisionManager
from spritesheet_functions import SpriteSheet

class Bullet(pygame.sprite.Sprite):
 
    def __init__(self, player, level):
        super().__init__()

        self.collisionManager = CollisionManager(self)

        # Set bullet speed vector
        self.change_x = 0
        self.change_y = 0
        self.direction = None

        # Grab the images for the bullet
        sprite_sheet = SpriteSheet("Assets/Bullet.png")
        self.images = [sprite_sheet.get_image(0, 0, 58, 58), # Closed door
        				sprite_sheet.get_image(58, 0, 116, 58)] # Opened door
        
        self.player = player
        if self.player.direction == "D":
            self.image = self.images[0]
            self.direction = "D"
        elif self.player.direction == "U":
            self.image = self.images[0]
            self.direction = "U"
        elif self.player.direction == "L":
            self.image = self.images[1]
            self.direction = "L"
        else: 
            self.image = self.images[1]
            self.direction = "R"
        self.rect = self.image.get_rect()

        self.level = level
        block = self
        block.rect.x = self.player.rect.x
        block.rect.y = self.player.rect.y
        block.player = self.player
        self.level.shot_list.add(block)

    def update(self):
        # Move the bullet
        if self.direction == "R":
            self.go_right()
        elif self.direction == "L":
            self.go_left()
        if self.direction == "U":
            self.go_up()
        elif self.direction == "D":
            self.go_down()
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Walls, artifacts & door collisions
        if self.collisionManager.fixed_objects(self.level.walls_list) or self.collisionManager.fixed_objects(self.level.door_list) or self.collisionManager.fixed_objects(self.level.artifact_list):
            self.level.shot_list.empty()
        self.change_x = 0
        self.change_y = 0

        # Enemies collisions
        block_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        b = None
        flag = False
        for block in block_hit_list:
            self.level.shot_list.remove(self)
            flag = True
            b = block
        if flag:
            if b.get_status() == 0 or b.get_status() == 4:
                b.set_egg()
            elif b.get_status() == 1 or b.get_status() == 2:
                self.level.enemy_list.remove(b)
                b.status = 3

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.image = self.images[1]
        self.change_x = -29
        self.change_y = 0
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.image = self.images[1]
        self.change_x = 29
        self.change_y = 0

    def go_up(self):
        """ Called when the user hits the up arrow. """
        self.image = self.images[0]
        self.change_y = -29
        self.change_x = 0

    def go_down(self):
        """ Called when the user hits the down arrow. """
        self.image = self.images[0]
        self.change_y = 29
        self.change_x = 0