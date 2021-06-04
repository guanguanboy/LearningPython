# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

s = np.random.uniform(0, 1, 12000)  # 产生1200个[0,1)的数
#count, bins, ignored = plt.hist(s, 12, normed=True)
count, bins, ignored = plt.hist(s, 12)

print('count:', count)
print('bins:', bins)
print('np.ones_like(bins):', np.ones_like(bins))

"""
hist原型：
        matplotlib.pyplot.hist(x, bins=10, range=None, normed=False, weights=None,
        cumulative=False, bottom=None, histtype='bar', align='mid', 
        orientation='vertical',rwidth=None, log=False, color=None, label=None, 
        stacked=False, hold=None,data=None,**kwargs)
输入参数很多，具体查看matplotlib.org,本例中用到3个参数，分别表示：s数据源，bins=12表示bin 
的个数，即画多少条条状图，normed表示是否归一化，每条条状图y坐标为n/(len(x)`dbin),整个条状图积分值为1
输出：count表示数组，长度为bins，里面保存的是每个条状图的纵坐标值
     bins:数组，长度为bins+1,里面保存的是所有条状图的横坐标，即边缘位置
     ignored: patches，即附加参数，列表或列表的列表，本例中没有用到。
"""
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()