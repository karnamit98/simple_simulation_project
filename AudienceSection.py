import numpy as np
import matplotlib.pyplot as plt
import randomcolor

class AudienceSection:
    def __init__(self,axes):
        self.axes = axes
        x_ticks=np.arange(10, 151, 20)
        y_ticks=np.arange(0, 101, 10)
        self.axes.set_xlim(0,150)
        self.axes.set_ylim(0,101)
        self.axes.set_xticks(x_ticks)
        self.axes.set_yticks(y_ticks)
        # self.axes.set_aspect("equal")
        # self.axes.axis('equal')
        self.light_rays=[]
        # self.draw_triangles()
        
    def addLightRays(self):
        for i in range(self.num_lights):
            x=i*10+10
            y= 5 
            # x=i*self.light_radius*2+self.light_radius*2
            # y = self.light_radius  
            randColor = randomcolor.RandomColor().generate()[0]
            intensity = round( np.random.uniform(0.5,1) ,2)
            light = LightRays([x,y],"down",randColor,self.light_radius, intensity)
            # light.plotLight(self.axes)
            self.audience.addLightRay([x,y],randColor)
            self.lights.append(light)
        
    def addLightRay(self,sourcePosition,sourceColor):
        sX = sourcePosition[0]
        sY = sourcePosition[1]
        # x = [sX-3,sX,sX+3,sX-3]
        # y = [sY,sY+10,sY,sY]
        # print(x,y)
        # self.light_rays.append({"position":[x,y]})
        
        points = [[sX-3,sY], [sX,sY+100],[sX+3,sY] ]
        lr = LightRay(points=points,direction="down",color=sourceColor)
        self.light_rays.append(lr)
        
    # def plotRays(self):
    #     for lr in self.light_rays:
    #         # plt.plot(lr["position"][0],lr["position"][1])
    #         # print(lr)
        
    def draw_triangles(self):
        # n=3
        # t = np.arange(0,360+(360/(n)),360/(n))
        # x = 10*np.sin(np.radians(t))
        # y = 10*np.cos(np.radians(t))
        # self.plt.plot(x,y)
        # self.axesaxis('equal')
        #Arc Plot
        d=np.arange(start=0,stop=90,step=1)
        rad=np.deg2rad(d)
        r=10
        xc = r*np.cos(rad)
        yc = r*np.sin(rad)
        plt.plot(xc,yc,color="yellow")
        
    def shiftColors(self):
        for lr in self.light_rays:
             
            pass
    
    
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
        self.polygon = plt.Polygon(self.points,color=self.color,alpha=self.intensity,closed=False)
        axes.add_patch(self.polygon)
        
    def setAttribute(self,key,value):
        if key=="color":
            self.color = value 
        elif key=="intensity":
            self.intensity== value
        elif key=="points":
            self.points == value
        else:
            pass