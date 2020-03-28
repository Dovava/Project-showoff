import os, pip, subprocess, tkinter
root= tkinter.Tk()
w = tkinter.Label(root, text="Welcome to my Tkinter powered Python libary installer.\n Please write the name of the libary.\n Then click the install or uninstall button.\n When you're done press the QUIT button to exit the Python shell.\n When it starts saying not responding don't worry!\n I does it when it struggles doing it.\n But never crashes unless you exit the app while it is not responding.\nDo not click a button while another button is processing because it results in double clicking")
w.pack()
canvas1 = tkinter.Canvas(root, width = 400, height = 280)
canvas1.pack()
print("This is the output prompt! We are ready")
entry = tkinter.Entry(root)
canvas1.create_window(200,260, window=entry)
root.title("Libary Installer 1.3")
def installlib():
                x1 = entry.get()
                text = "pip install "+str(x1)
                subprocess.call(text)
                print("Done")
def uninstalllib():
                x2= entry.get()
                text2 = "pip uninstall "+str(x2)
                subprocess.call(text2)
                print("Done")
if __name__ == '__main__':
                pass
else:
                print("Welcome to developer mode! Please use help()")
frame = tkinter.Frame(root)
frame.pack()
button = tkinter.Button(frame, text="Download lib", fg="green",command=installlib)
button3 = tkinter.Button(frame, text="Uninstall lib", fg="green",command=uninstalllib)
button2 = tkinter.Button(frame, text="QUIT", fg="red",command=quit)

button.pack()
button3.pack()
button2.pack()
canvas1.pack()
root.mainloop()
