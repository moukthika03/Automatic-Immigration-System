from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename

def open_file():
    global img
    img = askopenfilename(parent=root, initialdir="/", title='Please select a file')
	
def gui_client():
    img=""
    global root
    root = Tk()
    root.title('Bureau Of Immigration--India')
    root.geometry('1000x600')
    root.configure(background='black')
    text = Text(width = 55, height=4, font=("Ariel", 30),background="gray")
    text.insert(INSERT, "Welcome to automatic immigration system! Please scan passport:-")
    text.pack()
    btn = Button(root, text ='Open', command = lambda:open_file())
    btn.pack(side = TOP, pady = 10)
    Button(root, text="Choose", command=root.destroy).pack()
    mainloop()
    #return 


