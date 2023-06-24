from pygame import*
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