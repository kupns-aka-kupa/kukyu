import re


def whitespace_number(n):
    s = str(bin(n))
    replace = [["-0b", "\t"], ["0b0", " "], ["0b", " "], ["1", "\t"], ["0", " "]]
    for r in replace:
        s = s.replace(*r)
    return s + "\n"
