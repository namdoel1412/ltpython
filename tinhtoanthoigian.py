from audioop import reverse


class Gamer:
    id: str
    name: str
    startTime: str
    endTime: str
    duration: int
    useTime: str

    def __init__(self, id: str, name: str, startTime: str, endTime: str):
        self.id = id
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        t1 = [int(i) for i in startTime.split(':')]
        t2 = [int(i) for i in endTime.split(':')]
        self.duration = t2[0]*60+t2[1] - (t1[0]*60+t1[1])
        self.Calculate()
    
    def Calculate(self):
        hh = int(self.duration/60)
        mm = self.duration - hh*60
        self.useTime = str(hh) + " gio " + str(mm) + " phut"

t = int(input())
dic = {}
lst = []
for i in range(0, t):
    id = input()
    name = input()
    startTime = input()
    endTime = input()
    gamer = Gamer(id, name, startTime, endTime)
    lst.append(gamer)

lstSorted = sorted(sorted(lst, key=lambda x:x.id), key=lambda x:x.duration, reverse=True)
for item in lstSorted:
    print(item.id + ' ' + item.name + ' ' + item.useTime)




