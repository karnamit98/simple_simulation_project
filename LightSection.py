import matplotlib.pyplot as plt
import numpy as np
import randomcolor
from Light import Light
from helpers import *

class LightSection:
    
    def __init__(self,axes):
        self.num_lights = NUM_LIGHTS
        self.light_radius = LIGHT_RADIUS
        self.axes = axes
        self.colors = COLORS
        

        self.lights = []  # Store the lights in a list

        #add lights
        self.addLights()
        self.plotLights()

       

    def addLights(self):
        c=0
        for i in range(self.num_lights):
            x=i*10+5
            y= 5 
            color = self.colors[c]
            intensity = round( np.random.uniform(0.5,1) ,2)
            light = Light([x,y],"down",color,self.light_radius, intensity)
            self.lights.append(light)
            c+=1



    def plotLights(self):
        for light in self.lights:
           light.plotLight(self.axes)


    def shiftColors(self):
        prev =  self.lights[-1].color
        for light in self.lights:
            temp = light.color
            light.setAttribute("color",prev)
            prev=temp
            # light.plotLight(self.axes)
            
        
    def translateLights(self,i):
        # i between 1 and 15 incl
        # prev =  self.lights[-1].position
        count = 1
        for light in self.lights:
            temp = light.position
            newX = temp[0]+1
            temp[0] = newX if newX<150 else 0
            light.setAttribute("position",temp)
            # print(count,i)
            if(count%3==0):
                light.setAttribute("intensity", 0.2)
            if(count%7==0):
                light.setAttribute("height",np.random.randint(4,9))
            
            count += 1
            

    def shiftLights(self):
        pass
        # for light in self.lights:    
        #     # light.setAttribute("intensity", np.random.uniform(0.01,1))  
        #     # light.setAttribute("color",randomcolor.RandomColor().generate()[0])  
        #     x=light.position[0]
        #     y=light.position[1]
        #     # x=i*10+10
        #     newX = (x+10) if x<140 else 10
        #     light.setAttribute("position",[newX,y])
        #     print(newX,x)
        #     light.plotLight(self.axes)

        # for i in range(self.lights.len()):
        #     nextPos = self.lights[-1].position


        # self.lights.insert(0,self.lights.pop())
        # for i in range(self.num_lights):
        #     x=i*10+10
        #     y= 5 
        #     self.lights[i].setAttribute("position",[x,y])
        # self.plotLights()
        # print(self.lights)
 

    