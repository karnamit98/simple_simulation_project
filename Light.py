import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Light:
    def __init__(self, position,direction, color="red", radius=5,intensity=0.1 ):
        self.position = position
        self.color = color
        self.radius = radius 
        self.intensity = intensity #0-11
        self.direction = direction
        self.circle = None
        self.height = 10

       

    # Returns the Light object as a dictionary
    def get(self):
        return {"position":self.position,"direction":self.direction,"color":self.color,"radius":self.radius,"intensity":self.intensity}
    
    # Plots the circle patch to the given axes
    def plotLight(self,axes):
        # Remove the old circles from figure
        if(self.circle != None):
            self.circle.set_visible(False)
            self.circle.remove()
        self.circle = patches.Circle(self.position,self.radius,color=self.color,alpha=self.intensity,ls=":",lw=5)
        self.circle.set_height(self.height)
        axes.add_patch(self.circle)
        

    def setAttribute(self,key,value):
        if key=="color":
            self.color = value 
            self.circle.set_color(value)
        elif key=="intensity":
            self.intensity== value
            self.circle.set_alpha(value)
        elif key=="position":
            self.position== value
            self.circle.center = ((value[0],value[1]))
        elif key=="height":
            # self.height == np.random.randint(4,10)
            self.circle.set_height(self.height)
        else:
            pass

    
        
    # def 
