#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# 为直方图准备数据
mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma * np.random.randn(10000)        # 使用随机数生成器创建两个正态分布变量
x2 = mu2 + sigma * np.random.randn(10000)

# 绘图
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(x1, bins=50, density=False, color='darkgreen')          # 创建概率分布图
n, bins, patches = ax1.hist(x2, bins=50, density=False, color='orange', alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histograms', fontsize=14, fontweight='bold')      # 为基础图添加一个居中的标题
ax1.set_title('Two Frequency Distributions')    # 为子图添加一个居中的标题，位于基础图标题下面
plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
plt.show()
