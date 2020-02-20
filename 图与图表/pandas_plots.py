#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# 准备数据
fig, axes = plt.subplots(nrows=1, ncols=2)      # 创建两个并排放置的子图
ax1, ax2 = axes.ravel()                         # 将两个子图分别赋给变量ax1和ax2
data_frame = pd.DataFrame(np.random.rand(5, 3),
                          index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'],
                          columns=pd.Index(['Metric 1', 'Metric 2', 'Metric 3'], name='Metrics'))

# 绘制条形图
data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot')       # 创建条形图
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
ax1.set_xlabel('Customer')
ax1.set_ylabel('Value')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# 绘制箱线图
colors = dict(boxes='DarkBlue', whiskers='Gray', medians='Red', caps='Black')       # 为箱线图创建颜色字典
data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box Plot')       # 创建箱线图
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
ax2.set_xlabel('Metric')
ax2.set_ylabel('Value')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# 保存图片
plt.savefig('pandas_plots.png', dpi=400, bbox_inches='tight')
plt.show()
