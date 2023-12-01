#!/bin/python3

import pygame
from classes.Enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mario remix')

        self.game_running = False
        self.game_clock = pygame.time.Clock()
        self.game_display = pygame.display.set_mode((800, 600))
        self.game_display.fill((0, 0, 0))
        self.enemies = []

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False

    def update_game(self):
        for enemy in self.enemies:
            enemy.update_enemy()

    def render_game(self):
        for enemy in self.enemies:
            enemy.render_enemy(self.game_display)
        pygame.display.update()

    def game_loop(self):
        while self.game_running:
            self.event_handler()
            self.update_game()
            self.render_game()

            self.game_clock.tick(60)

    def launch_game(self):
        self.game_running = True
        self.game_loop()
        pygame.quit()


game = Game()
game.launch_game()
