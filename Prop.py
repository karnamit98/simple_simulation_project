import numpy as np
class Prop:
    def __init__(self,limits, type="", shape="circle", moving=False):
        self.limits=limits
        self.position=[np.random.randint(0,limits[0]),np.random.randint(0,limits[1])] 
        self.shape=shape #circle, square, rectangle, triangle
        self.moving=moving  #true -> moving, false->stationary

