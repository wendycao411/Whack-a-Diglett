#-load and resize diglett and mallet
#-mouse to mallet
#-move diglett randomly
#-timer
#detect hits
#score

import pygame
import sys
import random
import time
from button import Button
import math

pygame.init()

#functions
def move_diglett():
	diglett.x = random.randint(0, scr_w - diglett_size)
	diglett.y = random.randint(0, scr_h - diglett_size)

#variables
screen = pygame.display.set_mode()
scr_w = screen.get_size()[0] - 2
scr_h = screen.get_size()[1] - 27
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 17)
background_color = (135, 79, 23)

mallet_size = 30
mallet_image = pygame.image.load("mallet.png").convert_alpha()
mallet_image = pygame.transform.scale(mallet_image, (mallet_size, mallet_size))

fps = 60
diglett_move_frame = fps * 2
frame_counter = 0
game_length = 10
text_width = 80
text_height = 20
timer_display = Button(0,0, text_width, text_height, text = "Time: " + str(game_length), color = background_color, text_color=(255,255,255))
score = 0
score_display = Button(scr_w - text_width, 0, text_width, text_height, text = "Score: " + str(score), color = background_color, text_color=(255,255,255))

#hide mouse
pygame.mouse.set_visible(False)

#pick diglett size
diglett_size = int(min(scr_w, scr_h) / 5)
#make diglett button
diglett = Button(0,0, diglett_size, diglett_size, image = "diglett.png", color = background_color)

start_time = time.time()

while True:
	frame_counter += 1
	mouse = pygame.mouse.get_pos()

	elapsed_time = time.time() - start_time
	if elapsed_time >= game_length:
		print(score)
		pygame.quit()
		sys.exit()

	timer_display.text = "Time: " + str(math.ceil(game_length - elapsed_time))

	#checking events
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			#check which button is pressed (returns a tuple with left, middle, and right)
			if pygame.mouse.get_pressed()[0] and diglett.contains(mouse):
				score+=1
				score_display.text = "Score: " + str(score)
				move_diglett()
				frame_counter = 0

	if frame_counter % diglett_move_frame == 0:
		move_diglett()
				
	#draw stuff	
	screen.fill(background_color)
	timer_display.draw(screen)
	diglett.draw(screen)
	score_display.draw(screen)

	mallet_rect = [mouse[0] - mallet_size / 4, mouse[1] - 3/4 * mallet_size, mallet_size, mallet_size]
	screen.blit(mallet_image, mallet_rect)

			
	#show the render
	pygame.display.update()
	clock.tick(fps)