#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Heart class

 by: gNrg
"""
import pygame
 
class Heart(pygame.sprite.Sprite):
 
    def __init__(self, bonus):
        super().__init__()
        self.image = pygame.image.load("Assets/Heart.png").convert_alpha() 
        self.rect = self.image.get_rect()
        self.bonus = bonus