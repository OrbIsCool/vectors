from uuid import uuid4
import draw
import game


class Line:
    def __init__(s, x1, y1, x2, y2, color) -> None:
        s.x1 = x1
        s.x2 = x2
        s.y1 = y1
        s.y2 = y2
        s.color = color
        s.id = uuid4().int

    def draw(s, last_diff=None):
        last_diff = last_diff or (0, 0)
        d_x = last_diff[0]
        d_y = last_diff[1]

        draw.line_points(
            s.x1 + d_x,
            s.y1 + d_y,
            s.x2 + d_x,
            s.y2 + d_y,
            3,
            s.color,
        )

        return (d_x + (s.x2 - s.x1), d_y + (s.y2 - s.y1))
