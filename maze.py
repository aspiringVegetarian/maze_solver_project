from graphics import Window, Point, Line
import time

class Cell():
    
    def __init__(
        self,  p1, p2, window = None,
        has_top_wall = True,
        has_right_wall = True, 
        has_bottom_wall = True,
        has_left_wall = True):

        self._win = window
        self._x1 = p1.x 
        self._y1 = p1.y 
        self._x2 = p2.x 
        self._y2 = p2.y
        self._middle = Point( (p1.x + p2.x)/2 , (p1.y + p2.y)/2 )
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall
        self._visited = False
    
    def draw(self):
        if self.has_top_wall:
            line_color = "green"
        else:
            line_color = "white"
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), line_color)
        
        if self.has_right_wall:
            line_color = "green"
        else:
            line_color = "white"
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), line_color)

        if self.has_bottom_wall:
            line_color = "green"
        else:
            line_color = "white"
        self._win.draw_line(Line(Point(self._x2, self._y2), Point(self._x1, self._y2)), line_color)

        if self.has_left_wall:
            line_color = "green"
        else:
            line_color = "white"
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x1, self._y1)), line_color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "gray"
        else:
            line_color = "red"
        self._win.draw_line(Line(self._middle, to_cell._middle) , line_color)

import random

class Maze():

    def __init__(
        self,
        x1, y1,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        window=None, seed = None
    ):
        random.seed(seed)
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = [ [0 for _ in range(num_cols)] for _ in range(num_rows) ]

        self._create_cells()
        self._draw_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
    
    def _create_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                top_left_x = self.x1 + self.cell_size_x * j
                top_left_y = self.y1 + self.cell_size_y * i
                bottom_right_x = self.x1 + self.cell_size_x * (j + 1)
                bottom_right_y = self.y1 + self.cell_size_y * (i + 1)
                self._cells[i][j] = Cell(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y), self.window)

    def _draw_cells(self):
        if self.window:
            for row in self._cells:
                for cell in row:
                    cell.draw()
                    self.window.redraw()
                    time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        
        if self.window:
            self._cells[0][0].draw()
            self._cells[-1][-1].draw()
            self.window.redraw()
    
    def _break_walls_r(self, i, j):
        while True:
            # visit current
            current = self._cells[i][j]
            current._visited = True

            # find adjacent cells that could be potential directions
            to_visit = []
            # check left
            if j > 0:
                left_cell = self._cells[i][j-1]
                if not left_cell._visited:
                    to_visit.append((i, j-1, "left", left_cell))
            # check top
            if i > 0:
                top_cell = self._cells[i-1][j]
                if not top_cell._visited:
                    to_visit.append((i-1, j, "top", top_cell))
            # check right
            if j < len(self._cells[0]) - 1:
                right_cell = self._cells[i][j+1]
                if not right_cell._visited:
                    to_visit.append((i, j+1, "right", right_cell))
            # check bottom
            if i < len(self._cells) - 1:
                bottom_cell = self._cells[i+1][j]
                if not bottom_cell._visited:
                    to_visit.append((i+1, j, "bottom", bottom_cell))
            
            # if there are no possible moves, draw current and return to break out of loop
            if not to_visit:
                if self.window:
                    current.draw()
                    self.window.redraw()
                return
            
            # choose a direction at random, break the corresponding wall and then move to the new cell
            i, j, direction, target = random.choice(to_visit)
            if direction == "left":
                current.has_left_wall = False
                target.has_right_wall = False
            elif direction == "top":
                current.has_top_wall = False
                target.has_bottom_wall = False
            elif direction == "right":
                current.has_right_wall = False
                target.has_left_wall = False
            elif direction == "bottom":
                current.has_bottom_wall = False
                target. has_top_wall = False
            else:
                raise Exception("...something broke")
            
            if self.window:
                current.draw()
                self.window.redraw()
            
            self._break_walls_r(i,j)
            

            
            
