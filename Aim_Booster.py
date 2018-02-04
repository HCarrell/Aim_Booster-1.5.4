import Tkinter as tk
import random

root = tk.Tk()
root.wm_title('Aim_Booster')

radius_intvar = tk.IntVar()
radius_intvar.set(50)
#initialize radius
# center of circle

y = random.randint(40,680)
x = random.randint(40,1200)

def radius_changed(intval):
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


canvas = tk.Canvas(root, height=720, width=1240, background='#FFFFFF')
canvas.grid(row=0, column=1, rowspan=3)

r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#FFFFFF', fill='#FFFFFF')
global score_list
score_list =[]
high_score_list = []                           
def start(event):
    canvas.itemconfig(circle_item, outline='#000000', fill='#00FFFF')
    global interrupt
    interrupt = 0
    global score
    score = 0
    def countdown(count):
        # change text in label 
        global interrupt
        score = count
        label['text'] = count
        if interrupt == 0 and count > 0.0:
            # call countdown again after 10ms 
            root.after(1, countdown, count-1)
        if interrupt == 1:
            new_score = 100 - score
            editor.insert(tk.END, new_score)
            editor.see(tk.END)
            score_list.append(new_score)
            for score in score_list:
                if new_score < score:
                    high_score_list.append(new_score)
                    for high_score in high_score_list:
                        if new_score < high_score:
                            highest.insert(tk.END, new_score)
                            highest.see(tk.END)     
    countdown(100)

def interruption():
    global interrupt
    interrupt = 1
        
def position_changed():
    # Get data from model
    # Could do this: r = int(new_intval)
    x = random.randint(40,560)
    y = random.randint(40,560)
    r = radius_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-r, y-r, x+r, y+r)
    
def shoot(event):
    check = 0
    (x,y) = event.x, event.y
    event.x = x
    event.y = y
    [x1, y1, x2, y2] = canvas.coords(circle_item)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x < x2 and x > x1:
        check=check +1
    if y < y2 and y > y1:
        check=check +1
    if check == 2:
        canvas.itemconfig(circle_item, outline='#FFFFFF', fill='#FFFFFF')
        interruption()
        position_changed()
        
highest = tk.Text(root, height = 1, width=2)
highest.grid(column=3,row=0,rowspan=1)
editor = tk.Text(root, width=2)
editor.grid(column=3, row=1, rowspan=5)
     
label = tk.Label(root)
label.grid(row=2, column=0)

#countdown(random.randint(250,1000))
# root.after(0, countdown, 5)
canvas.bind('<ButtonPress-1>', shoot)
root.bind('<space>', start)

root.mainloop()