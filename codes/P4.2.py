def thomas_algorithm(A, b):
    n = len(b)
    a = [0] * n
    c = [0] * n
    x = [0] * n

    # 从矩阵 A 中提取三对角线系数
    for i in range(n):
        x[i] = A[i][i]
        if i > 0:
            a[i] = A[i][i - 1]
        if i < n - 1:
            c[i] = A[i][i + 1]

    # 第一步: 向前消元
    c_prime = [0] * n
    d_prime = [0] * n
    c_prime[0] = c[0] / x[0]
    d_prime[0] = b[0] / x[0]
    for i in range(1, n):
        m = 1.0 / (x[i] - a[i] * c_prime[i - 1])
        c_prime[i] = c[i] * m
        d_prime[i] = (b[i] - a[i] * d_prime[i - 1]) * m

    # 第二步: 回代
    x[n - 1] = d_prime[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i + 1]

    return x

# 举例:
A = [[2, 1, 0, 0], [1, 2, 1, 0], [0, 1, 2, 1], [0, 0, 1, 2]]
b = [5, 6, 7, 8]
x = thomas_algorithm(A, b)
print("方程组的解为：", x)
