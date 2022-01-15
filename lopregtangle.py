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
                res+= str(self.mau[i]).upper()
            else:
                res+=self.mau[i]
        return res

arr = input().split()
width = int(arr[0])
height = int(arr[1])
if(width <= 0 or height <= 0):
    print('INVALID')
else:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print(r.perimeter(), end=' ')
    print(r.area(), end=' ')
    print(r.color())
