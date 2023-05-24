import matplotlib.pyplot as plt

class Light:
    def __init__(self, position,direction, color="red", radius=5,intensity=0.1 ):
        self.position = position
        self.color = color
        self.radius = radius 
        self.intensity = intensity #0-11
        self.direction = direction
        self.circle = None

    # Returns the Light object as a dictionary
    def get(self):
        return {"position":self.position,"direction":self.direction,"color":self.color,"radius":self.radius,"intensity":self.intensity}
    
    # Plots the circle patch to the given axes
    def plotLight(self,axes):
        # Remove the old circles from figure
        if(self.circle != None):
            self.circle.set_visible(False)
            self.circle.remove()
        self.circle = plt.Circle(self.position,self.radius,color=self.color,alpha=self.intensity)
        axes.add_patch(self.circle)
        

    def setAttribute(self,key,value):
        if key=="color":
            self.color = value 
        elif key=="intensity":
            self.intensity== value
        elif key=="position":
            self.position== value
        else:
            pass

    
        
    # def 
