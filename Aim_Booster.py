
import Tkinter

root = Tkinter.Tk()
root.wm_title('Color-Shape Art Creation')

canvas = Tkinter.Canvas(root, height=300, width=300, background='#FFFFFF')
canvas.grid(row=0, column=1, rowspan=3)

root.mainloop()
