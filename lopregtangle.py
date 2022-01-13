class Rectangle:
    width = 0
    height = 0
    mau = ''
    def __init__(self, width, height, mau):
        self.width = width
        self.height = height
        self.mau = mau

    def perimeter(self):
        return (self.width+self.height)*2

    def area(self):
        return (self.width*self.height)
    
    def color(self):
        self.mau = self.mau.lower()
        length = len(self.mau)
        res = ""
        for i in range(0, length):
            if i == 0:
                res+= str(self.mau[i]+"").upper()
            else:
                res+=self.mau[i]
        return res


if __name__ == '__main__':
    arr = input().split()
    if len(arr) > 3:
        print('INVALID')
    else:
        r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))