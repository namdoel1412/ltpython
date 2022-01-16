t = int(input())

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
'X', 'Y', 'Z']

def doicoso(N, b):
    res = ""
    while N > 0:
        res+=alphabet[int(N%b)]
        N = int(N/b)
    print(res[::-1])

for i in range(0, t):
    lst = [int(i) for i in input().split()]
    doicoso(lst[0], lst[1])
