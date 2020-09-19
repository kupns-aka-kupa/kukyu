import re


def pig_it(s):
    out = s
    words = re.findall(r'\w+', s)
    swap = [i[1:] + i[0] + "ay" for i in words]
    for i in range(len(words)):
        out = re.sub(rf'\b{words[i]}\b', swap[i], out)
    return out
