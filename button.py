import pygame

pygame.font.init()

font = pygame.font.SysFont("comicsansms", 24)

class Button:
	def __init__(self, x, y, width, height, color = (150,255,150), text = None, text_color = (150,0,255), image = None):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.text = text
		self.text_color = text_color
		self.image = image
		if self.image != None:
			#if we are given an image name, load it:
			self.img = pygame.image.load(image).convert_alpha()
			# find the ratios of the height and width
			w_r = self.width / self.img.get_size()[0]
			h_r = self.height / self.img.get_size()[1]
			#pick the smaller ratio to be our scale
			scale = min(w_r, h_r)
			#find the new image dimensions
			img_w = int(self.img.get_size()[0] * scale)
			img_h = int(self.img.get_size()[1] * scale)
			#resize the image
			self.img = pygame.transform.scale(self.img, (img_w,img_h))


	def draw(self, screen):
		rect = [ self.x, self.y, self.width, self.height]
		#draw the rectangle
		pygame.draw.rect(screen, self.color, rect)
		#only reder text when there is text to rend
		if self.text != None:
			#render the text
			text_render = font.render(self.text, True, self.text_color)
			#center text in the button:
			text_rect = text_render.get_rect(center 
		= (self.x + self.width/2, self.y + self.height/2))
			screen.blit(text_render, text_rect)
		if self.image != None:
			#find center of button
			c_x = self.x + self.width / 2
			c_y = self.y + self.height / 2
			# find the top left corner of the image
			left = c_x - self.img.get_size()[0]/2
			top = c_y - self.img.get_size()[1]/2
			#create the rect for the image
			image_rect = [left, top, self.img.get_size()[0], self.img.get_size()[1]]
			screen.blit(self.img, image_rect)


	def contains(self, loc):
		#detect when mouse is on button
		if self.x <= loc[0] and loc[0] <= self.x + self.width and self.y <= loc[1] and loc[1] <= self.y + self.height:
			return True
		else:
			return False	