#!/usr/bin/env python3

import matplotlib.pyplot as plt

plt.style.use('ggplot')                     # 使用ggplot样式表来模拟ggplot2风格的图形

# 为条形图准备数据
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]

# 绘图
fig = plt.figure()                          # 创建了一个基础图
ax1 = fig.add_subplot(1, 1, 1)              # 在基础图中创建1行1列的子图，并使用第1个也是唯一的一个子图
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')    # 创建条形图
ax1.xaxis.set_ticks_position('bottom')      # x刻度线位置
ax1.yaxis.set_ticks_position('left')        # y刻度线位置
plt.xticks(customers_index, customers, rotation=0, fontsize='small')        # 将刻度线标签更改为实际的客户名称
plt.xlabel('Customer Name')                 # 添加x轴标签
plt.ylabel('Sale Amount')                   # 添加y轴标签
plt.title('Sale Amount per Customer')       # 添加图形标题
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')       # 保存统计图到当前文件夹
plt.show()
