def rotate_in_place(m):
    n = len(m)
    for i in range(0, n // 2):
        for j in range(i, n - i - 1):
            temp = m[j][i]
            m[j][i] = m[n - 1 - i][j]
            m[n - 1 - i][j] = m[n - 1 - j][n - 1 - i]
            m[n - 1 - j][n - 1 - i] = m[i][n - 1 - j]
            m[i][n - 1 - j] = temp
    return m
