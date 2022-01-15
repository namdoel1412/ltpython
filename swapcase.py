inp = input()
length = len(inp)
for i in range(0, length):
    if inp[i].islower():
        print(inp[i].upper(), end='')
    else:
        print(inp[i].lower(), end='')
print()