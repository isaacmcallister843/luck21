import pygame
import sys
from gameManager import GameManager
from dealer import Dealer
from deck import Deck
from player import Player

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blackjack Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
input_box_color = (200, 200, 200)

# Fonts
font = pygame.font.SysFont(None, 48)

card_image = pygame.image.load('Assets/2_of_clubs.png')  # Update this path
scaled_card_image = pygame.transform.scale(card_image, (200, 300))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def get_user_bet(input_box, input_box_color):
    user_text = ''
    active = False
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle whether the input box is active based on user click.
                active = input_box.collidepoint(event.pos)

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if user_text.isdigit() and int(user_text) > 0:
                            done = True
                            return int(user_text)
                        else:
                            print("Invalid bet. Please enter a valid number.")
                            user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.unicode.isdigit():  # Ensure only numeric input is allowed.
                        user_text += event.unicode

        txt_surface = font.render(user_text, True, WHITE)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, input_box_color, input_box, 2 if active else 1)

        pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    
    while True:
        input_box = pygame.Rect(50, 450, 140, 32)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with a color
        screen.fill((0, 128, 0))  # Green background
        
        # Blit the image onto the screen at position (50, 50)
        draw_text(f"Dealer's Hand: ", font, WHITE, screen, 50, 20)
        screen.blit(scaled_card_image, (50, 100))
        
        # Update the display
        bet = get_user_bet(input_box, input_box_color)
        print("Bet entered:", bet)

        pygame.display.update()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
