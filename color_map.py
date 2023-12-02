#!/bin/python3

import pygame


class ColorMap:
    def __init__(self):
        self.map_x = 0
        self.zoom_scale = 0
        self.image = pygame.image.load('assets/color_map.png')
        self.image_rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(self.image_rect.width * 2.5),
                                                         int(self.image_rect.height * 2.5)))

    def update(self, x_to_move):
        if x_to_move == 0:
            return
        self.map_x += x_to_move
