from grid import Grid
from blocks import *
import random
import pygame
from sound import SoundManager
from os import path
from colors import Colors

font_general = "fonts/general.ttf"
screen = pygame.display.set_mode((500, 620))

class Game:
    def __init__(self):
        """
        Initialize the game with a new grid, blocks, current block, next block,
        game over status, score, sound manager, and music playing status.
        """
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_blocks = [self.get_random_block() for _ in range(3)]
        self.game_over = False
        self.score = 0
        self.high_score() 
        self.sound_manager = SoundManager()  
        self.music_playing = False 

    def high_score(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, "highscore.txt"), 'r+') as f:
            try:
                self.high_score = int(f.read())
            except:
                self.high_score = 0

    def start_music(self):
        """
        Start playing the music if it's not already playing.
        """
        if not self.music_playing:
            self.sound_manager.play_music()
            self.music_playing = True

    def stop_music(self):
        """
        Stop playing the music if it's currently playing.
        """
        if self.music_playing:
            self.sound_manager.stop_music()
            self.music_playing = False

    def update_score(self, lines_cleared, move_down_points):
        """
        Update the score based on the number of lines cleared and the number of
        points earned from moving down.
        """
        point_font = pygame.font.Font(font_general, 20)
        points100_text = point_font.render("+100", True, Colors.white)
        points300_text = point_font.render("+300", True, Colors.white)
        points500_text = point_font.render("+500", True, Colors.white)
        
        if lines_cleared == 1:
            self.score += 100
            screen.blit(points100_text, (150, 310))
            pygame.display.update()
            pygame.time.delay(250)
        elif lines_cleared == 2:
            self.score += 300
            screen.blit(points300_text, (150, 310))
            pygame.display.update()
            pygame.time.delay(250)
        elif lines_cleared >= 3:
            self.score += 500
            screen.blit(points500_text, (150, 310))
            pygame.display.update()
            pygame.time.delay(250)
        self.score += move_down_points

        if self.score >= self.high_score:
            self.high_score = self.score
            with open(path.join(self.dir, "highscore.txt"), 'w') as f:
                f.write(str(self.score))

    def get_random_block(self):
        """
        Get a random block from the list of blocks, and remove it from the list.
        If the list is empty, reset the list to the original blocks.
        """
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        """
        Move the current block one cell to the left. If the block is not inside
        the grid or does not fit, move it back to its original position.
        """
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        """
        Move the current block one cell to the right. If the block is not inside
        the grid or does not fit, move it back to its original position.
        """
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        """
        Move the current block one cell down. If the block is not inside the
        grid or does not fit, move it back up and lock it into the grid.
        """
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        """
        Lock the current block into the grid by updating the grid with the
        block's positions, setting the current block to the next block,
        getting a new random block, and checking for any rows that have been
        cleared.
        """
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_blocks.pop(0)  # Use the first next block
        self.next_blocks.append(self.get_random_block())  # Add a new block to the queue
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.sound_manager.play_clear_sound()
            self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True

    def reset(self):
        """
        Resets the game to its initial state.
        """
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        #self.high_score = self.score
        self.score = 0

    def block_fits(self):
        """
        Checks if the current block fits in the grid without overlapping.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def rotate(self):
        """
        Rotates the current block if it's possible without overlapping or leaving the grid.
        """
        # Check if the current block is not an O-shaped block (which doesn't rotate)
        if not isinstance(self.current_block, OBlock):
            self.current_block.rotate()
            if not self.block_inside() or not self.block_fits():
                self.current_block.undo_rotation()
            else:
                self.sound_manager.play_rotate_sound()
                
    def block_inside(self):
        """
        Checks if the current block is inside the grid.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        # Adjust starting positions for the preview
        x_start, y_start = 255, 240
        for i, block in enumerate(self.next_blocks):
            # Initial y position for each block, with adjusted spacing
            y_position = y_start + (i * 90)  

            # Apply specific adjustments for each block type if necessary
            if isinstance(block, IBlock):
                # Special case for IBlock, if any special handling is needed
                adjusted_x = x_start
                adjusted_y = y_position + 15
            elif isinstance(block, OBlock):
                # Slightly adjust the position for OBlock to visually center it
                adjusted_x = x_start
                adjusted_y = y_position - 5
            else:
                # For other blocks, apply a generic adjustment
                adjusted_x = x_start + 15
                adjusted_y = y_position

            # Draw the block at the adjusted position
            block.draw(screen, adjusted_x, adjusted_y)
