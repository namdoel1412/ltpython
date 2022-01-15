class DiemThiSinh:
    hoTen = ''
    diem1 = 0
    diem2 = 0
    diem3 = 0

    def __init__(self, hoTen, diem1, diem2, diem3):
        self.hoTen = hoTen
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    
    def hienthi(self):
        print(self.hoTen, end=' ')
        td = self.diem1*0.1 + self.diem2*0.3 + self.diem3*0.6
        print(round(td, 1))
    
hoTen = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
ts = DiemThiSinh(hoTen, diem1, diem2, diem3)
ts.hienthi()

