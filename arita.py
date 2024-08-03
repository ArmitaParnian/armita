import pygame
pygame.init()
display=pygame.display.set_mode((800,600))
run = True
while True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
     
     display.fill((0,0,0))
text=myfont.render('armita')
pygame.display.update(