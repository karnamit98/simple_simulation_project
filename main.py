from LightSection import LightSection
from StageSection import StageSection
from SmokeMachine import SmokeMachine
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np
from matplotlib.animation import FuncAnimation
from platform import system
import random
from helpers import *
import itertools





# INTERVAL=10
# X_LIMIT=151
# LIGHTS_Y_LIMIT=15
# AUDIENCES_Y_LIMIT=101




def main():

    plt.style.use('dark_background') #dark_background #seaborn
    # plt.title("Spinal Tap", fontsize="18")
    fig, (ax1, ax2) = plt.subplots(nrows=2,ncols=1,sharex=True, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10,15))
    fig.tight_layout()
    ax1.set_autoscale_on(False)
    ax2.set_autoscale_on(False)
    pl.gcf().canvas.manager.set_window_title('Spinal Tap ')
    plt.subplots_adjust(left=0.029, bottom=0.25, right=0.775, top=0.962, wspace=0.171, hspace=0.011)




        # See discussion: https://stackoverflow.com/questions/12439588/how-to-maximize-a-plt-show-window-using-python
    # platform dependent maximizing of plot
    def plt_maximize():
        backend = plt.get_backend()
        cfm = plt.get_current_fig_manager()
        
        if backend == "wxAgg":
            cfm.frame.Maximize(True)
        elif backend == "TkAgg":
            if system() == "Windows":
                cfm.window.state("zoomed")  # This is windows only
            else:
                cfm.resize(*cfm.window.maxsize())
        elif backend == "QT4Agg":
            cfm.window.showMaximized()
        elif callable(getattr(cfm, "full_screen_toggle", None)):
            if not getattr(cfm, "flag_is_max", None):
                cfm.full_screen_toggle()
                cfm.flag_is_max = True
        else:
            raise RuntimeError("plt_maximize() is not implemented for current backend:", backend)

    plt_maximize()


      
    #Set light axes' sizes, from 0 151 with interval of 10
    x_ticks=np.arange(0, 151, 20)
    y_ticks=np.arange(0, 5, 4)
    ax1.set_xlim(0,150)
    ax1.set_xlim(0,4)
    ax1.set_xticks(x_ticks)
    ax1.set_yticks(y_ticks)
    lightSection = LightSection(ax1)
    x_ticks=np.arange(10, 151, 20)
    y_ticks=np.arange(0, 101, 10)
    ax2.set_xlim(0,150)
    ax2.set_ylim(0,100)
    ax2.set_xticks(x_ticks)
    ax2.set_yticks(y_ticks)
    stageSection = StageSection(ax2,limits=[150,100])
    

    smokeMachine1 = SmokeMachine(ax2, position=[0,0], direction=W)
    smokeMachine2 = SmokeMachine(ax2, position=[150,0], direction=E)
    smokeMachine3 = SmokeMachine(ax2, position=[0,0], direction=S)
    smokeMachine4 = SmokeMachine(ax2, position=[100,100], direction=N)
    
    smokeMachine1.generateSmokes(200)
    smokeMachine2.generateSmokes(200)
    smokeMachine3.generateSmokes(200)
    smokeMachine4.generateSmokes(200)
    smokeMachine1.plotSmokes(4)
    smokeMachine2.plotSmokes(4)
    smokeMachine3.plotSmokes(4)
    smokeMachine4.plotSmokes(4)

    def animate(i): 
        # plt.cla()  #clears the axes before next frame
        if i>1 :
            # lightSection.shiftColors()
            # stageSection.shiftColors()
            lightSection.translateLights(i)
            stageSection.translateLightRays(i)
        
        smokeMachine1.moveSmokes()
        smokeMachine2.moveSmokes()
        smokeMachine3.moveSmokes()
        smokeMachine4.moveSmokes()
        if i%17==0:
            # print("generating smokes")
            smokeMachine1.plotSmokes(2)
            smokeMachine2.plotSmokes(2)
            smokeMachine3.plotSmokes(2)
            smokeMachine4.plotSmokes(2)
        
       
        print(i)
   
    try:
        anim = FuncAnimation(fig, animate, interval=50,
                             frames=1000,
                            #   frames=np.arange(1, 16),  
                             cache_frame_data=False)
        a=1
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print("Unable to perform Action",e)
  

    # for i in range(1000):
    #     print(i)
    #     lightSection.translateLights(i)
    #     stageSection.translateLightRays(i)
    #     smokeMachine.moveSmoke()
    #     smokeMachine.generateSmokes(10)

    #     # break simulatiom
    #     # if a == 0:
    #     #     print("Simulation Ends!")
    #     #     break

    #     plt.pause(0.2)
    #     # plt.clf()



    plt.show()

    # stage = Stage()






if __name__ == "__main__":
    main()
