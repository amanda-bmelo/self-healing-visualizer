import pygame
from self_healing_visualizer.devices_interface.base import BaseUI
import sys


class MainUI():
    """Main class to hangle window and other pygame responsabilites"""
    def __init__(self, height: int, width: int, case_studies: list) -> None:
        pygame.init()
        pygame.key.set_repeat(200, 25)

        self.clock = pygame.time.Clock()
        self.window: pygame.Surface = pygame.display.set_mode((height,width),pygame.RESIZABLE)
        pygame.display.set_caption("Smart grid")
        pygame.display.set_icon(pygame.image.load("logo.png"))

        self.case_studies = case_studies
        self.index = 0

    @property
    def elements(self):
        return [self.case_studies[self.index].smart_grid_UI]

    @property
    def width(self):
        return self.window.get_width()

    @property
    def height(self):
        return self.window.get_height()
    
    def run(self, **kw):
        self.window.fill((225, 225, 225))
        delta = self.clock.tick(120) / 1000
        events = pygame.event.get()
        for e in events:
            if pygame.QUIT == e.type: ## Avoid freezing
                pygame.quit()
                sys.exit(0)
        keys = pygame.key.get_pressed()

        # for e in self.elements:
        #     e.input(keys)
        for e in self.elements:
            e.draw(self.window, self.width/2, self.height/2)
        pygame.display.update()