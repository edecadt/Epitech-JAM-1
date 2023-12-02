#!/bin/python3

import pygame

from map import Map
from enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mario remix')

        self.game_running = False
        self.game_clock = pygame.time.Clock()
        self.game_display = pygame.display.set_mode((800, 600))
        self.game_display.fill((0, 0, 0))
        self.map = Map()

        # var that will be 0 is no key is being pressed to move on the map
        self.x_to_move_on_map = 0
        self.enemies = []

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.x_to_move_on_map = -5
                if event.key == pygame.K_q:
                    self.x_to_move_on_map = 5
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_d and self.x_to_move_on_map == -5) or \
                        (event.key == pygame.K_q and self.x_to_move_on_map == 5):
                    self.x_to_move_on_map = 0

    def update_game(self):
        self.map.update(self.x_to_move_on_map)
        for enemy in self.enemies:
            enemy.update_enemy()

    def render_game(self):
        self.game_display.fill((0, 0, 0))
        self.map.render(self.game_display)
        for enemy in self.enemies:
            enemy.render_enemy(self.game_display)
        pygame.display.flip()

    def game_loop(self):
        while self.game_running:
            self.event_handler()
            self.update_game()
            self.render_game()

            # this line is to ensure the game runs at 60 fps
            self.game_clock.tick(60)

    def launch_game(self):
        self.game_running = True
        self.game_loop()
        pygame.quit()


game = Game()
game.launch_game()
