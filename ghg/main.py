from pygame import *
mixer.init()
font.init()
#создай окно игры
window = display.set_mode((600, 600))
display.set_caption('ping pong')
BG = transform.scale(image.load('bg.png'), (600,600))

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, filename, speed=0):
        super(). __init__()
        self.image = transform.scale(image.load(filename), (w ,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom < 600:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.right < 600:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        print(self.rect.y, self.rect.x)

class Wall(sprite.Sprite):
    def __init__(self, x, y, w, h,color):
        super().__init__()

        self.image = Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
wall1 = Wall(20,0,20,555, (71, 255, 81))

player = Player(50, 265, 470, 50, 'plat.png', 5)
run = True
finish = False
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(BG, (0,0))
        player.reset()
        player.update()
    
    display.update()
    clock.tick(60)
