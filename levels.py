#!/usr/bin/env python
"""
 Adventures of Manuel with PyGame

 Level classes

 by: gNrg
"""
import pygame
 
import constants
import artifact
import heart
import chest
import door
import wall
import snake
import water
import bridge

from spritesheet_functions import SpriteSheet

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player.  """
        self.player = player

        self.hearts_needed = 0
 
        # Lists of sprites used in all levels
        self.sprites = []

        self.artifact_list = pygame.sprite.Group()
        self.water_list = pygame.sprite.Group()
        self.bridge_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.hearts_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.chest_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.walls_list = pygame.sprite.Group()
        self.shot_list = pygame.sprite.Group()
 
        # Background image
        self.background = pygame.image.load("Assets/background.png").convert()
        self.background.set_colorkey(constants.WHITE)

        # Side menu images
        sprite_sheet = SpriteSheet("Assets/manolito.png")
        self.lives_image = sprite_sheet.get_image(116, 0, 58, 58)
        sprite_sheet = SpriteSheet("Assets/Bullet.png")
        self.shots_image = sprite_sheet.get_image(58, 0, 58, 58)

        # Side menu numbers
        sprite_sheets = [SpriteSheet("Assets/00.png"), SpriteSheet("Assets/01.png"), 
                         SpriteSheet("Assets/02.png"), SpriteSheet("Assets/03.png"), 
                         SpriteSheet("Assets/04.png"), SpriteSheet("Assets/05.png")]
        self.numbers = {
            0: sprite_sheets[0].get_image(0, 0, 58, 58),
            1: sprite_sheets[1].get_image(0, 0, 58, 58),
            2: sprite_sheets[2].get_image(0, 0, 58, 58),
            3: sprite_sheets[3].get_image(0, 0, 58, 58),
            4: sprite_sheets[4].get_image(0, 0, 58, 58),
            5: sprite_sheets[5].get_image(0, 0, 58, 58)
        }
    
    def set_player_position(self, x, y):
        self.player.rect.x = x
        self.player.rect.y = y

    # Update everythign on this level
    def update(self, screen):
        # Update everything in this level.
        self.shot_list.update()
        self.walls_list.update()
        self.artifact_list.update()
        self.water_list.update()
        self.bridge_list.update()
        self.block_list.update()
        for b in self.block_list:
            b.update()
        self.hearts_list.update()
        self.enemy_list.update()
        for c in self.chest_list:
            if c.hearts_needed <= self.player.hearts_collected:
                if self.player.gem == False:
                    c.open_chest()
                else: 
                    c.empty()
                    for d in self.door_list: d.open_door()
        self.chest_list.update()
        self.door_list.update()
        screen.blit(self.numbers.get(self.player.lives), [783, 116])
        screen.blit(self.numbers.get(self.player.shots), [783, 232])

 
    def draw(self, screen):
        # Draw everything on side menu.
        screen.blit(self.background, [0, 0])
        screen.blit(self.lives_image, [783, 58])
        screen.blit(self.numbers.get(self.player.lives), [783, 116])
        screen.blit(self.shots_image, [783, 174])
        screen.blit(self.numbers.get(self.player.shots), [783, 232])

        # Draw all the sprite lists
        self.shot_list.draw(screen)
        self.walls_list.draw(screen)
        self.artifact_list.draw(screen)
        self.water_list.draw(screen)
        self.bridge_list.draw(screen)
        self.block_list.draw(screen)
        self.hearts_list.draw(screen)
        self.enemy_list.draw(screen)
        for c in self.chest_list:
            if c.hearts_needed <= self.player.hearts_collected:
                if self.player.gem == False:
                    c.open_chest()
                else: 
                    c.empty()
                    for d in self.door_list: d.open_door()
        self.chest_list.draw(screen)
        self.door_list.draw(screen)

    def completed(self, screen):
        screen.fill(constants.BLACK)
        self.shot_list.empty()
        self.walls_list.empty()
        self.artifact_list.empty()
        self.block_list.empty()
        self.water_list.empty()
        self.bridge_list.empty()
        self.hearts_list.empty()
        self.enemy_list.empty()
        self.chest_list.empty()
        self.door_list.empty()
        self.player.end_level()

    def broke_egg(self):
        max_time = 0
        enemy_to_broke = None
        for enemy in self.enemy_list:
            if enemy.get_status() == constants.ENEMY_EGG:
                if enemy.change_status_time > max_time:
                    max_time = enemy.change_status_time
                    enemy_to_broke = enemy
        if enemy_to_broke != None:
            enemy_to_broke.broke_egg()

    def remove_egg(self):
        max_time = 0
        egg_to_remove = None
        for enemy in self.enemy_list:
            if enemy.get_status() == constants.ENEMY_BREAKING_EGG:
                if enemy.change_status_time > max_time:
                    max_time = enemy.change_status_time
                    egg_to_remove = enemy
        if egg_to_remove != None:
            egg_to_remove.remove_egg()
            if self.player.hearts_collected == self.hearts_needed:
                egg_to_remove.status = 4

class Loading(Level):
    """ Loading screen. """
    def __init__(self):
        # Background image
        self.background = pygame.image.load("Assets/Screens/Loading.png").convert()
        self.background.set_colorkey(constants.WHITE)
    def draw(self, screen):
        # Draw everything on side menu.
        screen.blit(self.background, [0, 0])


class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """

        # Player start position
        self.posx = 58
        self.posy = 232

        # Call the parent constructor
        Level.__init__(self, player)
 
        # Door
        block = door.Door()
        block.rect.x = 348
        block.rect.y = 0
        block.player = self.player
        self.door_list.add(block)

        # Walls
        self.walls = [ [wall.Wall(0), 58, 0],
                       [wall.Wall(1), 116, 0],
                       [wall.Wall(1), 174, 0],
                       [wall.Wall(1), 232, 0],
                       [wall.Wall(1), 290, 0],
                       [wall.Wall(1), 522, 0],
                       [wall.Wall(1), 580, 0],
                       [wall.Wall(1), 638, 0]]
        for w in self.walls:
            block = w[0]
            block.rect.x = w[1]
            block.rect.y = w[2]
            block.player = self.player
            self.walls_list.add(block)

        # Chest
        self.hearts_needed = 2
        block = chest.Chest(2)
        block.rect.x = 290
        block.rect.y = 580
        block.player = self.player
        self.chest_list.add(block)

        # Hearts
        self.hearts = [ [heart.Heart(0), 290, 116],
                   [heart.Heart(2), 638, 290]
                   ]
        for h in self.hearts:
            block = h[0]
            block.rect.x = h[1]
            block.rect.y = h[2]
            block.player = self.player
            self.hearts_list.add(block)

        # Snake
        block = snake.Snake(self.player, self)
        block.rect.x = 406
        block.rect.y = 348
        self.enemy_list.add(block)
 
        # Array with type of artifacts, and x, y location of them.
        level = [ [artifact.Artifact("Assets/Rock.png", self), 58, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 58, 116],
                  [artifact.Artifact("Assets/Rock.png", self), 116, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 174, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 232, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 290, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 232, 116],
                  [artifact.Artifact("Assets/Rock.png", self), 232, 174],
                  [artifact.Artifact("Assets/Rock.png", self), 290, 174],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 174],
                  [artifact.Artifact("Assets/Rock.png", self), 290, 232],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 232],
                  [artifact.Artifact("Assets/Rock.png", self), 290, 290],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 290],
                  [artifact.Artifact("Assets/Rock.png", self), 464, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 464, 116],
                  [artifact.Artifact("Assets/Rock.png", self), 464, 174],
                  [artifact.Artifact("Assets/Rock.png", self), 464, 232],
                  [artifact.Artifact("Assets/Rock.png", self), 464, 290],
                  [artifact.Artifact("Assets/Rock.png", self), 522, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 522, 116],
                  [artifact.Artifact("Assets/Rock.png", self), 522, 174],
                  [artifact.Artifact("Assets/Rock.png", self), 522, 232],
                  [artifact.Artifact("Assets/Rock.png", self), 522, 290],
                  [artifact.Artifact("Assets/Rock.png", self), 522, 348],
                  [artifact.Artifact("Assets/Rock.png", self), 580, 174],
                  [artifact.Artifact("Assets/Rock.png", self), 580, 232],
                  [artifact.Artifact("Assets/Rock.png", self), 58, 580],
                  [artifact.Artifact("Assets/Rock.png", self), 232, 580],
                  [artifact.Artifact("Assets/Rock.png", self), 58, 638],
                  [artifact.Artifact("Assets/Rock.png", self), 116, 638],
                  [artifact.Artifact("Assets/Rock.png", self), 174, 638,],
                  [artifact.Artifact("Assets/Rock.png", self), 232, 638],
                  [artifact.Artifact("Assets/Rock.png", self), 290, 638],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 638],

                  [artifact.Artifact("Assets/Tree.png", self), 58, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 58, 522],
                  [artifact.Artifact("Assets/Tree.png", self), 116, 116],
                  [artifact.Artifact("Assets/Tree.png", self), 116, 174],
                  [artifact.Artifact("Assets/Tree.png", self), 116, 406],
                  [artifact.Artifact("Assets/Tree.png", self), 116, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 116, 522],
                  [artifact.Artifact("Assets/Tree.png", self), 116, 580],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 116],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 174],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 232],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 406],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 522],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 580],
                  [artifact.Artifact("Assets/Tree.png", self), 232, 232],
                  [artifact.Artifact("Assets/Tree.png", self), 232, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 232, 522],
                  [artifact.Artifact("Assets/Tree.png", self), 464, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 464, 522],
                  [artifact.Artifact("Assets/Tree.png", self), 522, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 522, 522],
                  [artifact.Artifact("Assets/Tree.png", self), 522, 580],
                  [artifact.Artifact("Assets/Tree.png", self), 580, 58],
                  [artifact.Artifact("Assets/Tree.png", self), 580, 116],
                  [artifact.Artifact("Assets/Tree.png", self), 580, 290],
                  [artifact.Artifact("Assets/Tree.png", self), 580, 522],
                  [artifact.Artifact("Assets/Tree.png", self), 580, 580],
                  [artifact.Artifact("Assets/Tree.png", self), 638, 58],
                  [artifact.Artifact("Assets/Tree.png", self), 638, 116],
                  [artifact.Artifact("Assets/Tree.png", self), 638, 174],
                  [artifact.Artifact("Assets/Tree.png", self), 638, 232]

                  ]
        for a in level:
            block = a[0]
            block.rect.x = a[1]
            block.rect.y = a[2]
            block.player = self.player
            self.artifact_list.add(block)

class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 2. """

        # Player start position
        self.posx = 290
        self.posy = 580

        # Call the parent constructor
        Level.__init__(self, player)
 
        # Door
        block = door.Door()
        block.rect.x = 522
        block.rect.y = 0
        block.player = self.player
        self.door_list.add(block)

        # Walls
        self.walls = [ [wall.Wall(0), 58, 0],
                       [wall.Wall(1), 116, 0],
                       [wall.Wall(1), 174, 0],
                       [wall.Wall(1), 232, 0],
                       [wall.Wall(1), 290, 0],
                       [wall.Wall(1), 348, 0],
                       [wall.Wall(1), 406, 0],
                       [wall.Wall(1), 464, 0]]
        for w in self.walls:
            block = w[0]
            block.rect.x = w[1]
            block.rect.y = w[2]
            block.player = self.player
            self.walls_list.add(block)

        # Chest
        self.hearts_needed = 4
        block = chest.Chest(4)
        block.rect.x = 58
        block.rect.y = 348
        block.player = self.player
        self.chest_list.add(block)

        # Hearts
        self.hearts = [ [heart.Heart(2), 116, 116],
                   [heart.Heart(0), 580, 116],
                   [heart.Heart(0), 58, 638],
                   [heart.Heart(0), 464, 522]
                   ]
        for h in self.hearts:
            block = h[0]
            block.rect.x = h[1]
            block.rect.y = h[2]
            block.player = self.player
            self.hearts_list.add(block)

        # Dragon
        #block = snake.Snake()
        #block.rect.x = 406
        #block.rect.y = 348
        #block.player = self.player
        #self.enemy_list.add(block)
 
        # Array with type of artifacts, and x, y location of them.
        level = [ [artifact.Artifact("Assets/Rock.png", self), 348, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 406, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 464, 58],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 116],
                  [artifact.Artifact("Assets/Rock.png", self), 406, 116],
                  [artifact.Artifact("Assets/Rock.png", self), 464, 116],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 464],
                  [artifact.Artifact("Assets/Rock.png", self), 348, 522],
                  [artifact.Artifact("Assets/Rock.png", self), 406, 464],
                  [artifact.Artifact("Assets/Rock.png", self), 406, 522],

                  [artifact.Artifact("Assets/Tree.png", self), 174, 348],
                  [artifact.Artifact("Assets/Tree.png", self), 174, 406],
                  [artifact.Artifact("Assets/Tree.png", self), 232, 348],
                  [artifact.Artifact("Assets/Tree.png", self), 232, 406],
                  [artifact.Artifact("Assets/Tree.png", self), 464, 406],
                  [artifact.Artifact("Assets/Tree.png", self), 522, 406],
                  [artifact.Artifact("Assets/Tree.png", self), 464, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 522, 464],
                  [artifact.Artifact("Assets/Tree.png", self), 406, 174],
                  [artifact.Artifact("Assets/Tree.png", self), 464, 174]

                  ]
        for a in level:
            block = a[0]
            block.rect.x = a[1]
            block.rect.y = a[2]
            block.player = self.player
            self.artifact_list.add(block)

        # Green blocks
        block = artifact.Artifact("Assets/Block.png", self, True)
        block.rect.x = 232 #406
        block.rect.y = 580
        block.player = self.player
        self.block_list.add(block)

        waters = [[water.Water(), 58, 232],
                  [water.Water(), 116, 232],
                  [water.Water(), 174, 232],
                  [water.Water(), 232, 232],
                  [water.Water(), 58, 290],
                  [water.Water(), 116, 290],
                  [water.Water(), 174, 290],
                  [water.Water(), 232, 290],
                  [water.Water(), 348, 232],
                  [water.Water(), 406, 232],
                  [water.Water(), 464, 232],
                  [water.Water(), 522, 232],
                  [water.Water(), 348, 290],
                  [water.Water(), 406, 290],
                  [water.Water(), 464, 290],
                  [water.Water(), 522, 290],
                  [water.Water(), 638, 232],
                  [water.Water(), 638, 290],
                  [water.Water(), 638, 348],
                  [water.Water(), 638, 406],
                  [water.Water(), 638, 464],
                  [water.Water(), 638, 522],
                  [water.Water(), 638, 580],
                  [water.Water(), 638, 638],
                  [water.Water(), 580, 638],
                  [water.Water(), 522, 638],
                  [water.Water(), 464, 638],
                  [water.Water(), 406, 638]]

        for w in waters:
            block = w[0]
            block.rect.x = w[1]
            block.rect.y = w[2]
            block.player = self.player
            self.water_list.add(block)


        bridges = [[bridge.Bridge("VERTICAL"), 290, 232],
                  [bridge.Bridge("VERTICAL"), 290, 290],
                  [bridge.Bridge("VERTICAL"), 580, 232],
                  [bridge.Bridge("VERTICAL"), 580, 290]]

        for b in bridges:
            block = b[0]
            block.rect.x = b[1]
            block.rect.y = b[2]
            block.player = self.player
            self.bridge_list.add(block)