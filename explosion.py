import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, screen, file_name, pos, size, count, time):
        super().__init__()
        self.screen = screen
        self.master_image = pygame.image.load(file_name).convert_alpha()
        self.time = time
        self.timer = 0
        self.columns = size[0]
        self.lines = size[1]
        self.frame_count = count if count <= self.columns * self.lines else self.columns * self.lines

        img_rect = self.master_image.get_rect()
        self.width = img_rect.width // self.columns
        self.height = img_rect.height // self.lines
        self._rect = (0, 0, self.width, self.height)
        self.rect = (pos[0], pos[1], self.width, self.height)
        self.image = self.master_image.subsurface(self._rect)


        self.topleft = (0, 0)
        self.frame = 0
        self.old_frame = -1
        self.first_frame = 0
        self.last_frame = 0

        self.last_frame = (img_rect.width // self.width) * (img_rect.height // self.height) - 1


    def update(self):
        self.timer += 1
        if self.timer < self.time:
            return
        self.timer = 0

        self.frame += 1
        if self.frame >= self.frame_count:
            self.frame = 0

        frame_x = (self.frame % self.columns) * self.width
        frame_y = (self.frame // self.columns) * self.height
        rect = (frame_x, frame_y, self.width, self.height)
        self.image = self.master_image.subsurface(rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
