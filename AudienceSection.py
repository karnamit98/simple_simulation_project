import numpy as np

class AudienceSection:
    def __init__(self,axes,):
        self.axes = axes
        x_ticks=np.arange(10, 151, 20)
        y_ticks=np.arange(0, 101, 10)
        self.axes.set_xlim(0,150)
        self.axes.set_ylim(0,101)
        self.axes.set_xticks(x_ticks)
        self.axes.set_yticks(y_ticks)
        # self.axes.set_aspect("equal")
        # self.axes.axis('equal')

    