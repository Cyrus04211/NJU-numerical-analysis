import numpy as np
import matplotlib.pyplot as plt

def polyval(a, x): #在Matlab中已经内置了polyval方法, 可直接使用. 
    # 计算多项式 a[0]x^{n-1} + a[1]x^{n-2} + ... + a[n-1]
    n = len(a)
    y = np.zeros(len(x))
    cheby = np.zeros([n,len(x)])
    # 颠倒数组a
    a = a[::-1]
    y = a[0] + a[1]*x
    cheby[0] = np.ones(len(x))
    cheby[1] = x
    for i in range(2, n): #计算多项式的算法
        cheby[i]=2*x*cheby[i-1]-cheby[i-2]
        y += a[i]*cheby[i]
    return y
# def chebyshev(deg, x):
#     m = len(x)
#     y = np.zeros([deg + 1,m])
#     y[0] = np.ones(m)
#     y[1] = x
#     if deg > 1:
#         for i in range(2, deg + 1):
#             y[i] = 2 * x * y[i-1] - y[i-2]

#     return y[deg]

def polyfit(xdata, ydata, deg): #给定xdata和ydata, 返回多项式. 
    m = len(xdata)
    n = deg + 1
    xdatas = np.zeros([n,m])
    xdatas[0] = np.ones(m)
    xdatas[1] = xdata
    for i in range(2,n):    # 用不断迭代的方法得到xdata的幂次.
        xdatas[i] = 2 * xdata * xdatas[i-1] - xdatas[i-2] 

    # 装配矩阵 A (3x3矩阵, 分量分别为a_0, a_1, a_2.)
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            A[i][j] = np.dot(xdatas[n-1-i],xdatas[n-1-j])

    print(np.linalg.cond(A))

    # 装配右端向量 b
    b = np.zeros(n)
    for i in range(n):
        b[i] = np.dot(xdatas[n-1-i],ydata)

    # 解方程组
    a = np.linalg.solve(A, b)
    return a


if __name__ == "__main__": 
    xdata = np.array([0.000, 0.895, 1.641, 2.512, 3.542, 4.054, 4.602, 5.063, 5.354, 5.617])
    ydata = np.array([1.000, 1.803, 3.680, 7.320, 13.59, 17.41, 22.19, 24.89, 26.55, 29.77])
    m = len(ydata)

    deg = 9
    # 输出数据
    a = polyfit(xdata, ydata, deg)
    print(a)
    yfit = polyval(a, xdata)
    print('Loss:', np.linalg.norm(ydata-yfit)/m)
    
    # 画图
    x_draw = np.linspace(0, 6, 100)
    y_draw = polyval(a, x_draw)
    plt.plot(xdata,ydata, 'ro')
    plt.plot(x_draw,y_draw, 'b')
    plt.savefig('P7.4.png')
    plt.show()
