class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)
    
    # New colors for buttons
    yellow_green = (197, 202, 31)
    dark_red = (163, 17, 17)
    bright_orange = (255, 165, 0)
    bright_yellow = (255, 255, 0)
    light_purple = (194, 103, 255)
    bright_cyan = (0, 255, 255)
    bright_blue = (0, 119, 255)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]