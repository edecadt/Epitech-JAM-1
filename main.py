#!/bin/python3

import pygame

from map import Map
from enemy import Enemy
from player import Player
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mario remix')

        self.game_running = False
        self.game_clock = pygame.time.Clock()
        self.game_display = pygame.display.set_mode((800, 600))
        self.game_display.fill((0, 0, 0))
        self.map = Map()
        self.state = "menu"
        self.menu = Menu()

        # var that will be 0 is no key is being pressed to move on the map
        self.x_to_move_on_map = 0
        self.enemies = []
        self.player = None

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and self.state == "game":
                    self.x_to_move_on_map = -5
                if event.key == pygame.K_q and self.state == "game":
                    self.x_to_move_on_map = 5
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_d and self.x_to_move_on_map == -5) or \
                        (event.key == pygame.K_q and self.x_to_move_on_map == 5) and self.state == "game":
                    self.x_to_move_on_map = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu.start_button_rect.collidepoint(event.pos):
                    self.state = "game"

                if self.menu.right_arrow_rect.collidepoint(event.pos):
                    if self.menu.current_player > 0:
                        self.menu.current_player -= 1
                    else:
                        self.menu.current_player = 5

                if self.menu.left_arrow_rect.collidepoint(event.pos):
                    if self.menu.current_player < 5:
                        self.menu.current_player += 1
                    else:
                        self.menu.current_player = 0

    def update_game(self):
        self.map.update(self.x_to_move_on_map)
        if self.state == "menu":
            self.menu.update()
        elif self.state == "game":
            # self.player.update_player()
            for enemy in self.enemies:
                enemy.update_enemy()

    def render_game(self):
        self.game_display.fill((0, 0, 0))
        self.map.render(self.game_display)
        if self.state == "menu":
            self.menu.render_menu(self.game_display)
        elif self.state == "game":
            # self.player.render_player(self.game_display)
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
