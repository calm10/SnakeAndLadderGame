"""
Module has snake parameters of the game
"""
from cell import Cell

class Snake:
    """
    Snake class ha
    """

    def __init__(self, head: Cell, tail: Cell):
        """
        Init
        Args:
            head: head of the snake
            tail: tail of the snake

        """
        self.head = head
        self.tail = tail

    def get_head(self)->Cell:
        return self.head

    def get_tail(self) ->Cell:
        return self.tail
