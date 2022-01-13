class Point:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    p1 = 0
    p2 = 0

t = int(input())
for i in range(0, t):
    lst = [float(k) for k in input().split()]
    point1 = Point(lst[0], lst[1])
    point2 = Point(lst[2], lst[3])
    distance = ((point2.p1 - point1.p1)**2 + (point2.p2 - point1.p2)**2)**0.5
    res = round(distance, 4)
    tmp = str(res)
    length = len(tmp)
    count = 5
    for j in range(0, length):
        if tmp[j] == '.':
            count = 0
        else:
            count+=1
    if count < 4:
        for j in range(0, 4-count):
            tmp+='0'
    print(tmp)