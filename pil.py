import re

from PIL import Image

import q


RE_TYPE = re.compile("^\S+")
RE_OBJ_ENTRY = re.compile("\s+")


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, color=None):
        global canvas
        canvas[self.x, center[1]-self.y] = color or (255, 255, 255)

    def copy(self):
        return Point(self.x, self.y)


def triangle(coords):
    a, b, c = sorted(coords, key=lambda p: p.y)
    p1 = a.copy()
    p2 = a.copy()
    delta_p1 = float(b.x - a.x) / (b.y - a.y)
    delta_p2 = float(c.x - a.x) / (c.y - a.y)
    for y in (b.y, c.y):
        while p1.y < y:
            if p1.x > p2.x:
                p3 = p2.copy()
                x = p1.x
            else:
                p3 = p1.copy()
                x = p2.x
            while p3.x < x:
                p3.show()
                p3.x += 1
            p1.show()
            p1.y += 1
            p1.x += delta_p1
            p2.show()
            p2.y += 1
            p2.x += delta_p2
            delta_p1 = float(c.x - b.x) / (c.y - b.y)


screen = 800, 600
center = 400, 300

img = Image.new("RGB", (screen[0] + 1, screen[1] + 1), "black")
canvas = img.load()

with open("face.obj", "r") as source:
    lines = source.read().split("\n")

points = []
for line in lines:
    match = RE_TYPE.match(line)
    if match:
        if match.group() == "v":
            etype, x, y, z = RE_OBJ_ENTRY.split(line)
            x = (float(x) + 1) * center[0]
            y = screen[1] - (float(y) + 1) * center[1]
            canvas[x, y] = (255, 255, 255)
            points.append(Point(x, y))
        elif match.group() == "f":
            entry = RE_OBJ_ENTRY.split(line)
            q.q([points[int(el.split("/")[0])-1] for el in entry[1:]])

img.show()
