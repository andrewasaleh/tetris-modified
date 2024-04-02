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
high_score_surface = title_font.render("High Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)

font_title = "fonts/title.ttf"
font_general = "fonts/general.ttf"

# text design
game_over_font_size = 50
game_over_font = pygame.font.Font(font_general, game_over_font_size)

continue_font_size = 30
continue_font = pygame.font.Font(font_general, continue_font_size)

# Render the game over and ask for user input
game_over_surface = game_over_font.render("GAME OVER", True, Colors.red)
continue_surface = continue_font.render("Press any key to play again", True, Colors.white)

# Game rectangles for score and next block
score_rect = pygame.Rect(320, 55, 170, 60)
high_score_rect = pygame.Rect(325, 555, 170, 60)
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
        # Check if the mouse is hovering over the button to choose the color
        mouse_pos = pygame.mouse.get_pos()  # Get the mouse position
        if self.is_hovered(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        # Draw the button with rounded corners
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), border_radius=10)

        # Create and draw the button text
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, pos):
        # Check if the mouse is hovering over the button
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height

# Start button
#start_button = Button("Start", 200, 300, 100, 50, Colors.green, Colors.blue, title_font, Colors.white)

def main_menu():
    # Fonts for the main menu
    title_font = pygame.font.Font(font_title, 60)
    option_font = pygame.font.Font(font_general, 40)

    # Button properties for the main menu
    button_width = 200
    button_height = 60

    start_button = Button("Start Game", 150, 170, button_width, button_height, Colors.bright_yellow, Colors.dark_grey, option_font, (0, 0, 0))
    instructions_button = Button("Instructions", 150, 250, button_width, button_height, Colors.green, Colors.dark_grey, option_font, (0, 0, 0))
    high_scores_button = Button("High Scores", 150, 330, button_width, button_height, Colors.bright_blue, Colors.dark_grey, option_font, (0, 0, 0))
    quit_button = Button("Quit", 150, 410, button_width, button_height, Colors.red, Colors.dark_grey, option_font, (0, 0, 0))

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

        screen.fill(Colors.dark_grey) # Main Menu

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

# Gamme Loop for the main menu while the user has not choset to quit the game
while(menu_option != "Quit"):
    # Start playing the game!
    if menu_option == "Start":
        # Countdown 3 2 1 before starting game
        countdown_font = pygame.font.Font(font_general, 100)
        for i in range(3, 0, -1):
            screen.fill(Colors.dark_grey) # Loading Screen
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
                        print("Paused:", paused)  # Debug print

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
                screen.blit(high_score_surface, (345, 520))
                screen.blit(next_surface, (375, 180))
                pygame.draw.rect(screen, Colors.black, score_rect, 0, 10)
                score_value_surface = title_font.render(str(game.score), True, Colors.black)
                high_value_surface = title_font.render(str(game.high_score), True, Colors.black)
                screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
                screen.blit(high_value_surface, high_value_surface.get_rect(centerx=high_score_rect.centerx, centery=high_score_rect.centery))

                pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)
                game.draw(screen)
            else:
                # Display paused message
                paused_text = title_font.render("Paused - Press Esc to Resume", True, Colors.white)
                paused_rect = paused_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
                screen.blit(paused_text, paused_rect)

            # Drawing
            score_value_surface = title_font.render(str(game.score), True, Colors.white)
            high_value_surface = title_font.render(str(game.high_score), True, Colors.white)
            screen.fill(Colors.dark_grey)
            screen.blit(score_surface, (365, 20, 50, 50))
            screen.blit(high_score_surface, (345, 520, 50, 50))    #This is for the word "High Score"
            screen.blit(next_surface, (375, 180, 50, 50))

            pygame.draw.rect(screen, Colors.black, score_rect, 0, 10)
            screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                        centery=score_rect.centery))
            pygame.draw.rect(screen, Colors.black, high_score_rect, 0, 10)
            screen.blit(high_value_surface, high_value_surface.get_rect(centerx=high_score_rect.centerx,
                                                                        centery=high_score_rect.centery))
            pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)
            game.draw(screen)
            
            score_font_size = 30  # Size for score font
            score_font = pygame.font.Font(font_general, score_font_size)

            high_font_size = 30  # Size for score font
            high_font = pygame.font.Font(font_general, high_font_size)

            next_font_size = 30  # Size for next block font
            next_font = pygame.font.Font(font_general, next_font_size)

            # Render "Score" and "Next" using the custom fonts
            score_surface = score_font.render("Score", True, Colors.white)
            high_score_surface = score_font.render("High Score", True, Colors.white)
            next_surface = next_font.render("Next", True, Colors.white)

            if paused:
                # Screen dimensions for reference
                screen_width, screen_height = screen.get_size()
                
                # Define the semi-transparent box properties
                box_color = (0, 0, 0, 192)  # Semi-transparent black
                padding = 20  # Padding around the text for the box
                
                # Generate the paused text surface and rect
                paused_text = title_font.render("Paused - Press Esc to Resume", True, Colors.white)
                paused_rect = paused_text.get_rect(center=(screen_width / 2, screen_height / 2))
                
                # Box dimensions based on the text size plus padding
                box_width = paused_rect.width + padding * 2
                box_height = paused_rect.height + padding * 2
                box_x = paused_rect.x - padding
                box_y = paused_rect.y - padding
                
                # Create a new Surface with per-pixel alpha for semi-transparency
                box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
                box_surface.fill(box_color)  # Fill the surface with the semi-transparent color
                
                # Blit the semi-transparent box to the screen at the position
                screen.blit(box_surface, (box_x, box_y))
                
                # Blit the paused text over the box
                screen.blit(paused_text, paused_rect)
                
                pygame.display.update()  # Ensure the screen updates to show the pause message

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

    # Displays the instructions on how to play the game as well as the point system and how to pause the game
    if menu_option == "Instructions":

        instruction_font = pygame.font.Font(font_general, 50)
        screen.fill(Colors.dark_grey) # Loading Screen
        instruction_text = instruction_font.render("INSTRUCTIONS:", True, Colors.white)
        instruction_rect = instruction_text.get_rect(center=(140, 50))
        screen.blit(instruction_text, instruction_rect)
        
        rule_font = pygame.font.Font(font_general, 25) #Font for the rules
        rule1_text = rule_font.render("Press Down to move block faster", True, Colors.white)
        rule1_rect = rule1_text.get_rect(center=(175, 100))
        screen.blit(rule1_text, rule1_rect)

        rule2_text = rule_font.render("Press Left to move block to the left", True, Colors.white)
        rule2_rect = rule2_text.get_rect(center=(200, 150))
        screen.blit(rule2_text, rule2_rect)

        rule3_text = rule_font.render("Press Right to move block to the right", True, Colors.white)
        rule3_rect = rule3_text.get_rect(center=(205, 200))
        screen.blit(rule3_text, rule3_rect)

        rule4_text = rule_font.render("Press 'esc' to pause/unpause game", True, Colors.white)
        rule4_rect = rule4_text.get_rect(center=(185, 250))
        screen.blit(rule4_text, rule4_rect)

        points_font = pygame.font.Font(font_general, 50) #Font for the point system
        points_text = points_font.render("POINTS:", True, Colors.white)
        points_rect = points_text.get_rect(center=(75, 325))
        screen.blit(points_text, points_rect)
        
        pts1_text = rule_font.render("Down key = +1pt", True, Colors.white)
        pts1_rect = pts1_text.get_rect(center=(100, 375))
        screen.blit(pts1_text, pts1_rect)

        pts2_text = rule_font.render("1 line complete = +100pts", True, Colors.white)
        pts2_rect = pts2_text.get_rect(center=(140, 425))
        screen.blit(pts2_text, pts2_rect)

        pts3_text = rule_font.render("2 lines complete = +300pts", True, Colors.white)
        pts3_rect = pts3_text.get_rect(center=(145, 475))
        screen.blit(pts3_text, pts3_rect)

        pts4_text = rule_font.render("3 lines complete = +500pts", True, Colors.white)
        pts4_rect = pts4_text.get_rect(center=(145, 525))
        screen.blit(pts4_text, pts4_rect)

        pygame.display.update()
        pygame.time.delay(5000)

    # Displays the current high score for 3s
    if menu_option == "High Scores":
        hs_font = pygame.font.Font(font_general, 40)
        screen.fill(Colors.dark_grey) # Loading Screen
        hs_text = hs_font.render(f"CURRENT HIGH SCORE: {game.high_score}", True, Colors.white)
        hs_rect = hs_text.get_rect(center=(250, 150))
        screen.blit(hs_text, hs_rect)

        pygame.display.update()
        pygame.time.delay(3000)

    # Launch main_menu() again
    menu_option = main_menu()

#if menu_option == "Start":
    # Start playing music
#    sound_manager.play_music()

#    GAME_UPDATE = pygame.USEREVENT
#    pygame.time.set_timer(GAME_UPDATE, 200)

    # Start the countdown before the game starts
    #start_countdown()