import pygame
import colours


class Player(pygame.sprite.Sprite):

    def __init__(self, ppos, surface, level):
        pygame.sprite.Sprite.__init__(self)
        self.level = level
        self.sprites = pygame.sprite.Group()
        self.surface = surface
        self.state = "idle"
        self.stage = 1
        self.x = ppos[0]
        self.y = ppos[1]
        self.image = pygame.image.load("Graphics/cyborg {}/{}{}.png".format(self.state, self.state, self.stage))
        self.image.set_colorkey(colours.black)
        self.rect = self.image.get_rect(topleft=ppos)
        self.sprites.add(self)

    def animate(self):
        cycle = [1, 2, 3, 4]
        for num in cycle:
            self.stage = num

    def gravity(self, strength):
        self.strength = strength
        self.y += self.strength

    def jump(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.y -= 10

    def collision(self):
        touch = pygame.sprite.spritecollide(self, self.level, False)
        return touch

    def update(self):
        self.jump()
        self.surface.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
