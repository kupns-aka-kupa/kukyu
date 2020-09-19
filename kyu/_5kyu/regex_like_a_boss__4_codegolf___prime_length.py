import re

REGEX = r"^(?!(xx+)\1+$|x$)x+$"


def prime_len(s):
    return re.compile(REGEX).match(s)
