#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Collision manager

 by: gNrg
"""
import pygame

import constants
 
class CollisionManager(object):
    """ Class used to manage collisions between sprites. """
    def __init__(self, obj):
        self.obj = obj
        self.flag = False

    def block_vs_object(self, o_list): # Green blocks vs objects
        block_hit_list = pygame.sprite.spritecollide(self.obj, o_list, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.obj.rect.right == block.rect.left:
                self.obj.rect.right = block.rect.left
            elif self.obj.rect.left == block.rect.right:
                # Otherwise if we are moving left, do the opposite.
                self.obj.rect.left = block.rect.right
            elif self.obj.rect.bottom == block.rect.top:
                self.obj.rect.bottom = block.rect.top
            elif self.obj.rect.top == block.rect.bottom:
                self.obj.rect.top = block.rect.bottom
            self.flag = True
        return self.flag

    def fixed_objects(self, o_list):
        block_hit_list = pygame.sprite.spritecollide(self.obj, o_list, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.obj.change_x > 0:
                self.obj.rect.right = block.rect.left
            elif self.obj.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.obj.rect.left = block.rect.right
            self.flag = True
        block_hit_list = pygame.sprite.spritecollide(self.obj, o_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.obj.change_y > 0:
                self.obj.rect.bottom = block.rect.top
            elif self.obj.change_y < 0:
                self.obj.rect.top = block.rect.bottom
            self.flag = True
        return self.flag

    def snakes(self, o_list):
        block_hit_list = pygame.sprite.spritecollide(self.obj, o_list, False)
        b = None
        for block in block_hit_list:
            if block.get_status() == 0 or block.get_status() == 4:
                # If we are moving right, set our right side to the left side of the item we hit
                if self.obj.change_x > 0:
                    self.obj.rect.right = block.rect.left
                elif self.obj.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.obj.rect.left = block.rect.right
            elif block.get_status() == 1 or block.get_status() == 2:
                if self.obj.change_x > 0:
                    block.rect.left = self.obj.rect.right
                elif self.obj.change_x < 0:
                    block.rect.right = self.obj.rect.left
            self.flag = True
            b = block
        block_hit_list = pygame.sprite.spritecollide(self.obj, o_list, False)
        for block in block_hit_list:
            if block.get_status() == 0 or block.get_status() == 4:
                if self.obj.change_y > 0:
                    self.obj.rect.bottom = block.rect.top
                elif self.obj.change_y < 0:
                    self.obj.rect.top = block.rect.bottom
            elif block.get_status() == 1 or block.get_status() == 2:
                if self.obj.change_y > 0:
                    block.rect.top = self.obj.rect.bottom
                elif self.obj.change_y < 0:
                    block.rect.bottom = self.obj.rect.top
            self.flag = True
            b = block
        return [self.flag, b]

    def green_blocks(self, o_list):
        block_hit_list = pygame.sprite.spritecollide(self.obj, o_list, False)
        for block in block_hit_list:
            if not block.update():
                if self.obj.change_x > 0:
                    block.rect.left = self.obj.rect.right
                elif self.obj.change_x < 0:
                    block.rect.right = self.obj.rect.left
                elif self.obj.change_y > 0:
                    block.rect.top = self.obj.rect.bottom
                elif self.obj.change_y < 0:
                    block.rect.bottom = self.obj.rect.top
            else:
                if self.obj.change_x > 0:
                    self.obj.rect.right = block.rect.left
                elif self.obj.change_x < 0:
                    self.obj.rect.left = block.rect.right
                elif self.obj.change_y > 0:
                    self.obj.rect.bottom = block.rect.top
                elif self.obj.change_y < 0:
                    self.obj.rect.top = block.rect.bottom
