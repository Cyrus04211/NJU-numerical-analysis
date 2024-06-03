import numpy as np


def gaussian_elimination(A, b):
    n = len(A)
 
    # 将数组的数据类型转换为float64
    A = A.astype(np.float64)
    b = b.astype(np.float64)
 
    # 高斯消元
    for i in range(n - 1):
        max_idx = i
 
        # 选取列主元
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_idx][i]):
                max_idx = j
 
        # 交换行
        A[[i, max_idx]] = A[[max_idx, i]]
        b[[i, max_idx]] = b[[max_idx, i]]
 
        for j in range(i + 1, n):
            # 计算倍数
            multiplier = A[j][i] / A[i][i]
 
            # 更新矩阵
            A[j][i:] -= multiplier * A[i][i:]
            b[j] -= multiplier * b[i]
 
    # 回代求解
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i + 1:], x[i + 1:])) / A[i][i]
 
    return x

# 举例
A=np.array([[2,1,-1],
            [-3,-1,2],
            [-2,1,2]])
b=np.array([8,-11,-3])
x=gaussian_elimination(A,b)
print("方程组的解为：", x)
