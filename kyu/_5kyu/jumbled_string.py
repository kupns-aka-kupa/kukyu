
def jumbled_string(s, x):
    print(len(s), s, x)

    for i in range(x):
        s = s[::2] + s[1::2]
    return s
