def format_duration(s):
    if s == 0:
        return "now"
    time = [[s, "second"],
            [0, "minute"],
            [0, "hour"],
            [0, "day"],
            [0, "year"]]
    factors = [60, 60, 24, 365]
    for i in range(len(factors)):
        if time[i][0] < factors[i]:
            break
        time[i + 1][0] = time[i][0] // factors[i]
        time[i][0] %= factors[i]

    out = [" ".join(map(str, i)) + ("s" if i[0] > 1 else "") for i in time[::-1] if i[0] > 0]
    if len(out) > 1:
        return " and ".join([", ".join(out[:-1]), out[-1]])
    else:
        return " ".join(out)
