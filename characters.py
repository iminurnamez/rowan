import pygame as pg
import main
import images as i

class Hero(pg.sprite.Sprite):
    def __init__(self, map_pos, screen_pos):
        super().__init__()
        self.images = {
            "still": {
                "up": [i.rowanFront],
                "down": [i.rowanFront],
                "left": [i.rowanFront],
                "right": [i.rowanFront]},
            "moving": {
                "up": [i.rowanBack],
                "down": [i.rowanfrontstep1, i.rowanfrontstep2],
                "left": [i.rowanLeft],
                "right": [i.rowanRight]}}
        self.state = "still"
        self.direction = "down"
        self.step = 0
        self.update_image()
        self.rect = self.image.get_rect(center=screen_pos)
        self.map_rect = self.image.get_rect(center=map_pos)
        self.move_keys = {
            pg.K_UP: "up",
            pg.K_DOWN: "down",
            pg.K_LEFT: "left",
            pg.K_RIGHT: "right"}
        self.directions = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0)}            
        self.move_speed = 3
        self.moved = [0, 0]
        
    def update_image(self):
        images = self.images[self.state][self.direction]  
        self.image = images[self.step % len(images)]
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in self.move_keys:
                self.state = "moving"
                self.direction = self.move_keys[event.key]
        elif event.type == pg.KEYUP:
            self.state = "still"

    def update(self):
        self.moved = [0, 0]
        if self.state == "moving":
            self.move()
        self.update_image()        
        
    def move(self):
        x = self.directions[self.direction][0] * self.move_speed
        y = self.directions[self.direction][1] * self.move_speed
        self.map_rect.move_ip(x, y)
        self.moved = [x, y]
        self.step += 1
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class MapObject(pg.sprite.Sprite):
    def __init__(self, name, rect):
        super().__init__()
        self.name = name
        self.rect = rect
        
    def update(self, hero):
        if self.rect.colliderect(hero.map_rect):
            print("hero collided with {}".format(self.name))       
        
class Camera(object):
    def __init__(self, topleft=(0, 0)):
        self.image = i.mappy
        self.rect = self.image.get_rect(topleft=topleft)

    def update(self, hero):
        x = hero.moved[0] * -1
        y = hero.moved[1] * -1
        self.rect.move_ip(x, y)
        
    def draw(self, surface):
       surface.blit(self.image, self.rect)
