import tkinter as tk
import tkinter.font as tkFont

# create tkinter object
app = tk.Tk()
# set app title
app.winfo_toplevel().title("System Thingy")
# set object's size
app.geometry("640x480")

# create font style to use in app
fontStyle = tkFont.Font(family = "Times New Roman", size = 18)

# create a label
labelExample = tk.Label(app, text = "The system is idle", font = fontStyle)

def normal():
    # change label text
    labelExample.config(text = "The system is idle")
    # change background - using configure
    app.configure(bg='gray')

def bgRed():
    # change background for bgRed call - using configure
    app.configure(bg='red')
    # change label text
    labelExample.config(text = "System Off")
    # call normal reset method after 2 seconds
    app.after(3400, normal)

def bgGreen():
    # change background for bgGreen call - using 'bg'
    app['bg'] = 'green'
    # change label text
    labelExample.config(text = "System Running")

# create a virtual image to be used for sizing the buttons in pixels instead of text units
pixelVirtual = tk.PhotoImage(width = 1, height = 1)

# put the label in the app using pack example (TOP, BOTTOM, LEFT, RIGHT)
labelExample.pack(side = tk.TOP)

# button example - what window, button text, background color, foreground color, use virtual
# image for sizing, width, height, compound="c" to show text
buttonExample1 = tk.Button(app, text="System On", bg="Green", fg="white", image=pixelVirtual, width=200, height=100, compound="c", command = bgGreen)
# use place to give the button a pixel location on screen
buttonExample1.place(x=400, y=100)

buttonExample2 = tk.Button(app, text="System Off", bg="Red", fg="white", image=pixelVirtual, width=200, height=100, compound="c", command = bgRed)
buttonExample2.place(x=400, y=340)

# minimal exit button and pack example (TOP, BOTTOM, LEFT, RIGHT)
buttonExample4 = tk.Button(app, text = "EXIT", command = app.quit)
buttonExample4.pack(side=tk.BOTTOM)

app.mainloop()