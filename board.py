"""
Module has board of the game
"""
from typing import List, Tuple
from cell import Cell
from ladder import Ladder
from snake import Snake


class Board:
    """
    Board class has details of board, snake, ladder,
    start point and end point
    """
    cells = []
    snakes = []
    ladders = []
    partition_limit = 10

    def __init__(self, start: int,
                 end: int,
                 snake_points: List[Tuple],
                 ladder_points: List[Tuple]):
        """
        Init
        Args:
            start: game start point
            end: game end point
            snake_points: snakes positions on the board
            ladder_points: ladders positions on the board
        """
        self.start = start
        self.end = end
        self.snake_points = snake_points
        self.ladder_points = ladder_points

    @staticmethod
    def check_snake(cell):
        """
        Check if cell is associated with snake
        Args:
            cell: cell details

        Returns:
            True or False
        """
        for snake in Board.snakes:
            if snake.head.x == cell.x and snake.head.y == cell.y:
                return snake
        return None

    @staticmethod
    def check_ladder(cell):
        """
        Check if cell is associate with the ladder
        Args:
            cell: cell details

        Returns:
            True or False
        """
        for ladder in Board.ladders:
            if ladder.start.x == cell.x and ladder.start.y == cell.y:
                return ladder
        return None

    def create_board(self):
        """
        method populates board of the game
        """
        self.create_cells()
        self.create_snakes()
        self.create_ladders()

    def create_cells(self):
        """
        Creates cells
        """
        index = self.start
        y = 0
        while index <= self.end:
            x = 1
            while x <= Board.partition_limit:
                index = index + 1
                Board.cells.append(Cell(x, y))
                x = x + 1
            y = y + 1

    def _get_cell(self, point) ->Cell:
        """
        Gets cells x and y co-ordinates
        Args:
            point: point number in the board

        Returns:
            Cell object
        """
        return Cell(point % Board.partition_limit, point // Board.partition_limit)

    def create_snakes(self):
        """
        Creates snake for board
        """
        for snake_point in self.snake_points:
            Board.snakes.append(Snake(self._get_cell(snake_point[0]),
                                      self._get_cell(snake_point[1])))

    def create_ladders(self):
        """
        Creates ladder for board
        """
        for ladder_point in self.ladder_points:
            Board.ladders.append(Ladder(self._get_cell(ladder_point[0]),
                                        self._get_cell(ladder_point[1])))

    def print_board(self):
        """
        Shows boards information such as cell, snake and ladder

        """
        self.create_board()
        index = 0
        for cell in Board.cells:
            if index == Board.partition_limit:
                index = 0
                print("\n")

            print(cell.get_x(), cell.get_y())
            index = index + 1

        for snake in Board.snakes:
            snake_head = snake.get_head()
            snake_tail = snake.get_tail()
            print("snake head %s, %s", snake_head.get_x(), snake_head.get_y())
            print("snake tail %s, %s", snake_tail.get_x(), snake_tail.get_y())

        for ladder in Board.ladders:
            start = ladder.get_start()
            end = ladder.get_end()
            print("ladder start %s, %s", start.get_x(), start.get_y())
            print("ladder end %s, %s", end.get_x(), end.get_y())
