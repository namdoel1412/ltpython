class SoPhuc:
    phanThuc: int
    phanAo: int
    def __init__(self, phanThuc, phanAo):
        self.phanThuc = phanThuc
        self.phanAo = phanAo

def tongSP(a: SoPhuc, b: SoPhuc):
    return SoPhuc(a.phanThuc + b.phanThuc, a.phanAo + b.phanAo)

def tichSP(a: SoPhuc, b: SoPhuc):
    return SoPhuc(a.phanThuc*b.phanThuc - a.phanAo*b.phanAo, a.phanThuc*b.phanAo + a.phanAo*b.phanThuc)

t = int(input())
for i in range(0, t):
    lst = [int(i) for i in input().split()]
    sp1 = SoPhuc(lst[0], lst[1])
    sp2 = SoPhuc(lst[2], lst[3])
    tmp1 = tongSP(sp1, sp2)
    C = tichSP(tmp1, sp1)
    D = tichSP(tmp1, tmp1)
    if(C.phanAo < 0):
        print(C.phanThuc, end=' - ')
        print(abs(C.phanAo), end='i, ')
    else:
        print(C.phanThuc, end=' + ')
        print(abs(C.phanAo), end='i, ')

    if(D.phanAo < 0):
        print(D.phanThuc, end=' - ')
        print(abs(D.phanAo), end='i')
    else:
        print(D.phanThuc, end=' + ')
        print(abs(D.phanAo), end='i')
    print()

