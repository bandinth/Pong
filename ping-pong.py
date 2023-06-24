from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image=tranform.scale(image.load(player_image),(width,height))
        self.rect=self.image.get_rect()
        self.x=player_x
        self.y=player_y
        self.speed=player_speed
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        key=key.get_pressed()
        if key[K_UP] and self.rect.y<0:
            self.rect.y-=self.speed
        if key[K_DOWN] and self.rect.y>widht-80:
            self.rect.y+=self.speed
    def update_l(self):
        key=key.get_pressed()
        if key[K_w] and self.rect.y<0:
            self.rect.y-=self.speed
        if key[K_s] and self.rect.y>widht-80:
            self.rect.y+=self.speed
    
            
    
        

width=600
height=600

mw=display.set_mode((width,height))
mw.fill((100,100,255))
display.set_caption("Пінг Понг")

clock=time.Clock()

game=True
finish=False
FPS=60

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False


    display.update()
    clock.tick(FPS)
