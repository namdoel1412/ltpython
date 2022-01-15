class LuongMua:
    startTime: str
    endTime: str
    luongMua: float
    duration: float

    def __init__(self, startTime: str, endTime: str, luongMua: float):
        self.startTime = startTime
        self.endTime = endTime
        self.luongMua = luongMua
        t1 = [int(i) for i in startTime.split(':')]
        t2 = [int(i) for i in endTime.split(':')]
        time1 = t1[0]*60+t1[1]
        time2 = t2[0]*60+t2[1]
        self.duration = time2 - time1

t = int(input())
dic = {}
for i in range(0, t):
    tramDo = input()
    startTime = input()
    endTime = input()
    luongMua = float(input())
    td1 = LuongMua(startTime, endTime, luongMua)
    if tramDo not in dic:
        dic[tramDo] = [td1.duration, td1.luongMua]
    else:
        dic[tramDo] = [dic[tramDo][0] + td1.duration, dic[tramDo][1] + td1.luongMua]
    k = 1
for item in dic.keys():
    print('T0' + str(k), end=' ')
    print(item, end=' ')
    #print(dic)
    tmp = str(round(dic[item][1]/(dic[item][0]/60), 2))
    length = len(tmp)
    res = -1
    for j in range(0, length):
        if tmp[j] == '.':
            res = j
            break
    if length - res -1 < 2:
        for j in range(0, 2 - (length - res -1)):
            tmp+='0'
    print(tmp)
    k+=1