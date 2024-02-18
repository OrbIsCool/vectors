from draw import *
import pygame as pg
from line import Line
from itertools import permutations


class Tick:
    def __init__(s):
        xm, ym = pg.mouse.get_pos()
        s.xm = xm
        s.ym = ym
        s.kp = pg.key.get_pressed()
        s.mp = pg.mouse.get_pressed()
        s.x = SCREEN_DIM[0] / 2
        s.y = SCREEN_DIM[1] / 2
        s.lines = (
            Line(s.x, s.y, s.x + 100, s.y + 100, (255, 0, 0)),
            Line(s.x, s.y, s.x - 100, s.y - 100, (0, 255, 0)),
            Line(s.x, s.y, s.x + 100, s.y - 100, (0, 0, 255)),
            Line(s.x, s.y, s.x - 100, s.y + 100, (0, 255, 255)),
            Line(s.x, s.y, s.x - 100, s.y + 150, (255, 255, 0)),
            Line(s.x, s.y, s.x - 100, s.y + 150, (100, 100, 0)),
            Line(s.x, s.y, s.x - 100, s.y + 150, (255, 0, 255)),
        )
        s.current = None
        s.gr = s.graph()

    def const(s):  # will do every time
        screen.fill((0, 0, 0))
        xm, ym = pg.mouse.get_pos()
        s.xm = xm
        s.ym = ym
        s.kp = pg.key.get_pressed()
        s.mp = pg.mouse.get_pressed()
        if s.kp[pg.K_ESCAPE]:
            quit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

    def screen_1(s):
        s.const()
        line_points(s.x, 0, s.x, SCREEN_DIM[1])
        line_points(0, s.y, SCREEN_DIM[0], s.y)
        s.draw()
        for l1 in s.lines:
            center_size(l1.x2, l1.y2, 10, 10, (255, 255, 255))
            if s.mp[0]:
                if s.current is l1:
                    l1.x2 = s.xm
                    l1.y2 = s.ym
                elif not s.current:
                    if -10 < s.xm - l1.x2 < 10:
                        if -10 < s.ym - l1.y2 < 10:
                            s.current = l1
            else:
                s.current = None

        # x = y = 0
        # for line in s.lines:
        # x += line.x2 - s.x
        # y += line.y2 - s.y
        # line_points(s.x, s.y, x + s.x, y + s.y, 8, (255, 255, 255))
        pygame.display.flip()

    def draw1(s):
        for p in permutations(s.lines, len(s.lines)):
            last_diff: Line = None
            for i in p:
                last_diff = i.draw(last_diff=last_diff)

    def draw(s):
        s.draw_node1(s.gr, None)

    def draw_node(s, root, last_diff):
        # for loop
        items = [(root, last_diff)]
        for n, d in items:
            if n.v:
                d = n.v.draw(last_diff=d)

            for child in n.child.values():
                items.append((child, d))

    def draw_node1(s, root, last_diff):
        # recursion
        if root.v:
            last_diff = root.v.draw(last_diff=last_diff)

        for child in root.child.values():
            s.draw_node1(child, last_diff)

    def screen_2(s):
        s.const()
        # code here
        pygame.display.flip()

    def graph(s):
        root = Node()
        for lines in permutations(s.lines, len(s.lines)):
            runner = root
            for l in lines:
                runner = runner.add(Node(l))
        return root


class Node:
    def __init__(self, v: Line = None):
        self.v = v
        self.id = v.id if v else None
        self.child = dict()

    def add(self, n: "node"):
        if n.id not in self.child:
            self.child[n.id] = n
        return self.child[n.id]
