import matplotlib.pyplot as plt
import numpy as np
import randomcolor
from Light import Light

class LightSection:
    
    def __init__(self,axes,num_lights,light_radius):
        self.num_lights = num_lights
        self.light_radius = light_radius
        self.axes = axes
        #Set axes' sizes, from 0 151 with interval of 10
        x_ticks=np.arange(0, 151, 20)
        y_ticks=np.arange(0, 5, 4)
        self.axes.set_xlim(0,150)
        self.axes.set_xlim(0,4)
        self.axes.set_xticks(x_ticks)
        self.axes.set_yticks(y_ticks)

        self.lights = []  # Store the lights in a list

        #add lights
        self.addLights()
        self.plotLights()

    def addLights(self):
        for i in range(self.num_lights):
            x=i*10+10
            y= 5 
            # x=i*self.light_radius*2+self.light_radius*2
            # y = self.light_radius  
            randColor = randomcolor.RandomColor().generate()[0]
            intensity = round( np.random.uniform(0.5,1) ,2)
            light = Light([x,y],"down",randColor,self.light_radius, intensity)
            # light.plotLight(self.axes)
            self.lights.append(light)

        # print(self.lights)


    def plotLights(self):
        for light in self.lights:
            # light.setAttribute("intensity", np.random.uniform(0.01,1))
            # light.setAttribute("color", randomcolor.RandomColor().generate()[0])
           
            light.plotLight(self.axes)


    def shiftColors(self):
        prev =  self.lights[-1].color
        for light in self.lights:
            temp = light.color
            light.setAttribute("color",prev)
            print(temp,prev)
            prev=temp
            light.plotLight(self.axes)
            

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
 

    