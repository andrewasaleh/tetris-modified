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
game_over_surface = title_font.render("GAME OVER", True, Colors.red)
continue_surface = title_font.render("Press any key to play again", True, Colors.white)

# Game rectangles for score and next block
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 280)

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
        # Button properties
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

        screen.fill(Colors.dark_blue) # Main Menu

        title_text = title_font.render("Python Tetris", True, Colors.black)
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
        screen.fill(Colors.dark_blue) # Loading Screen
        countdown_text = countdown_font.render(str(i), True, Colors.white)
        countdown_rect = countdown_text.get_rect(center=(250, 300))
        screen.blit(countdown_text, countdown_rect)
        pygame.display.update()
        pygame.time.delay(1000)

    # Start the game after countdown
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

    # Sound and music flags
    game_over_sound_played = False
    music_playing = True

    paused = False  # Pause state flag

    # Start background music
    sound_manager.play_music()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Toggle pause with the Esc key, only if the game is not over
                if event.key == pygame.K_ESCAPE and not game.game_over:
                    paused = not paused
                    if paused:
                        pygame.mixer.music.pause()  # Pause the music
                    else:
                        pygame.mixer.music.unpause()  # Resume the music

                # Game over condition: press any key to restart
                if game.game_over:
                    # Reset the game state to start a new game
                    game.reset()
                    game.game_over = False
                    game_over_sound_played = False
                    if not music_playing:
                        sound_manager.play_music()
                        music_playing = True
                    paused = False  # Ensure game is not paused when restarting
                    continue  # Skip the rest of the loop to immediately start the new game

                # Game control keys, only active if not paused and game is not over
                if not paused and not game.game_over:
                    if event.key == pygame.K_LEFT:
                        game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        game.move_right()
                    elif event.key == pygame.K_DOWN:
                        game.move_down()
                        game.update_score(0, 1)
                    elif event.key == pygame.K_UP:
                        game.rotate()
                
            # Automatically move the block down if the game is ongoing and not paused
            if event.type == GAME_UPDATE and not game.game_over and not paused:
                game.move_down()

        if not paused:
            # Game logic updates
            screen.fill(Colors.dark_blue)
            screen.blit(score_surface, (365, 20))
            screen.blit(next_surface, (375, 180))
            pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
            score_value_surface = title_font.render(str(game.score), True, Colors.black)
            screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
            pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
            game.draw(screen)
        else:
            # Display paused message
            paused_text = title_font.render("Paused - Press Esc to Resume", True, Colors.white)
            paused_rect = paused_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(paused_text, paused_rect)

        # Drawing
        score_value_surface = title_font.render(str(game.score), True, Colors.black)
        screen.fill(Colors.dark_grey)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                    centery=score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)
        
        # Draw the game over screen on top of everything, including the paused message if necessary
        if game.game_over:
            if not game_over_sound_played:
                sound_manager.play_game_over_sound()
                game_over_sound_played = True  # Prevents replaying the sound
                pygame.mixer.music.stop()  # Stop music
                music_playing = False
            
            # Calculate positions for the surfaces
            game_over_rect = game_over_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 20))
            continue_rect = continue_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 20))
            
            # Color for the rectangle box
            box_color = (0, 0, 0, 192)  # Full black with 50% transparency
            padding = 20
            box_width = max(game_over_rect.width, continue_rect.width) + padding * 2
            box_height = (continue_rect.bottom - game_over_rect.top) + padding * 2
            box_x = screen.get_width() / 2 - box_width / 2
            box_y = game_over_rect.top - padding

            # Create a new Surface with per-pixel alpha (for semi-transparency)
            box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
            box_surface.fill(box_color)

            # Blit the box surface to the screen at the calculated position
            screen.blit(box_surface, (box_x, box_y))

            # Then blit the text surfaces over the box
            screen.blit(game_over_surface, game_over_rect)
            screen.blit(continue_surface, continue_rect)

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