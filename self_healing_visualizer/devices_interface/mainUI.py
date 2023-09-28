import pygame
from self_healing_visualizer.devices_interface.base import BaseUI
import sys


class MainUI():
    def __init__(self, height: int, width: int, elements: list[BaseUI]) -> None:
        pygame.init()
        pygame.key.set_repeat(200, 25)
        self.height = height
        self.width = width

        self.clock = pygame.time.Clock()
        self.window: pygame.Surface = pygame.display.set_mode((height,width),pygame.RESIZABLE)

        self.elements = elements

    def run(self, **kw):
        self.window.fill((225, 225, 225))
        delta = self.clock.tick(120) / 1000
        events = pygame.event.get()
        for e in events:
            if pygame.QUIT == e.type: ## Avoid freezing
                pygame.quit()
                sys.exit(0)
        keys = pygame.key.get_pressed()

        for e in self.elements:
            e.draw(self.window, self.width/2, self.height/2)
        pygame.display.update()