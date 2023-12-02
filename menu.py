import json

import pygame

players = json.load(open("assets/players.json"))


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.players = players
        self.current_player = 0
        self.start_button = pygame.image.load("assets/start_button.png")
        self.left_arrow = pygame.image.load("assets/arrow_button.png")
        self.right_arrow = pygame.image.load("assets/arrow_button.png")

        for player in self.players:
            player["sprite"] = pygame.image.load(player["texture"])
            player["sprite"] = pygame.transform.scale(player["sprite"], (920 / 2, 623 / 2))

        self.start_button = pygame.transform.scale(self.start_button, (466 / 2, 151 / 2))
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.topleft = (400 - 466 / 4, 400)

        self.left_arrow = pygame.transform.scale(self.left_arrow, (542 / 6, 461 / 6))
        self.left_arrow_rect = self.left_arrow.get_rect()
        self.left_arrow = pygame.transform.rotate(self.left_arrow, 180)
        self.left_arrow_rect.topleft = (640 - 542 / 4, 250)

        self.right_arrow = pygame.transform.scale(self.right_arrow, (542 / 6, 461 / 6))
        self.right_arrow_rect = self.right_arrow.get_rect()
        self.right_arrow_rect.topleft = (200, 250)

    def update_menu(self):
        pass

    def render_menu(self, screen):
        screen.blit(self.start_button, (400 - 466 / 4, 400))
        screen.blit(self.left_arrow, (200, 250))
        screen.blit(self.right_arrow, (640 - 542 / 4, 250))
        screen.blit(self.players[self.current_player]["sprite"], (175, 100))
