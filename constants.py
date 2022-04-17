import pygame, os

# Lambda Functions #
ranlen = lambda x: range(len(x))
load = lambda path, image: pygame.image.load(os.path.join(path, image))
resize = lambda image, size: pygame.transform.scale(image, size)
rotate = lambda image, angle: pygame.transform.rotate(image, angle)

# Pygame Controls and tools#

Clock = pygame.time.Clock()

# Assets #
StartPageIcon = resize(load("assets", "moodboard.png"), (256, 256))
ZombiePageIcon = resize(load("assets", "zombie.png"), (256, 256))
clickhere = resize(load("assets", "click-here.png"), (32, 32))
here = resize(load("assets", "signboard.png"), (512, 512))
StartIcons = [StartPageIcon, rotate(StartPageIcon, 10), rotate(StartPageIcon, 12.5), rotate(StartPageIcon, 15),
              rotate(StartPageIcon, 17.5), rotate(StartPageIcon, 20), rotate(StartPageIcon, 17.5),
              rotate(StartPageIcon, 15), rotate(StartPageIcon, 12.5), rotate(StartPageIcon, 10), StartPageIcon,
              rotate(StartPageIcon, -10), rotate(StartPageIcon, -12.5), rotate(StartPageIcon, -15),
              rotate(StartPageIcon, -17.5), rotate(StartPageIcon, -20), rotate(StartPageIcon, -17.5),
              rotate(StartPageIcon, -15), rotate(StartPageIcon, -12.5), rotate(StartPageIcon, -10), StartPageIcon
              ]
ZombieIcons = [ZombiePageIcon, rotate(ZombiePageIcon, -10), rotate(ZombiePageIcon, -12.5), rotate(ZombiePageIcon, -15),
              rotate(ZombiePageIcon, -17.5), rotate(ZombiePageIcon, -20), rotate(ZombiePageIcon, -17.5),
              rotate(ZombiePageIcon, -15), rotate(ZombiePageIcon, -12.5), rotate(ZombiePageIcon, -10), ZombiePageIcon,
              rotate(ZombiePageIcon, 10), rotate(ZombiePageIcon, 12.5), rotate(ZombiePageIcon, 15),
              rotate(ZombiePageIcon, 17.5), rotate(ZombiePageIcon, 20), rotate(ZombiePageIcon, 17.5),
              rotate(ZombiePageIcon, 15), rotate(ZombiePageIcon, 12.5), rotate(ZombiePageIcon, 10), ZombiePageIcon
              ]

# Constants #
SIZE = (1200, 800)
playingtimes:int = 1