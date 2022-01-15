def calTB(lst):
    tmp = (lst[0]*2 + lst[1]*2 + lst[2] + lst[3] + lst[4] + lst[5] + lst[6] + lst[7] + lst[8] + lst[9])/12
    return tmp

class BangDiem:
    hoTen: str
    toan: float
    tv: float
    mon3: float
    mon4: float
    mon5: float
    mon6: float
    mon7: float
    mon8: float
    mon9: float
    mon10: float
    MaSV: str
    trungbinh: float
    hocLuc: str
    
    def __init__(self, hoTen: str, lst, MaSV: str, tb = 0):
        self.hoTen = hoTen
        self.toan = lst[0]
        self.tv = lst[1]
        self.mon3 = lst[2]
        self.mon4 = lst[3]
        self.mon5 = lst[4]
        self.mon6 = lst[5]
        self.mon7 = lst[6]
        self.mon8 = lst[7]
        self.mon9 = lst[8]
        self.mon10 = lst[9]
        self.MaSV = MaSV
        tmp = float((float(lst[0])*2) + float(lst[1])*2 + float(lst[2]) + float(lst[3]) + float(lst[4]) + float(lst[5]) + float(lst[6]) + float(lst[7]) + float(lst[8]) + float(lst[9]))/12
        tmp2 = (sum(lst) + lst[0] + lst[1]) / 12
        self.trungbinh = round(tmp2, 1)
        # print(round(7.65, 1))
        if self.trungbinh >= 9:
            self.hocLuc = "XUAT SAC"
        elif self.trungbinh >= 8:
            self.hocLuc = "GIOI"
        elif self.trungbinh >= 7:
            self.hocLuc = "KHA"
        elif self.trungbinh >= 5:
            self.hocLuc = "TB"
        else:
            self.hocLuc = "YEU"

t = int(input())
lst = []
for i in range(1, t+1):
    hoTen = input()
    diem = [float(j) for j in input().split()]
    msHS = ""
    if i < 10:
        msHS = "HS0"+str(i)
    else:
        msHS = "HS"+str(i)
    bd1 = BangDiem(hoTen, diem, msHS)
    lst.append(bd1)
lst = sorted(sorted(lst, key = lambda x:x.MaSV), key=lambda x:x.trungbinh, reverse=True)
for item in lst:
    print(item.MaSV + ' ' + item.hoTen + ' ' + str(item.trungbinh) + ' ' + item.hocLuc)

        
    