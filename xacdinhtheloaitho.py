t = int(input())
res = 0
tutuyet = 0
lucbat = 0
lst = []
sobai = 1
for i in range(0, t):
    tmp = len(input().split())
    lst.append(tmp)
res = []
if lst[0] == 6:
    lucbat = 1
    res.append(1)
step = 0

for i in range(0, t):
    if lst[i] == 7:
        step+=1
    if step == 4:
        tutuyet+=1
        res.append(2)
        step = 0
    if lst[i] == 7 and i+1 < t and lst[i+1] == 6:
        lucbat += 1
        res.append(1)
print(tutuyet + lucbat)
for item in res:
    print(item)
