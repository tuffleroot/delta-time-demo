import sys,time
import pygame as pg
pg.init()

win=pg.display.set_mode((800,400))
fps_clock=pg.time.Clock()
rect=pg.rect.Rect(100,175,50,50)

font=pg.font.Font("arial.ttf",20)
time_label=font.render("Time Elapsed: 0",True,(255,255,255))
time_label_rect=time_label.get_rect(center=(400,50))
FPS=90
SPEED=250
start_moving=False

last_time=time.time()
while True:
    new_time=time.time()
    dt=new_time-last_time
    last_time=new_time
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
            start_moving=True
            start_time=time.time()
        
    if start_moving:
        rect.x+=int(SPEED*dt)
    
    if rect.right>=700 and start_moving:
        start_moving=False
        time_label=font.render(f"Time Elapsed: {time.time()-start_time:.2f} sec",True,(255,255,255))
        time_label_rect=time_label.get_rect(center=(400,50))
    

    win.fill((18,18,18))
    pg.draw.line(win,(255,255,255),(100,50),(100,350),3)
    pg.draw.line(win,(255,255,255),(700,50),(700,350),3)
    win.blit(time_label,time_label_rect)
    pg.draw.rect(win,(255,0,0),rect)
    pg.display.update()
    fps_clock.tick(FPS)