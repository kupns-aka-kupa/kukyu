import re


def mod4(s):
    return re.compile(".*\[[-+]?(?:"
                     "(?:\d*(?:0[048]|[2468][048]|[13579][26]))|"
                     "(?:[048])"
                     ")\]").match(s)
