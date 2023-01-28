import sys


def read_maze(fileName):
    file = open(fileName, 'r', encoding='utf-8')
    MAZE = [i for i in file.readlines()]
    file.close()
    return Maze(MAZE)


class Maze:
    def __init__(self, maze):
        self.MAZE = maze

    def get_position(self, x, y):
        if x > self.get_height() - 1 or y > self.get_width() - 1:
            return None
        return Position((x, y), self.MAZE)

    def get_height(self):
        return len(self.MAZE)

    def get_width(self):
        return len(self.MAZE)

    def __str__(self):
        res = ""
        for i in self.MAZE:
            res += i
        return res


class Position:
    symbols = [" ", "╴", "╷", "┐", "╶", "─", "┌", "┬", "╵", "┘", "│", "┤", "└", "┴", "├", "┼"]

    up = ["╵", "┘", "└", "┴"]
    down = ["╷", "┐", "┌", "┬"]
    up_and_down = ["│", "┤", "├", "┼"]

    left = ["╴", "┘", "┐", "┤"]
    right = ["╶", "└", "┌", "├"]
    middle = ["─", "┴", "┬", "┼"]
    blank = " "

    def __init__(self, coord: tuple, maze: list):
        self.X = coord[0]
        self.Y = coord[1]
        self.MAZE = maze

    def has_direction(self, direction: str):
        x, y, m = self.X, self.Y, self.MAZE
        direction = direction.lower()

        if direction == 'north':  # Go up
            if x == 0:
                return False
            elif m[x][y] in self.up + self.up_and_down:
                if m[x - 1][y] in self.down + self.up_and_down: return True
        elif direction == 'south':  # Go down
            if x != len(m)-1:
                if m[x][y] in self.down + self.up_and_down:
                    if m[x + 1][y] in self.up + self.up_and_down: return True

        elif direction == 'west':  # Go left
            if y == 0:
                return False
            if m[x][y] in self.left + self.middle:
                if m[x][y - 1] in self.right + self.middle: return True
        elif direction == 'east':  # Go right
            if y != len(m[0]) - 1:
                if m[x][y] in self.right + self.middle:
                    if m[x][y + 1] in self.left + self.middle: return True
        return True

    def is_exit(self):
        x, y, m = self.X, self.Y, self.MAZE
        if len(m) == 1 and len(m[0]) == 1: return m[0][0] != " "
        if x == 0:
            if y == 0: return False
            if m[0][y] in self.up + self.up_and_down: return True
        elif x == len(m) - 1:
            if m[x][y] in self.down + self.up_and_down: return True
        elif y == 0:
            if x == 0: return False
            if m[x][0] in self.left + self.middle: return True
        elif y == len(m[0]) - 1:
            if m[x][y] in self.right + self.middle: return True
        return False

    def __str__(self):
        return str(self.MAZE[self.x][self.y])

