import re


def strip_comments(s, m):
    pattern = '\\'.join(m) if len(m) else "\\"
    return re.sub(rf' *[\{pattern}].*', '', s)
