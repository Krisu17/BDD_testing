import math
import sys

def returnEnthrophyLevel(inputString):
    d = inputString
    stat = {}
    for c in d:
        m = c
        if m in stat:
            stat[m] += 1
        else:
            stat[m] = 1
    H = 0.0
    for i in stat.keys():
        pi = stat[i]/len(d)
        H -= pi*math.log2(pi)
    if (H < 1.8):
        return "0"
    if (H < 2.4):
        return "1"
    if (H < 3):
        return "2"
    if (H < 3.5):
        return "3"
    else:
        return "4"