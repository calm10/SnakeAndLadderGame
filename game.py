"""
Game module
"""
import time
from board import Board
from player import Player
from dice import get_dice_number
from cell import Cell


class Game:
    """
    Game class has information about player and board
    """
    board = None
    players = []
    winners = []

    def __init__(self, start, end, player_count):
        """
        Init
        Args:
            start: start point of the game
            end: end point of the game
            player_count: number of player
        """
        self.start = start
        self.end = end
        self.player_count = player_count

    @staticmethod
    def get_player_detail():
        """
        Get name of the player
        Returns:
            Player Model
        """
        name = input("Enter Player name \n")
        initial_position = Cell(0, 0)
        return Player(name, initial_position)

    def populate_players(self):
        """
        Fill players required information

        """
        index = 0

        while index < self.player_count:
            Game.players.append(Game.get_player_detail())
            index = index + 1

    @staticmethod
    def print_players():
        """
        Show players information

        """
        for player in Game.players:
            print(player.get_name())

    def create_board(self):
        """
        Create board

        """
        snake_points = [(99, 7), (83, 17), (73, 2), (64, 29), (52, 11), (44, 19), (28, 6)]
        ladder_points = [(21, 82), (5, 50), (8, 26), (66, 87), (43, 77), (62, 96), (54, 93)]
        Game.board = Board(self.start, self.end, snake_points, ladder_points)
        Game.board.print_board()

    def start_game(self):
        """
        Populate player and board information and start the play

        """
        self.populate_players()
        Game.print_players()
        self.create_board()
        print("play starts")
        self.play()
        print("play ends")

    def play(self):
        """
        Start Rolling dice and give each player a chance
        """
        index = 0
        while Game.players:
            player = Game.players[index]
            print("player name is " + player.get_name())
            dice_number = get_dice_number()
            print("dice number %s", dice_number)
            print("player current position is ")
            self.move_player(player, dice_number)
            if self.check_player_won(player):
                Game.players.pop(index)
                Game.winners.append(player)
                continue

            if not DiceRules.get_next_chance(dice_number):
                index = (index + 1) % self.player_count

            time.sleep(1)

    def check_player_won(self, player):
        """
        Check if player has reached the target
        Args:
            player: player object

        Returns:
            True or False
        """
        if (player.position.x + player.position.y*10) == self.end:
            return True
        return False

    def move_player(self, player, dice_number):
        """
        Move player as per dice number and check if player has
        not reached a cell where snake can bite or player can climb the ladder
        Args:
            player: player object
            dice_number: dice number
        """
        if ((player.position.x == 0 and player.position.y==0) and DiceRules.can_player_starts(dice_number)) or (player.position.x != 0 or player.position.y!=0):

            player_position = player.position
            print(player_position.x, player_position.y, end='')
            new_position = (player_position.x + player_position.y * 10) + dice_number
            print("new player's position would be")
            print(new_position)

            if new_position > self.end:
                return

            player_position.x = new_position % 10
            player_position.y = new_position // 10
            print("new player's position is")
            print(new_position)

            snake = Board.check_snake(player_position)
            if snake is not None:
                print("Snake bites")
                player_position.x = snake.tail.x
                player_position.y = snake.tail.y

            ladder = Board.check_ladder(player_position)
            if ladder is not None:
                print("Climb the ladder")
                player_position.x = ladder.end.x
                player_position.y = ladder.end.y

            player.position = player_position


class DiceRules:
    """
    Dice Game rules
    """
    @staticmethod
    def get_next_chance(dice_number: int) -> bool:
        """
        Check if player will get next chance
        Args:
            dice_number: dice number

        Returns:
            True or False
        """
        if dice_number == 6 or dice_number == 1:
            return True
        return False

    @staticmethod
    def can_player_starts(dice_number: int) -> bool:
        """
        Check if player can start the play or not
        Args:
            dice_number: dice number

        Returns:
            True or False
        """
        if dice_number == 6:
            return True
        return False


def main():
    """

    Returns:

    """
    print("start the game")
    player_count = input("How many players are going to play\n")
    game = Game(1, 100, int(player_count))
    game.start_game()


if __name__ == '__main__':
    main()