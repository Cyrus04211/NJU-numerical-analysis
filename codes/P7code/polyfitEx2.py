import numpy as np
import matplotlib.pyplot as plt

def polyval1(a, x): 
    # 计算多项式 a[0]x^{n-1} + a[1]x^{n-2} + ... + a[n-1]
    n = len(a)
    y = np.zeros(len(x))
    # 颠倒数组a
    a = a[::-1]
    for i in range(n):
        y += a[i] * x**i
    return y

def polyval2(a, x, f): 
    n = len(a)
    y = np.zeros(len(x))
    # 颠倒数组a
    a = a[::-1]
    y = a[0]
    for i in range(1,n):
        y += a[i] * f[i-1](x)
    return y

def polyfit(xdata, ydata, f): 
    # 给定xdata和ydata, 函数f, 返回广义多项式. 
    # f可以输入数字，如果输入数字，那么就表示多项式的次数. 
    # f也可以输入函数数组f=[f1, ..., f_n]，表示广义多项式拟合，同时加上常值函数. 
    m = len(xdata)

    if(type(f)==int): #多项式
        n = f + 1 #f表示deg
        xdatas = np.zeros([n,m])
        xdatas[0] = np.ones(m)
        for i in range(1, n):    # 用不断迭代的方法得到xdata的幂次.
            xdatas[i] = xdatas[i-1] * xdata 
    else:
        n = len(f) + 1 
        xdatas = np.zeros([n,m])
        xdatas[0] = np.ones(m)
        for i in range(1, n):
            # TODO   
            xdatas[i] = f[i-1] (xdata)

    # 装配矩阵 A 
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            A[i][j] = np.dot(xdatas[n-1-i],xdatas[n-1-j])

    # 装配右端向量 b
    b = np.zeros(n)
    for i in range(n):
        b[i] = np.dot(xdatas[n-1-i],ydata)

    # 解方程组
    a = np.linalg.solve(A, b)
    return a

# 调用

if __name__ == "__main__":
    xdata = np.array([0.000, 0.895, 1.641, 2.512, 3.542, 4.054, 4.602, 5.063, 5.354, 5.617])
    ydata = np.array([1.000, 1.803, 3.680, 7.320, 13.59, 17.41, 22.19, 24.89, 26.55, 29.77])
    m = len(ydata)
    
    def f0(x):
        return x
    def f1(x):
        return np.cos(x) 
    def f2(x):
        return np.sin(x)
    def f3(x):
        return np.cos(2*x) 
    def f4(x):
        return np.sin(2*x)
    def f5(x):
        return np.cos(3*x) 
    def f6(x):
        return np.sin(3*x)
    def f7(x):
        return np.cos(4*x) 
    def f8(x):
        return np.sin(4*x)
    # 累加到sin(9*x) 
    def f9(x):
        return np.cos(5*x) 
    def f10(x):
        return np.sin(5*x)
    def f11(x):
        return np.cos(6*x) 
    def f12(x):
        return np.sin(6*x)
    def f13(x):
        return np.cos(7*x) 
    def f14(x):
        return np.sin(7*x)
    def f15(x):
        return np.cos(8*x) 
    def f16(x):
        return np.sin(8*x)
    def f17(x):
        return np.cos(9*x) 
    def f18(x):
        return np.sin(9*x)
    def f19(x):
        return np.cos(10*x) 
    def f20(x):
        return np.sin(10*x)

    a1 = polyfit(xdata, ydata, 2)  #polyfit返回值是次数从大到小的拟合多项式的系数.
    print(a1)

    f = [f0, f1, f2]
    a2 = polyfit(xdata,ydata,f)  #polyfit返回值是次数从大到小的拟合多项式的系数.
    print(a2)
    # [-1.90183422  2.68270259  4.90973928 -2.15461946]
    # -1.9f0 + 2.68f1 + 4.91f2 - 2.15
    # 画图
    x_draw = np.linspace(0, 6, 100)
    y_draw1 = polyval1(a1, x_draw)
    y_draw2 = polyval2(a2, x_draw, f)
    # 创建画布和子图
    fig, axs = plt.subplots(2, 1, figsize=(6, 6))

    # 在第一个子图中绘制数据
    axs[0].plot(x_draw, y_draw1, 'b-')
    axs[0].plot(xdata, ydata, 'ro')
    # 在第二个子图中绘制拟合曲线
    axs[1].plot(x_draw, y_draw2, 'b-')
    axs[1].plot(xdata, ydata, 'ro')
    # 添加图例
    # axs[0].legend()
    # axs[1].legend()

    # 添加标题
    # axs[0].set_title('Original Data')
    # axs[1].set_title('Fitted Curve')
    # 保存图像
    plt.savefig('P7.2.png')
    # 显示图形
    plt.tight_layout()  # 自动调整子图布局
    plt.show()
