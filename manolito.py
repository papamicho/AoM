#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Player class

 by: gNrg
"""
import pygame
 
import constants
from collisionManager import CollisionManager
from spritesheet_functions import SpriteSheet
import bullet
 
class Manolito(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
    def __init__(self):
        # Call the parent's constructor
        super().__init__()
 
        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
        
        self.lives = 5
        self.shots = 0

        self.collisionManager = CollisionManager(self)

        # This holds all the images for the animated walk of manolito
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []
 
        # What direction is manolito facing?
        self.direction = "D"
 
        self.level = None
        self.level_end = False
        self.hearts_collected = 0
        self.gem = False
 
        sprite_sheet = SpriteSheet("Assets/manolito.png")
        # Load all the down facing images into a list
        image = sprite_sheet.get_image(0, 0, 58, 58)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(58, 0, 58, 58)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(116, 0, 58, 58)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(174, 0, 58, 58)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(232, 0, 58, 58)
        self.walking_frames_d.append(image)

        # Load all the left facing images into a list
        image = sprite_sheet.get_image(0, 58, 58, 58)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(58, 58, 58, 58)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(116, 58, 58, 58)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(174, 58, 58, 58)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(232, 58, 58, 58)
        self.walking_frames_l.append(image)

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 116, 58, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(58, 116, 58, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(116, 116, 58, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(174, 116, 58, 58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(232, 116, 58, 58)
        self.walking_frames_r.append(image)

        # Load all the up facing images into a list
        image = sprite_sheet.get_image(0, 174, 58, 58)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(58, 174, 58, 58)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(116, 174, 58, 58)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(174, 174, 58, 58)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(232, 174, 58, 58)
        self.walking_frames_u.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_d[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = 58
        self.rect.y = 58
 
    def update(self):
        # Move the player
        self.rect.x += self.change_x
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 29) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 29) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        self.rect.y += self.change_y
        pos = self.rect.y
        if self.direction == "U":
            frame = (pos // 29) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        elif self.direction == "D":
            frame = (pos // 29) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]
        
        # Wall & door collisions
        if not self.gem: 
            self.collisionManager.fixed_objects(self.level.walls_list)
            self.collisionManager.fixed_objects(self.level.door_list)
        else:
            block_hit_list = pygame.sprite.spritecollide(self, self.level.door_list, False, pygame.sprite.collide_rect_ratio(0.1)) 
            if block_hit_list != []:
                self.level_end = True

        # Artifact collisions
        self.collisionManager.fixed_objects(self.level.artifact_list)

        # Water
        self.collisionManager.fixed_objects(self.level.water_list)

        # Green blocks
        self.collisionManager.green_blocks(self.level.block_list)

        # Collect hearts
        block_hit_list = pygame.sprite.spritecollide(self, self.level.hearts_list, True, pygame.sprite.collide_rect_ratio(0.1))
        for block in block_hit_list:
            self.hearts_collected += 1
            if block.bonus > 0: 
                self.shots = block.bonus
            # When all hearts are collected, change the status of the enemies
            if self.hearts_collected == self.level.hearts_needed:
                for enemy in self.level.enemy_list:
                    if enemy.status == 0:
                        enemy.status = constants.ENEMY_ATTACK

        # Chest collisions
        if self.hearts_collected < self.level.hearts_needed:
            self.collisionManager.fixed_objects(self.level.chest_list)
        elif self.gem == False:
            block_hit_list = pygame.sprite.spritecollide(self, self.level.chest_list, False, pygame.sprite.collide_rect_ratio(0.1))
            for block in block_hit_list:
                self.gem = True
                self.level.enemy_list.empty() # Remove enemies

        # Snake collisions
        self.collisionManager.snakes(self.level.enemy_list)



        self.change_x = 0
        self.change_y = 0
 
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -29
        self.change_y = 0
        self.direction = "L"
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 29
        self.change_y = 0
        self.direction = "R"

    def go_up(self):
        """ Called when the user hits the up arrow. """
        self.change_y = -29
        self.change_x = 0
        self.direction = "U"

    def go_down(self):
        """ Called when the user hits the down arrow. """
        self.change_y = 29
        self.change_x = 0
        self.direction = "D"

    def shot(self, sound):
        """ Called when the user hits space. """
        if self.shots > 0 and self.level.shot_list.sprites() == []:
            self.shots -= 1
            sound.play()
            bullet.Bullet(self, self.level)

    def end_level(self):
        self.shots = 0
        self.gem = False
        self.hearts_collected = 0
        self.level_end = False
