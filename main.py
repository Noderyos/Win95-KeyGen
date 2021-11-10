from random import randint as rdi
maxs = [i for i in range(9*7) if i%7==0][1:]
while True:
    max = maxs[rdi(0,len(maxs) - 1)]
    key += str(rdi(0,9)) + str(rdi(0,9)) + str(rdi(0,9)) + "-"
    for i in range(7):
        val = rdi(0,9)
        if max - val > 0:
            key += str(val)
            max -= val
        else:
            key += str(max)
            max = 0
    print(key)