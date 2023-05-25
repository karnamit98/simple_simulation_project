import numpy as np
import matplotlib.pyplot as plt
import randomcolor
import random
from Prop import Prop 
from helpers import *


class StageSection:
    def __init__(self,axes,limits=[0,0]):
        self.num_lights = NUM_LIGHTS
        self.axes = axes
        self.colors = COLORS
        self.limits = limits

        self.light_rays=[]
        #add light rays
        self.addLightRays()
        self.plotLightRays()

        self.props= []
        self.addProps()

       
    def addProps(self):
        num=10 #random.randint(5,20)
        for i in range(num):
            prop = Prop(self.limits)
    
        
    def addLightRays(self):
        c=0
        for i in range(self.num_lights):
            # center of light source circle
            x=i*10+5
            y= 5 
            points = [[x-10,-1*y], [x,y+100],[x+10,-1*y] ]
            color = self.colors[c]
            # intensity = round( np.random.uniform(0.5,1) ,2)
            light_ray = LightRay(points=points,direction="down",color=color)
            self.light_rays.append(light_ray)
            c+=1
    
    def plotLightRays(self):
        for light_ray in self.light_rays:
           light_ray.plotLightRay(self.axes)


 
    def translateLightRays(self,i):
        # prev =  self.light_rays[-1].points
        count=1
        for light_ray in self.light_rays:
            temp = light_ray.points
            newX1 = temp[1][0]+1
            nexX0 = temp[0][0]+1
            newX2 = temp[2][0]+1
            temp[1][0] = newX1 if newX1<150 else 0
            temp[0][0] =  nexX0 if newX1<150 else -10
            temp[2][0] =  newX2 if newX1<150 else 10
          
            if(count%3==0):
                light_ray.setAttribute("intensity", 0.3)
            light_ray.setAttribute("points",temp)

            count += 1
            
        
 
    
class LightRay:
    def __init__(self,points, direction, color="#1089ff",intensity=1):
        self.points = points  #3x2 array of ints
        self.direction=direction #flat side facing directions
        self.color = color 
        self.intensity = intensity 
        self.polygon = None
        
    def get(self):
        return {"points":self.points, "direction":self.direction, "color":self.color}
    
    def plotLightRay(self,axes):
        # Remove the old polygon from figure
        if(self.polygon != None):
            self.polygon.set_visible(False)
            self.polygon.remove()
        self.polygon = plt.Polygon(self.points,facecolor=self.color,alpha=self.intensity,closed=False,edgecolor="white",ls="--",lw=2)
        axes.add_patch(self.polygon)

    
        
    def setAttribute(self,key,value):
        if key=="color":
            self.color = value 
            self.polygon.set_facecolor(value)
        elif key=="intensity":
            self.intensity== value
            self.polygon.set_alpha(value)
        elif key=="points":
            self.points == value
            self.polygon.set_xy(value)
        else:
            pass