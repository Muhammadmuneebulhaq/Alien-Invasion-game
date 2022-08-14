# to generate aliens randomly
'''for row_number in range(0,number_of_rows):
            for alien_number in range(0,number_of_aliens):
                alien = alien(self)
                alien.x = alien.x + random.randint(0, available_space_x)
                alien.y = alien.y + random.randint(0, available_space_y)
                alien.rect.x = alien.x
                alien.rect.y = alien.y
                self.aliens.add(alien)'''
        
#the following code snippet is for switching between fullscreen and dimensions in settings
'''elif event.key == pygame.K_f:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height                        
        self.settings.screen_width = self.screen.get_rect().width
        self.rocket = Rocket(self) 
    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: 
        self.settings.screen_height = 800
        self.settings.screen_width = 1200
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.rocket = Rocket(self)'''
        
import pygame
pygame.init()
while True:
    pygame.display.set_mode((200, 200))