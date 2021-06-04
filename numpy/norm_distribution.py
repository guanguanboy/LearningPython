import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(20201125)
size = 50000
x = np.random.randn(size)
print(type(x))
y1 = (np.sum(x<1)-np.sum(x<-1))/size
y2 = (np.sum(x<2)-np.sum(x<-2))/size
y3 =(np.sum(x<3)-np.sum(x<-3))/size
print(y1)
print(y2)
print(y3)

plt.hist(x, bins=200)
plt.show()

y1 = stats.norm.cdf(1) - stats.norm.cdf(-1)
y2 = stats.norm.cdf(2) - stats.norm.cdf(-2)
y3 = stats.norm.cdf(3) - stats.norm.cdf(-3)

print(y1)
print(y2)
print(y3)

# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 数据
mu = 100  # 均值
sigma = 20  # 方差
# 2000个数据
x1 = mu + sigma*x


# 画图 bins:条形的个数， normed：是否标准化
#plt.hist(x=x1, bins=200)


# 展示
#plt.show()