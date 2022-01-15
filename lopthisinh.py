import string


class ThiSinh:
    hoTen: string
    ngaySinh: string
    point1: float
    point2: float
    point3: float
    tongDiem: float
    def __init__(self, hoTen: string, ngaySinh: string, point1: float, point2: float, point3: float):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.tongDiem = point1 + point2 + point3

ts = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
print(ts.hoTen, end=' ')
print(ts.ngaySinh, end=' ')
print(round(ts.tongDiem, 1))