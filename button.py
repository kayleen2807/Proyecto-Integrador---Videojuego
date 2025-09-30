import pygame
class Button():
	def __init__(self, image, image_hover, pos, text_input, font, base_color, hovering_color):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input

        # Si no hay imagen, usa el texto como imagen
		if image is None:
			self.text = self.font.render(self.text_input, True, self.base_color)
			self.image = self.text
		else:
			self.image = image
			self.text = self.font.render(self.text_input, True, self.base_color)

        # Si no hay imagen_hover, usa la misma
		self.image_hover = image_hover if image_hover else self.image

        # Ahora sí, ya tenemos una Surface válida
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			screen.blit(self.image_hover, self.rect)
		else:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

		
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)