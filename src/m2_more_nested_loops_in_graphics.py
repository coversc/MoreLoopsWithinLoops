"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Caitlin Coverstone.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------

    upper_left = rectangle.get_upper_left_corner()
    lower_right = rectangle.get_lower_right_corner()

    x1 = upper_left.x
    x2 = lower_right.x
    y1 = upper_left.x
    y2 = lower_right.y

    cent_x = (x1 + x2)/2
    cent_y = (y1 + y2)/2

    dx = lower_right.x - upper_left.x
    dy = upper_left.y - lower_right.y

    for j in range (n):
        cy = cent_y + j* dy
        for k in range(j+1):
            cx = cent_x + k * dx

            x1 = cx-dx/2
            y1 = cy+dy/2
            x2 = cx+dx/2
            y2 = cy-dy/2

            new_rectangle = rg.Rectangle(rg.Point(x1,y1), rg.Point(x2,y2))
            new_rectangle.attach_to(window)
            window.render()
        cent_x = cent_x - dx/2






# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
