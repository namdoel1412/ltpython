class BXH:
    name: str
    correct: int
    submit: int

    def __init__(self, name: str, correct: int, submit: int):
        self.name = name
        self.correct = correct
        self.submit = submit


t = int(input())
res = []
for i in range(0, t):
    name = input()
    lst = [int(i) for i in input().split()]
    bxh = BXH(name, lst[0], lst[1])
    res.append(bxh)

res = sorted(sorted(sorted(res, key=lambda x:x.name), key=lambda x:x.submit), key=lambda x:x.correct, reverse=True)

for item in res:
    print(item.name + ' ' + str(item.correct) + ' ' + str(item.submit))
