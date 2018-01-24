import Tkinter as tk
import random


root = tk.Tk()
root.wm_title('Aim_Booster')

radius_intvar = tk.IntVar()
radius_intvar.set(50) #initialize radius
# center of circle
x = random.randint(40,560)
y = random.randint(40,560)

def radius_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    r = radius_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-r, y-r, x+r, y+r)
# Instantiate and place slider
radius_slider = tk.Scale(root, from_=10, to=40, variable=radius_intvar,    
                              label='Radius', command=radius_changed)
radius_slider.grid(row=1, column=0, sticky=tk.W)
# Create and place directions for the user
text = tk.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

canvas = tk.Canvas(root, height=600, width=600, background='#FFFFFF')
canvas.grid(row=0, column=1, rowspan=3)

r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
def start(event):
    def countdown(count):
        # change text in label      
        label['text'] = count
        if count > 0.0:
            # call countdown again after 10ms 
            root.after(1, countdown, count-1)
    countdown(random.randint(40,150))

    
            
    
label = tk.Label(root)
label.grid(row=2, column=0)



#countdown(random.randint(250,1000))
# root.after(0, countdown, 5)
root.bind('<space>', start)
#canvas.bind('ButtonPressed-1>', shoot)

root.mainloop()
