import sys


class Position:
    symbols = [" ", "╴", "╷", "┐", "╶", "─", "┌", "┬", "╵", "┘", "│", "┤",
               "└", "┴", "├", "┼"]

    def has_direction(self, direction):
        return False

    def is_exit(self):
        return False


class Maze:

    def get_position(self, x, y):
        return None

    def get_height(self):
        return 0

    def get_width(self):
        return 0


def read_maze(filename):
    return None


if __name__ == "__main__":
    #You can do whatever you want here.
    pass
