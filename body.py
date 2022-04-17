import pygame, sys, os
from Sonama.constants import *
from random import randint as ints
from pygame.sprite import Sprite
import asyncio


class DrawCircles:
    def __init__(self, screen, position):
        self.screen = screen
        self.colour = (0, 0, 0)
        self.position = Coordinates(position[0], position[1])
        self.radius = 15
        self.extra = 1
        pygame.draw.circle(self.screen, self.colour, self.position.coordinates, self.radius, self.extra)


class Multi(Sprite):
    def __init__(self):
        super(Sprite, self).__init__()

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()


class DrawLines:
    def __init__(self, screen, start_pos: list, end_pos: list):
        self.screen = screen
        self.colour = (0, 0, 0)
        self.start_pos = Coordinates(start_pos[0], 500 - start_pos[1])
        self.end_pos = Coordinates(end_pos[0], end_pos[1])
        self.radius = 15
        self.extra = 1
        pygame.draw.line(self.screen, self.colour, self.start_pos.coordinates, self.end_pos.coordinates)


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def update(self):
        self.coordinates = (self.x, self.y)

    def __repr__(self):
        return (f'{self.__class__.__name__}')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode(SIZE)
        self.canvas = pygame.Surface((550, 500))
        self.canvas.fill((255, 255, 255))
        self.gameover = False
        self.account = 100
        self.invested = 0
        self.animnum = 0
        self.screen = 1
        self.clock = Clock
        self.total = self.account + self.invested
        self.playingtimes = playingtimes
        self.font = pygame.font.Font('freesansbold.ttf', 57)
        self.mid = pygame.font.Font('freesansbold.ttf', 35)
        self.smal = pygame.font.Font('freesansbold.ttf', 23)
        self.title = self.font.render("Stocks!!!", True, (0, 0, 0))
        self.rec = self.smal.render("By: Aryan Dhawan", True, (0, 0, 0))
        self.personal = self.font.render(f"Amount: {self.account}", True, (0, 0, 0))
        self.personal1 = self.font.render(f"Invested: {self.invested}", True, (0, 0, 0))
        self.investthing = self.mid.render("Invest now?[R]", True, (0, 0, 0))
        self.sellthing = self.mid.render("Sell now?[C]", True, (0, 0, 0))
        self.skipthing = self.mid.render("Skip now?[S]", True, (0, 0, 0))
        self.mark100 = self.smal.render("100", True, (0, 0, 0))
        self.mark50 = self.smal.render("50", True, (0, 0, 0))
        self.day1 = self.smal.render("1", True, (0, 0, 0))
        self.day2 = self.smal.render("2", True, (0, 0, 0))
        self.day3 = self.smal.render("3", True, (0, 0, 0))
        self.day4 = self.smal.render("4", True, (0, 0, 0))
        self.day5 = self.smal.render("5", True, (0, 0, 0))
        self.personal2 = self.font.render(f"Net: {self.total}", True, (0, 0, 0))
        self.currentday = 0
        self.days: list = [i + 1 for i in range(5)]
        self.amounts: list = [ints(0, 100) + ints(0, 100) + ints(0, 70) for i in range(5)]
        self.differences = [self.amounts[i] - self.amounts[i - 1] for i in range(1, 5)]
        self.bank = pygame.sprite.Group()
        self.rect1 = pygame.Rect((300, 468), (301, 469))
        self.rect2 = pygame.Rect((300, 518), (300, 518))
        self.rect3 = pygame.Rect((300, 568), (301, 569))
        self.times = 0

    def draw(self, image1, location):
        self.win.blit(image1, location)

    def canvasDraw(self, image, location):
        self.canvas.blit(image, location)

    def codebase(self):

        if self.screen == 1:
            self.win.fill(pygame.Color('white'))
        else:
            self.win.fill(pygame.Color('gray'))
        self.clock.tick(10)

        if self.animnum < len(StartIcons) - 1:
            self.animnum += 1
        else:
            self.animnum = 0

        if self.screen == 1:
            self.draw(self.title, (556, 242))
            self.draw(self.rec, (556, 400))
            self.draw(StartIcons[self.animnum], (156, 242))
            self.draw(ZombieIcons[self.animnum], (78, 436))
        elif self.screen == 2:
            self.draw(self.personal, (64, 368))
            self.draw(self.personal1, (64, 268))
            self.draw(self.personal2, (64, 168))
            self.draw(self.investthing, (64, 468))
            self.draw(self.sellthing, (64, 518))
            self.draw(self.skipthing, (64, 568))
            self.draw(self.canvas, (600, 100))
            self.draw(self.day1, (700, 600))
            self.draw(self.day2, (800, 600))
            self.draw(self.day3, (900, 600))
            self.draw(self.day4, (1000, 600))
            self.draw(self.day5, (1100, 600))
            for i in range(5):
                if self.currentday < 7 and i <= self.currentday:
                    DrawCircles(self.canvas, [100 * (i + 1), 500 - self.amounts[i]])
                    if i == 0:
                        DrawLines(self.canvas, [0, 0], [100, 500 - self.amounts[i]])
                    else:
                        DrawLines(self.canvas, [100 * i, self.amounts[i - 1]],
                                  [100 * (i + 1), 500 - self.amounts[i]])
        elif self.screen == 3:
            self.draw(self.personal2, (496, 64))
            self.draw(here, (256, 256))

        pygame.display.update()

    async def mus(self):
        pygame.mixer.music.play(loops=1)

    def run(self):

        while not self.gameover:

            for events in pygame.event.get():
                if events.type == pygame.QUIT:  # Change Later
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if self.screen == 1:
                        self.screen = 2
                if events.type == pygame.KEYDOWN:
                    if self.screen == 2:
                        if events.key == pygame.K_r:
                            if self.account > 0 and self.account - (self.amounts[self.currentday] // 4) >= 0:
                                self.times += 1
                                self.invested += (self.amounts[self.currentday] // 4)

                                self.account -= self.amounts[self.currentday] // 4
                                self.personal = self.font.render(f"Amount: {self.account}", True, (0, 0, 0))
                                self.personal1 = self.font.render(f"Invested: {self.invested}", True, (0, 0, 0))
                                self.total = self.account + self.invested

                                self.personal2 = self.font.render(f"Net: {self.total}", True, (0, 0, 0))

                        if events.key == pygame.K_c:
                            if self.account >= 0 and self.invested - (self.amounts[self.currentday] // 4) >= 0:
                                self.invested -= (self.amounts[self.currentday] // 4)
                                self.account += self.amounts[self.currentday] // 4
                                if self.times != 1: self.times -= 1

                                self.personal = self.font.render(f"Amount: {self.account}", True, (0, 0, 0))
                                self.personal1 = self.font.render(f"Invested: {self.invested}", True, (0, 0, 0))
                                self.total = self.account + self.invested
                                self.personal2 = self.font.render(f"Net: {self.total}", True, (0, 0, 0))

                        if events.key == pygame.K_s:

                            if self.currentday < 4:

                                self.invested = int((((self.amounts[self.currentday + 1]) * self.times) / 5))

                                self.personal1 = self.font.render(f"Invested: {self.invested}", True, (0, 0, 0))
                                self.total = self.account + self.invested
                                self.personal2 = self.font.render(f"Net: {self.total}", True, (0, 0, 0))
                                self.currentday += 1
                            else:
                                self.screen = 3
                    if self.screen == 3:
                        if events.key == pygame.K_d:
                            self.playingtimes += 1
                            playingtimes = self.playingtimes
            self.codebase()
