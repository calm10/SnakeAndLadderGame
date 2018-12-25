"""
Module has ladder class
"""
from cell import Cell


class Ladder:
    """
    Ladder class
    """

    def __init__(self, start: Cell, end: Cell):
        """
        Init
        Args:
            start: start cell of the ladder
            end: end cell of the ladder
        """
        self.start = start
        self.end = end

    def get_start(self) -> Cell:
        return self.start

    def get_end(self) -> Cell:
        return self.end
