from cmath import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(a: Point, b: Point):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

t = int(input())
for i in range(0, t):
    lst = [float(i) for i in input().split()]
    p1 = Point(lst[0], lst[1])
    p2 = Point(lst[2], lst[3])
    p3 = Point(lst[4], lst[5])
    d1 = distance(p1, p2)
    d2 = distance(p2, p3)
    d3 = distance(p1, p3)
    if (d1+d2==d3 or d1+d3==d2 or d2+d3==d1):
        print("INVALID")
    else:
        tmp = round(d1+d2+d3, 3)
        print(tmp)
