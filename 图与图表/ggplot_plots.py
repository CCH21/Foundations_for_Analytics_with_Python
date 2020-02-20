#!/usr/bin/env python3

from ggplot import *

print(diamonds.head())
plt = ggplot(diamonds, aes(x='carat', y='price', colour='cut')) + \
      geom_point(alpha=0.5) + \
      scale_color_gradient(low='#05D9F6', high='#5011D1') + \
      xlim(0, 6) + ylim(0, 20000) + \
      xlab("Carat") + ylab("Price") + \
      ggtitle("Diamond Price by Carat and Cut") + \
      theme_gray()
print(plt)

ggplot.save(plt, "ggplot_plots.png", dpi=400)
