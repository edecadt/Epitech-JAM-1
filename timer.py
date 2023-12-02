#!/bin/python3

import pygame


class Timer:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.text_surface = self.font.render("00:00", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.rectangle_rect = self.text_rect.inflate(20, 20)
        self.rectangle_rect.topleft = (10, 10)
        self.text_rect.center = self.rectangle_rect.center

    def update(self, current_tick, starting_tick):
        minutes = (current_tick - starting_tick) // 60000
        sec = (current_tick - starting_tick) % 60000
        sec //= 1000

        self.text_surface = self.font.render(("%02d:%02d" % (minutes, sec)), True, (255, 255, 255))

    def render(self, game_display):
        pygame.draw.rect(game_display, (0, 0, 0), self.rectangle_rect)
        game_display.blit(self.text_surface, self.text_rect)

