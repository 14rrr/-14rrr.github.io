import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
RED = (200,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
clock = pygame.time.Clock()

font = pygame.font.SysFont('sans', 50)
text = font.render("Random",True, BLACK)
text_box = text.get_rect()

random_pos = (35,50)

circle_color = RED

while running:		
	clock.tick(60)
	screen.fill(WHITE)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen,WHITE,(random_pos[0],random_pos[1],text_box[2],text_box[3]))

	screen.blit(text,random_pos)

	pygame.draw.circle(screen,circle_color,(200,300),50)

	if (mouse_x > random_pos[0]) and (mouse_x < random_pos[0] + text_box[2]) and (mouse_y > random_pos[1]) and (mouse_y < random_pos[1] + text_box[3]):
		text = font.render("Random",True, BLUE)	
		pygame.draw.line(screen,BLUE,(random_pos[0],random_pos[1] + text_box[3]) , (random_pos[0] + text_box[2],random_pos[1] + text_box[3]))
	
	else:
		text = font.render("Random",True, BLACK)

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (mouse_x>35) and (mouse_x<191) and (mouse_y>50) and (mouse_y<108):
					circle_color = (randint(0,255),randint(0,255),randint(0,255))
					print("Right click rectangle")
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()
	
pygame.quit()