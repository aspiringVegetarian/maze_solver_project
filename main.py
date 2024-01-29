from graphics import Window, Point, Line
from maze import Cell, Maze

def main():

    """   
    # B
    window.draw_line(Line(Point(20, 20), Point(20, 80)), 'blue')
    window.draw_line(Line(Point(20, 20), Point(50, 20)), 'blue')
    window.draw_line(Line(Point(20, 50), Point(50, 50)), 'blue')
    window.draw_line(Line(Point(20, 80), Point(50, 80)), 'blue')
    window.draw_line(Line(Point(50, 20), Point(50, 50)), 'blue')
    window.draw_line(Line(Point(50, 50), Point(50, 80)), 'blue')

    # O
    window.draw_line(Line(Point(70, 20), Point(70, 80)), 'blue')
    window.draw_line(Line(Point(100, 20), Point(100, 80)), 'blue')
    window.draw_line(Line(Point(70, 20), Point(100, 20)), 'blue')
    window.draw_line(Line(Point(70, 80), Point(100, 80)), 'blue')

    # 2nd O
    window.draw_line(Line(Point(120, 20), Point(120, 80)), 'blue')
    window.draw_line(Line(Point(150, 20), Point(150, 80)), 'blue')
    window.draw_line(Line(Point(120, 20), Point(150, 20)), 'blue')
    window.draw_line(Line(Point(120, 80), Point(150, 80)), 'blue')

    # T
    window.draw_line(Line(Point(170, 20), Point(200, 20)), 'blue')
    window.draw_line(Line(Point(185, 20), Point(185, 80)), 'blue')

    # S
    window.draw_line(Line(Point(220, 20), Point(250, 20)), 'blue')
    window.draw_line(Line(Point(220, 20), Point(220, 50)), 'blue')
    window.draw_line(Line(Point(220, 50), Point(250, 50)), 'blue')
    window.draw_line(Line(Point(250, 50), Point(250, 80)), 'blue')
    window.draw_line(Line(Point(250, 80), Point(220, 80)), 'blue')

    """
    screen_x = 800
    screen_y = 700
    window = Window(screen_x, screen_y)

    margin = 50
    num_rows = 15
    num_cols = 15
    cell_size_x = (screen_x - (2 * margin)) / num_cols
    cell_size_y = (screen_y - (2 * margin)) / num_rows
    seed = None

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window, seed)

    window.wait_for_close()


main()