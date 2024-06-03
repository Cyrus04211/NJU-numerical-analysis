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
    i = 0
    epcho=[]
    loss=[] 
    #TODO: 补全梯度下降法的代码. 可自行调整eta的输入
    while True:
        epcho.append(i)
        loss.append(f(x[0],x[1]))
        gradient = np.array([dfi(*x) for dfi in df])
        x -= eta * gradient
        i += 1
        if np.linalg.norm(gradient) < eps:
            break
    plt.plot(epcho,loss,'b-')
    plt.savefig('P7.7.png')
    return x

xdata = np.array([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
ydata = np.array([0.04, 0.17, 0.65, 1.39, 1.85, 1.90, 1.99])
def f(a,b):
    return np.sum((2/(1+a*np.exp(b*xdata))-ydata)**2)/len(xdata)
def dfa(a,b):
    return np.sum(-4*(1/(1+a*np.exp(b*xdata))**2)*2*np.exp(b*xdata)*(2/(1+a*np.exp(b*xdata))-ydata))/len(xdata)
def dfb(a,b):
    return np.sum(-4*(1/(1+a*np.exp(b*xdata))**2)*np.exp(b*xdata)*a*2*xdata*(2/(1+a*np.exp(b*xdata))-ydata))/len(xdata)

if __name__ == "__main__": 
    # 线性化处理
    yt = np.log(2.0/ydata-1.0) 
    u = np.polyfit(xdata,yt,1) #u[0]x+u[1]
    b = u[0]
    c = u[1]
    a = np.exp(c)
    print(a,b)
    # 优化
    x0 = np.array([a,b])   #设置初始值
    eta = 1e-4                 #可自行调整
    a,b = optimize(f,[dfa,dfb],x0,eta)
    print(a,b)
    # 画图
    # xdraw = np.linspace(-1.5,1.5,100)
    # ydraw = 2.0/(1+a*np.exp(b*xdraw))
    # plt.plot(xdata,ydata, 'ro')
    # plt.plot(xdraw,ydraw, 'b')
    # plt.savefig('P7.6.png')
    # plt.show()