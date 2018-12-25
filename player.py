"""
Module has information about player
"""
from cell import Cell


class Player:
    """
    Player class
    """

    def __init__(self, name: str, position: Cell):
        """
        Init
        Args:
            name: name of the player
            position: start position of the player
        """
        self.name = name
        self.position = position

    def get_name(self) -> str:
        return self.name

    def get_position(self) -> Cell:
        return self.position
