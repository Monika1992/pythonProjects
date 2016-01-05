import random as rd
from abc import ABCMeta, abstractmethod
import time
import csv

# TODO: repair access modifiers in all classes from "protected" to "private"

class Player(object):

    __metaclass__ = ABCMeta

    def __init__(self, name, defense_game_board, offense_game_board):
        self._name = name
        self._defense_game_board = defense_game_board
        self._offense_game_board = offense_game_board

    @property
    def name(self):
        return self._name

    @property
    def defense_game_board(self):
        return self._defense_game_board

    @property
    def offense_game_board(self):
        return self._offense_game_board

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def spread_ships(self, ship_count):
        pass

    @abstractmethod
    def get_next_shoot_coords(self):
        pass

class HumanPlayer(Player):

    def __init__(self, name, defense_game_board, offense_game_board):
        super(HumanPlayer, self).__init__(name, defense_game_board, offense_game_board)

    # TODO: Implement spread_ships() method
    # TODO: Implement get_next_shoot_coords() method:

class ComputerPlayer(Player):

    def __init__(self, name, defense_game_board, offense_game_board):
        super(ComputerPlayer, self).__init__(name, defense_game_board, offense_game_board)

    def _randomly_place_ship(self):
        if self._defense_game_board.is_full() == True:
            raise Exception('Game board is full, cannot place other ship')

        random_x = rd.randint(0,self._defense_game_board.width-1)
        random_y = rd.randint(0,self._defense_game_board.height-1)
        was_ship_placed = self._defense_game_board.put_object(random_x, random_y, Ship())

        if was_ship_placed == False:
            self._randomly_place_ship()

    def spread_ships(self, ship_count):
        for i in range(ship_count):
            self._randomly_place_ship()


class RandomComputerPlayer(ComputerPlayer):

    def __init__(self, name, defense_game_board, offense_game_board):
        super(RandomComputerPlayer, self).__init__(name, defense_game_board, offense_game_board)

    def _get_random_coords(self):
        random_x = rd.randint(0,self._defense_game_board.width-1)
        random_y = rd.randint(0,self._defense_game_board.height-1)

        return [random_x, random_y]

    def get_next_shoot_coords(self):
        return self._get_random_coords()


class EvenComputerPlayer(ComputerPlayer):

    def __init__(self, name, defense_game_board, offense_game_board):
        super(EvenComputerPlayer, self).__init__(name, defense_game_board, offense_game_board)

        # TODO: implement get_next_shoot_coords() for even numbers only

    def get_next_shoot_coords(self):
        pass


class OddComputerPlayer(ComputerPlayer):

    def __init__(self, name, defense_game_board, offense_game_board):
        super(OddComputerPlayer, self).__init__(name, defense_game_board, offense_game_board)
        self._odd_x = -1
        self._odd_y = 0

    def _get_odd_coords(self):
        if self._odd_x == self.offense_game_board.width-1:
            self._odd_x = 1
            self._odd_y += 1
            if self._odd_y == self.offense_game_board.height:
                self._odd_x = +1
                self._odd_y = 0
        else:
            self._odd_x += 2

        print ("Odd Coords are: " + str([self._odd_x, self._odd_y]))
        return [self._odd_x, self._odd_y]

    def get_next_shoot_coords(self):
        return self._get_odd_coords()

class GraduallyComputerPlayer(ComputerPlayer):

    def __init__(self, name, defense_game_board, offense_game_board):
        super(GraduallyComputerPlayer, self).__init__(name, defense_game_board, offense_game_board)
        self._gradual_x = -1
        self._gradual_y = 0


    def _get_gradual_coords(self):

        if self._gradual_x == self.offense_game_board.width-1:
            self._gradual_x = 0
            self._gradual_y += 1
            if self._gradual_y == self.offense_game_board.height-1:
                self._gradual_x = 0
                self._gradual_y = 0
        else:
            self._gradual_x += 1

        return [self._gradual_x, self._gradual_y]

    def get_next_shoot_coords(self):
        return self._get_gradual_coords()

class GameBoard(object):

    def __init__(self, height, width):
        self._height = height
        self._width = width
        self.reset()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def _get_new_game_board(self):
        return [[None for x in range(self._height)] for x in range(self._width)]

    def reset(self):
        self.game_board = self._get_new_game_board()

    def is_there_object(self, x, y):
        if not self.are_coords_valid(x,y):
            return False

        if self.game_board[x][y] == None:
            return False

        return True

    def are_coords_valid(self, x, y):
        return -1 < x < self._width or -1 < y < self._height

    def put_object(self, x, y, object_instance):
        if self.is_there_object(x, y) == True:
            return False
        else:
            self.game_board[x][y] = object_instance
            return True

    def get_object(self, x, y):
        if not self.are_coords_valid(x,y):
            return None

        return self.game_board[x][y]

    def is_full(self):
        for x in range(self._width):
            for y in range(self._height):
                if self.is_there_object(x,y) == False:
                    return False

        return True

    def get_all_objects(self):
        all_objects = []
        for x in range(self._width):
            for y in range(self._height):
                if self.is_there_object(x,y) == True:
                    all_objects.append(self.get_object(x,y))

        return all_objects

    def print_board(self):
        for x in range(self._width):
            for y in range(self._height):
                if self.is_there_object(x,y):
                    print ("o"),
                else:
                    print ("."),
            print ("")

class Ship(object):

    def __init__(self):
        self._is_ship_destroyed = False

    @property
    def is_ship_destroyed(self):
        return self._is_ship_destroyed

    @is_ship_destroyed.setter
    def is_ship_destroyed(self, value):
        self._is_ship_destroyed = value


class Shot(object):

    def __init__(self, was_hit = False):
        self._was_hit = was_hit

    @property
    def was_hit(self):
        return self._was_hit

    @was_hit.setter
    def was_hit(self, value):
        self._was_hit = value


class Game(object):

    def __init__(self, player_1, player_2, game_board_size, ship_count, player_1_name, player_2_name):
        self._player_1 = self._create_player(player_1, player_1_name, game_board_size)
        self._player_2 = self._create_player(player_2, player_2_name, game_board_size)
        self._game_board_size = game_board_size
        self._ship_count = ship_count
        self._current_player = self._player_1

    @property
    def winner_player(self):
        return self._winner_player


    def start(self):
        self._spread_ships()

        round_number = 0

        while True:
            round_number += 1

            self._process_round()

            if self._is_game_finished():
                self._winner_player = self._current_player
                break
            else:
                self._print_round_state(round_number)
                self._switch_next_player()


    def _print_round_state(self, round_number):
        print ("Round number " + str(round_number) + ":")
        print ("----------------")
        print ("")
        print ("Player 1 defense:")
        self._player_1.defense_game_board.print_board()
        print ("Player 1 offense:")
        self._player_1.offense_game_board.print_board()

        print (" - - - - - - - - ")

        print ("Player 2 defense:")
        self._player_2.defense_game_board.print_board()
        print ("Player 2 offense:")
        self._player_2.offense_game_board.print_board()
        print ("")
        print ("")
        print ("")

    def _process_round(self):
        next_shoot_coords = self._current_player.get_next_shoot_coords()
        shoot_x = next_shoot_coords[0]
        shoot_y = next_shoot_coords[1]
        current_player_offense_game_board = self._current_player._offense_game_board
        other_player_defense_game_board = self._get_other_player(self._current_player)._defense_game_board

        current_player_offense_game_board.put_object(shoot_x, shoot_y, Shot())

        if other_player_defense_game_board.is_there_object(shoot_x, shoot_y) == True:
            other_player_defense_game_board.get_object(shoot_x, shoot_y)._is_ship_destroyed = True
            current_player_offense_game_board.put_object(shoot_x, shoot_y, Shot(True))
        else:
            current_player_offense_game_board.put_object(shoot_x, shoot_y, Shot())

    def _is_game_finished(self):
        if self._are_all_ships_destroyed(self._player_1.defense_game_board) or self._are_all_ships_destroyed(self._player_2.defense_game_board):
            return True

        return False

    def _get_winner(self):
        pass

    def _switch_next_player(self):
        self._current_player = self._get_other_player(self._current_player)

    def _get_other_player(self, player):
        if player == self._player_1:
            return self._player_2
        else:
            return self._player_1

    def _are_all_ships_destroyed(self, defense_game_board):
        all_ships = defense_game_board.get_all_objects()
        for ship in all_ships:
            if ship.is_ship_destroyed == False:
                return False
        return True

    def _create_player(self, player_string, name, game_board_size):

        defense_gameboard = GameBoard(game_board_size, game_board_size)
        offense_gameboard = GameBoard(game_board_size, game_board_size)

        player = None

        if player_string == "Random":
            player = RandomComputerPlayer(name, defense_gameboard, offense_gameboard)
        elif player_string == "Even":
            player = EvenComputerPlayer(name, defense_gameboard, offense_gameboard)
        elif player_string == "Odd":
            player = OddComputerPlayer(name, defense_gameboard, offense_gameboard)
        elif player_string == "Gradually":
            player = GraduallyComputerPlayer(name, defense_gameboard, offense_gameboard)

        return player

    def _spread_ships(self):
        self._player_1.spread_ships(self._ship_count)
        self._player_2.spread_ships(self._ship_count)


class GameStats(object):

    def __init__(self, game_data, start_time, end_time, played_games, player_1, player_2):
        self.data = game_data
        self.start_time = start_time
        self.end_time = end_time
        self.played_games = played_games
        self.player_1 = player_1
        self.player_2 = player_2
        self.win_stats = []

    def get_game_length(self):
        game_length = abs(self.end_time - self.start_time)
        return game_length/self.played_games

    def _count_stats(self):

        random_player_wins, gradually_player_wins, odd_player_wins, even_player_wins = 0, 0, 0, 0
        random_player_chance, gradually_player_chance, odd_player_chance, even_player_chance = 0, 0, 0, 0

        if self.data[0] == "Random":
            random_player_wins += self.data[2]
            random_player_chance += (self.data[2]*100)/self.played_games
        elif self.data[0] == "Gradually":
           gradually_player_wins += self.data[2]
           gradually_player_chance += (self.data[2]*100)/self.played_games
        elif self.data[0] == "Odd":
           odd_player_wins += self.data[2]
           odd_player_chance += (self.data[2]*100)/self.played_games
        elif self.data[0] == "Even":
            even_player_wins += self.data[2]
            even_player_chance += (self.data[2]*100)/self.played_games

        if self.data[1] == "Random":
            random_player_wins += self.data[3]
            random_player_chance += (self.data[2]*100)/self.played_games
        elif self.data[1] == "Gradually":
            gradually_player_wins += self.data[3]
            gradually_player_chance += (self.data[2]*100)/self.played_games
        elif self.data[1] == "Odd":
            odd_player_wins += self.data[3]
            odd_player_chance += (self.data[2]*100)/self.played_games
        elif self.data[1] == "Even":
            even_player_wins += self.data[3]
            even_player_chance += (self.data[2]*100)/self.played_games

        game_length = self.get_game_length()

        self.win_stats = [random_player_wins, gradually_player_wins, odd_player_wins, even_player_wins, game_length,
                     random_player_chance, gradually_player_chance, odd_player_chance, even_player_chance,
                          self.player_1, self.player_2]


    def _save_stats(self):
        with open ("game_stats.csv", "a") as file:
            wr = csv.writer(file)
            wr.writerow(self.win_stats)
            file.close()

player_1_victories = 0
player_2_victories = 0
player_1_type = "Gradually"
player_2_type = "Gradually"
player_1_name = "Player_1"
player_2_name = "Player_2"
played_games = 3
ship_count = 5
game_board_size = 10

start_time = time.time()
for i in range(played_games):
    game = Game(player_1_type, player_2_type, game_board_size, ship_count, player_1_name, player_2_name)
    game.start()
    winner = game.winner_player.name
    if winner == player_1_name:
        player_1_victories +=1
    elif winner == player_2_name:
        player_2_victories +=1
end_time = time.time()

data = [player_1_type, player_2_type, player_1_victories, player_2_victories]

game_stats = GameStats(data, start_time, end_time, played_games, player_1_type, player_2_type)
game_length = game_stats.get_game_length()
game_stats._count_stats()
game_stats._save_stats()


print ("Type: " + player_1_type + " Name: " + player_1_name + " won: " + str(player_1_victories) + " games out of: " + str(played_games))
print ("Type: " + player_2_type + " Name: " + player_2_name + " won: " + str(player_2_victories) + " games out of: " + str(played_games))




