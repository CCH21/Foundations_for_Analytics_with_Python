#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# 为箱线图准备数据
N = 500
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
index_value = np.random.random_integers(low=0, high=N-1, size=N)
normal_sample = normal[index_value]
lognormal_sample = lognormal[index_value]
box_plot_data = [normal, normal_sample, lognormal, lognormal_sample]

# 绘图
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
box_labels = ['normal', 'normal_sample', 'lognormal', 'lognormal_sample']       # 保存每个箱线图的标签
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True,
            labels=box_labels)          # 创建4个箱线图
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box Plots: Resampling of Two Distributions')
plt.xlabel('Distribution')
plt.ylabel('Value')
plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
plt.show()
