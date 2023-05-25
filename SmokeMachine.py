import random
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from helpers import *
class SmokeMachine:
    def __init__(self, axes, position, direction, intensity=0.5, initial_speed=4):
        self.position = position
        self.direction = direction
        self.intensity = intensity 
        self.axes = axes
        self.initial_speed = initial_speed
        self.smokes = []
        self.plotted = 0
        self.variableParam = ""

        if(direction==W or direction==E):
            self.variableParam = "y"
        elif( direction==N or direction==S):
            self.variableParam = "x"
        else:
            pass


    
    def generateSmokes(self,num):
        count=0
        while count<num:
            pos=[self.position[0],self.position[1]]
            if(self.variableParam=="x"):
                pos[0] = random.randint(0,150)
            else:
                pos[1] = random.randint(0,100)
            smoke = Smoke(position=pos,radius=1,intensity=1,color="#848884",movement_direction=reverseDirection(self.direction),speed=self.initial_speed)
            # smoke.plotSmoke(self.axes)
            self.smokes.append(smoke)
            count += 1
        # print(f"{num} new smokes, total: {len(self.smokes)}")

    def plotSmokes(self,num):
        
        i=0
       
        while i<num and self.plotted<len(self.smokes):
            # print(f"c:{self.plotted}, i:{i}")
            self.smokes[self.plotted].plotSmoke(self.axes)
            self.plotted += 1
            i += 1

    def moveSmokes(self):
        # if(self.smokes)
        print("move smoke")
        for i in range(self.plotted):
            if(self.smokes[i] != None):
                self.smokes[i].move()




class Smoke:
    def __init__(self, position, radius, intensity, color, movement_direction, speed):
        self.position = position
        self.radius = radius
        self.intensity = intensity
        self.color = color
        self.direction = movement_direction
        self.circle = None
        self.speed = speed

    def move(self,deviate=True):

        print(f"going-->{self.direction} {self.position}")

        self.position = movement(self.position,self.direction,self.speed)
        self.circle.center = ((self.position[0],self.position[1])) 
        if(self.position[0]>150 or self.position[0]<0 or self.position[1]>100 or self.position[1]<0):
            self.direction = reverseDirection(self.direction)
            print("limittt",self.direction)
        # self.direction = randomizeDirection(self.direction)
        
        # increase size and decrease intensity with time and movement
        
        if(self.intensity>0.01):
            self.intensity -= 0.01
            self.circle.set_alpha(self.intensity)
            # self.removeSmoke()
        self.radius += 0.1
        self.circle.set_radius(self.radius)

       

      

        
   

    def plotSmoke(self,axes):
        self.circle = plt.Circle(self.position,self.radius,color=self.color,alpha=self.intensity,linestyle=":")

        axes.add_patch(self.circle)

    def removeSmoke(self):
        self.circle.set_visible(False)
        self.circle.remove()


        