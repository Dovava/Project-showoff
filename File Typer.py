import keyboard, time, tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()
filename = filedialog.askopenfilename()
filedata = open(filename,'r').readlines()
for i in range(5):
                print(5-i)
                time.sleep(1)
for i in range(0,len(filedata)):
                keyboard.write(filedata[i])
