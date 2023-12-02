#!/bin/python3

import pygame

from map import Map
from enemy import Enemy
from player import Player
from color_map import ColorMap


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mario remix')

        self.game_running = False
        self.game_clock = pygame.time.Clock()
        self.game_display = pygame.display.set_mode((800, 600))
        self.game_display.fill((0, 0, 0))
        self.map = Map()
        self.color_map = ColorMap()

        # var that will be 0 is no key is being pressed to move on the map
        self.x_to_move_on_map = 0
        self.enemies = []
        self.player = Player(100, 430, 100, 100, 'assets/player.png', 10)

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
        # collision between player and objects on its right (width -> 100, height -> 100)
        if self.x_to_move_on_map < 0 and self.color_map.image.get_at((-1 * self.color_map.map_x + self.player.x + 100, self.player.y + 99))[1] != 0:
            self.x_to_move_on_map = 0
        # collision between player and objects on its left (width -> 100, height -> 100)
        if self.x_to_move_on_map > 0 and self.color_map.image.get_at((-1 * self.color_map.map_x + self.player.x - 5, self.player.y + 99))[1] != 0:
            self.x_to_move_on_map = 0
        self.map.update(self.x_to_move_on_map)
        self.color_map.update(self.x_to_move_on_map)
        self.player.update_player()
        for enemy in self.enemies:
            enemy.update_enemy()

    def render_game(self):
        self.game_display.fill((0, 0, 0))
        self.map.render(self.game_display)
        self.player.render_player(self.game_display)
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
