from LightSection import LightSection
from AudienceSection import AudienceSection
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib.animation import FuncAnimation
from platform import system
import random




NUM_LIGHTS=14
LIGHT_RADIUS=4


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


      

    lightSection = LightSection(ax1,NUM_LIGHTS,LIGHT_RADIUS)
    audienceSection = AudienceSection(ax2)

    xs=[]
    ys=[]

    def animate(i):
        plt.cla()  #clears the axes before next frame
        if i>0 :
            lightSection.shiftColors()
        
        # plt.plot()

        xs.append(i+1)
        ys.append(random.randint(0,100))
        ax2.plot(xs,ys)
        # ax1.plot()
       
        print(i)
   
    try:
        anim = FuncAnimation(fig, animate, interval=200, frames=1000,  cache_frame_data=False)
        a=1
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print("Unable to perform Action",e)
  


    plt.show()

    # stage = Stage()






if __name__ == "__main__":
    main()
