from colors import Colors
import pygame
from position import Position

class Block:
    """
    This class represents a block in a game.
    Each block has an id, cells, cell_size, row_offset, column_offset, 
    rotation_state, and colors.
    """
    def __init__(self, id):
        self.id = id
        self.cells = {} # dictionary to store the positions of cells in different rotation states
        self.cell_size = 30 # size of each cell
        self.row_offset = 0 # number of rows to move the block downwards
        self.column_offset = 0 # number of columns to move the block to the right
        self.rotation_state = 0 # current rotation state of the block
        self.colors = Colors.get_cell_colors() # colors for the cells
        self.texture = None  # Attribute to hold the texture image
        

    def move(self, rows, columns):
        """
        Moves the block by the specified number of rows and columns.
        """
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        """
        Returns the positions of the cells in the current rotation state,
        taking into account the row and column offsets.
        """
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        """
        Rotates the block to the next rotation state.
        """
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        """
        Rotates the block to the previous rotation state.
        """
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1