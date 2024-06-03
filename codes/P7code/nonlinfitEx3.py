import numpy as np
import matplotlib.pyplot as plt
import scipy
from pandas import read_csv  #需要安装pandas包读取csv文件

# 可添加其他你可能需要的包, 例如处理日期数据的包.

# 读取数据
d = read_csv('wuhan2020.csv')
df = d.values
print(df)

# TODO: 处理数据