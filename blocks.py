import pygame
from movement import Block
from position import Position

class LBlock(Block):
    def __init__(self):
        # L-shaped block with a unique ID
        super().__init__(id=1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # Move the block to the initial position

        # Load image for L block
        self.image = pygame.image.load("Images/green_block.png")

    def draw(self, screen, offset_x, offset_y):
        """
        Draws the L-shaped block with texture on the screen, taking into account the row and column offsets.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            screen.blit(self.image, (offset_x + tile.column * self.cell_size, 
                                     offset_y + tile.row * self.cell_size))

class JBlock(Block):
    def __init__(self):
        # J-shaped block with a unique ID
        super().__init__(id=2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)  # Move the block to the initial position

    def draw(self, screen, offset_x, offset_y):
        """
        Draws the J-shaped block with texture on the screen, taking into account the row and column offsets.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            texture = pygame.image.load("Images/red_block.png")  # Load the texture image
            texture_rect = texture.get_rect()
            texture_rect.topleft = (offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size)
            screen.blit(texture, texture_rect)

class IBlock(Block):
    def __init__(self):
        # I-shaped block with a unique ID
        super().__init__(id=3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)  # Move the block to the initial position

    def draw(self, screen, offset_x, offset_y):
        """
        Draws the I-shaped block with texture on the screen, taking into account the row and column offsets.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            texture = pygame.image.load("Images/orange_block.png")  # Load the texture image
            texture_rect = texture.get_rect()
            texture_rect.topleft = (offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size)
            screen.blit(texture, texture_rect)

class OBlock(Block):
    def __init__(self):
        # O-shaped block with a unique ID
        super().__init__(id=4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)  # Move the block to the initial position

    def draw(self, screen, offset_x, offset_y):
        """
        Draws the O-shaped block with texture on the screen, taking into account the row and column offsets.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            texture = pygame.image.load("Images/yellow_block.png")  # Load the texture image
            texture_rect = texture.get_rect()
            texture_rect.topleft = (offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size)
            screen.blit(texture, texture_rect)

class SBlock(Block):
    def __init__(self):
        # S-shaped block with a unique ID
        super().__init__(id=5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

    def draw(self, screen, offset_x, offset_y):
        """
        Draws the S-shaped block with texture on the screen, taking into account the row and column offsets.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            texture = pygame.image.load("Images/purple_block.png")  # Load the texture image
            texture_rect = texture.get_rect()
            texture_rect.topleft = (offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size)
            screen.blit(texture, texture_rect)
class TBlock(Block):
    def __init__(self):
        # T-shaped block with a unique ID
        super().__init__(id=6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # Move the block to the initial position

    def draw(self, screen, offset_x, offset_y):
        """
        Draws the T-shaped block with texture on the screen, taking into account the row and column offsets.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            texture = pygame.image.load("Images/cyan_block.png")  # Load the texture image
            texture_rect = texture.get_rect()
            texture_rect.topleft = (offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size)
            screen.blit(texture, texture_rect)

class ZBlock(Block):
    def __init__(self):
        # Z-shaped block with a unique ID
        super().__init__(id=7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)  # Move the block to the initial position

    def draw(self, screen, offset_x, offset_y):
        """
        Draws the Z-shaped block with texture on the screen, taking into account the row and column offsets.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            texture = pygame.image.load("Images/blue_block.png")  # Load the texture image
            texture_rect = texture.get_rect()
            texture_rect.topleft = (offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size)
            screen.blit(texture, texture_rect)