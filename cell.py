"""
Module has cell attributes of the board game
"""


class Cell:
    """
    Cell Class
    """

    def __init__(self, x: int, y: int):
        """
        Init the args
        Args:
            x: x co-ordinate of the cell
            y: y co-ordinate of the cell

        """
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self)-> int:
        return self.y
