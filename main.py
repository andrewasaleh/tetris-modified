import pygame
import sys
from game import Game
from colors import Colors
from sound import SoundManager 

# Initialize Pygame
pygame.init()

# Game fonts
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Game rectangles for score and next block
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Game screen
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Game clock
clock = pygame.time.Clock()

# Game and sound manager
game = Game()
sound_manager = SoundManager() 

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, font, font_color):
        # Initialize button properties
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.font_color = font_color

    def draw(self, screen):
        # Draw the button on the screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, pos):
        # Check if the mouse is hovering over the button
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height

# Start button
start_button = Button("Start", 200, 300, 100, 50, Colors.green, Colors.blue, title_font, Colors.white)

def main_menu():
    # Fonts for the main menu
    title_font = pygame.font.Font(None, 50)
    option_font = pygame.font.Font(None, 40)

    # Button properties for the main menu
    button_width = 200
    button_height = 60

    start_button = Button("Start Game", 150, 200, button_width, button_height, Colors.bright_yellow, Colors.dark_grey, option_font, (0, 0, 0))
    instructions_button = Button("Instructions", 150, 300, button_width, button_height, Colors.green, Colors.dark_grey, option_font, (0, 0, 0))
    high_scores_button = Button("High Scores", 150, 400, button_width, button_height, Colors.bright_blue, Colors.dark_grey, option_font, (0, 0, 0))
    quit_button = Button("Quit", 150, 500, button_width, button_height, Colors.red, Colors.dark_grey, option_font, (0, 0, 0))

    # Main menu event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_hovered(pygame.mouse.get_pos()):
                    return "Start"
                elif instructions_button.is_hovered(pygame.mouse.get_pos()):
                    return "Instructions"
                elif high_scores_button.is_hovered(pygame.mouse.get_pos()):
                    return "High Scores"
                elif quit_button.is_hovered(pygame.mouse.get_pos()):
                    return "Quit"

        screen.fill(Colors.dark_blue)

        title_text = title_font.render("Python Tetris", True, Colors.white)
        title_rect = title_text.get_rect(center=(250, 100))
        screen.blit(title_text, title_rect)

        start_button.draw(screen)
        instructions_button.draw(screen)
        high_scores_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.update()
        clock.tick(60)

# Launch main menu
menu_option = main_menu()

if menu_option == "Start":
    # Countdown 3 2 1 before starting game
    countdown_font = pygame.font.Font(None, 100)
    for i in range(3, 0, -1):
        screen.fill(Colors.dark_blue)
        countdown_text = countdown_font.render(str(i), True, Colors.white)
        countdown_rect = countdown_text.get_rect(center=(250, 300))
        screen.blit(countdown_text, countdown_rect)
        pygame.display.update()
        pygame.time.delay(1000)

    # Start the game after countdown
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

    # Start playing music
    sound_manager.play_music()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        # Drawing
        score_value_surface = title_font.render(str(game.score), True, Colors.white)

        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))

        if game.game_over == True:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                      centery=score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)

# Launch main menu
menu_option = main_menu()

if menu_option == "Start":
    # Start playing music
    sound_manager.play_music()

    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

    # Start the countdown before the game starts
    start_countdown()