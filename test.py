import math
import sys

seed = int(input())


ct = 0
ans = 0


wums = set()

wums_ct = 0

while wums_ct < 4:
    seed = seed + math.floor(seed//13) + 15
    lx, ly = (seed % 100) // 10, seed % 10
    # if wums.add((lx, ly)):
    #     wums_ct += 1
    if (lx, ly) not in wums:
        wums.add((lx, ly))
        wums_ct += 1



for line in sys.stdin:
    data = int(line)
    x, y = data // 10, data % 10
    if ct < 4:
        ans += 1
    dist = float('inf')



    if ct < 4  and (x, y) in wums:
        ct += 1
        print('You hit a wumpus!')
        wums.remove((x, y))
        # print(wums)


    if ct < 4:
        for lx, ly in wums:
            dist = min(dist, (abs(lx - x) + abs(ly - y)))
        print(int(dist))


print(f"Your score is {ans} moves.")