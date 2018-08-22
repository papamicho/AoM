#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Artifacts class

 by: gNrg
"""
import pygame
from collisionManager import CollisionManager
 
class Artifact(pygame.sprite.Sprite):
 
    def __init__(self, file, level, flag = False):
        """ Artifact represent a constant block on the map """
        super().__init__()
        self.flag = flag
        self.level = level
        self.collisionManager = CollisionManager(self)
        # Grab the image for this platform
        self.image = pygame.image.load(file).convert_alpha() 
        self.rect = self.image.get_rect()

    def update(self):
        coll = False
        if self.flag:
            if not coll: coll = self.collisionManager.block_vs_object(self.level.walls_list)
            if not coll: coll = self.collisionManager.block_vs_object(self.level.door_list)
            if not coll: coll = self.collisionManager.block_vs_object(self.level.artifact_list)
            if not coll: coll = self.collisionManager.block_vs_object(self.level.water_list)
            #coll = self.collisionManager.block_vs_object(self.level.block_list)
            if not coll: coll = self.collisionManager.block_vs_object(self.level.chest_list)
        return coll