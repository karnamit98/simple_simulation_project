
class Prop:
    def __init__(self, position, shape="circle", moving=False):
        self.position=position 
        self.shape=shape #circle, square, rectangle, triangle
        self.moving=moving  #true -> moving, false->stationary
