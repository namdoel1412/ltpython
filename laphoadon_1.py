from cProfile import label


class HoaDon:
    hoTen: str
    old: float
    new: float
    maKH: str
    sl: float
    thanhTien: float

    def __init__(self, hoTen, old, new, maKH):
        self.hoTen = hoTen
        self.old = old
        self.new = new
        self.maKH = maKH
        self.sl = new - old
        self.TinhTien()

    def TinhTien(self):
        tmp = self.sl
        res = 0
        if tmp >= 101:
            res = 50*100 + 50*150 + (tmp-100)*200
            res += res*0.05
        elif tmp >= 51:
            res += 50*100 + (tmp-50)*150
            res += res*0.03
        else:
            res += tmp*100
            res += res*0.02
        
        self.thanhTien = round(res)


t = int(input())
lst = []
for i in range(1, t+1):
    hoTen = input()
    old = float(input())
    new = float(input())
    maKH = ""
    if i < 10:
        maKH = "KH0"+str(i)
    else:
        maKH = "KH"+str(i)
    hd = HoaDon(hoTen, old, new, maKH)
    lst.append(hd)

lstSorted = sorted(sorted(lst, key=lambda x:x.maKH), key=lambda x:x.thanhTien, reverse=True)
for item in lstSorted:
    print(item.maKH + ' ' + item.hoTen + ' ', end='')
    print(item.thanhTien)



