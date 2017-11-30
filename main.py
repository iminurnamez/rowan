import pygame as pg
import characters as char
import images as i

#setting window size
display_width = 900
display_height = 600

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


class Gamerun(object):
    def __init__(self, width, height):
        self.done = False
        self.screen = pg.display.set_mode((width, height))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.hero = char.Hero(self.screen_rect.center, self.screen_rect.center)
        #sprite to represent the base of the tree
        self.tree = char.MapObject("Tree", pg.Rect(772, 173, 25, 11))
        self.camera = char.Camera()
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.done = True
            self.hero.get_event(event)
            
    def update(self):
        self.hero.update()
        self.tree.update(self.hero)
        self.camera.update(self.hero)
        
    def draw(self):
        self.screen.fill(pg.Color("black"))
        self.camera.draw(self.screen)
        self.hero.draw(self.screen)
        
    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(30)
        pg.quit()
        
if __name__ == '__main__':
    Gamerun(display_width, display_height).main()

