import numpy as np
import matplotlib.pyplot as plt

def optimize(f,df,x0,eta,eps=1e-8):
    #输入: f(x1,...,xn), df=[df1,...,dfn], 其中dfi是f关于xi的偏导数. 
    #返回值: 迭代的最后一步x. 
    #先判断输入是否合理
    n = len(x0)
    assert f.__code__.co_argcount == n, 'Dimension of input of f does not match x0'
    assert len(df) == n, 'Dimension of df does not match x0'
        
    #开始优化
    x = x0 
    #TODO: 补全梯度下降法的代码. 可自行调整eta的输入
    while True:
        gradient = np.array([dfi(*x) for dfi in df])
        x -= eta * gradient
        if np.linalg.norm(gradient) < eps:
            break
    return x

if __name__ == "__main__": 
    #一个简单的算例来验证optimize
    def f(x1,x2):
        return x1*x1+x2*x2
    def df1(x1,x2):        #改成(x1,x2,x3)应该需要报错
        return 2*x1
    def df2(x1,x2):
        return 2*x2
    x0 = np.array([0.5,0.5])   #设置初始值
    eta = 1e-4                 #可自行调整
    x = optimize(f,[df1,df2],x0,eta)
    print(x)