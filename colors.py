class Colors:
    # MAIN GAME COLORS
    dark_grey = (60, 60, 60) # OUTER DESIGN
    green = (47, 230, 23) # L BLOCK
    red = (232, 18, 18) # J BLOCK
    orange = (226, 116, 17) # I BLOCK
    yellow = (237, 234, 4) # O BLOCK
    purple = (166, 0, 247) # S BLOCK
    cyan = (21, 204, 209) # T BLOCK
    blue = (13, 64, 216) # Z BLOCK
    white = (255, 255, 255) # MAIN GAME FONT
    black  = (20, 20, 20)  # MAIN GAME ALT FONT
    dark_blue = (80, 128, 191) # MAIN GAME UI OUTLINE
    
    # MAIN MENU BUTTON COLORS
    yellow_green = (197, 202, 31) # INSTRUCTIONS BUTTON
    dark_red = (163, 17, 17) # QUIT BUTTON
    bright_yellow = (255, 255, 0) # START BUTTON
    bright_blue = (0, 119, 255) # HIGH SCORES BUTTON
    
    @classmethod
    def get_cell_colors(cls):
        return [cls.black, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]