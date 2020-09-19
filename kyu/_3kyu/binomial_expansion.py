import re


def binomial(n, k):
    return factorial(1, n) // (factorial(1, k) * factorial(1, n - k))


def factorial(f, n):
    return factorial(f * n, n - 1) if n > 1 else f


def parse(expr):
    var = re.search(r'[a-z]', expr).group(0)
    return var, map(int, [re.sub(r'-$', "-1", i) if i else "1"
                          for i in re.split(rf'(?:{var})|(?:\)\^)', expr[1:])])


def expand(expr):
    var, (a, b, p) = parse(expr)
    c = [a ** (p - i) * b ** i * binomial(p, i) for i in range(p + 1)]

    res = list(map(str, c[:1])) + list(map(lambda i: str(i) if i < 0 else "+" + str(i), c[1:]))
    out = []
    for i in range(len(res)):
        s = res[i]
        if p - i > 0:
            s += f"{var}"
            if abs(int(res[i])) == 1:
                s = s.replace('1', "")
        if p - i > 1:
            s += f"^{p - i}"
        print(s)
        out.append(s)
    print(out)
    return "".join(out)
