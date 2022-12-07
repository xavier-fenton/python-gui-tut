import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps= []


def addApp():
  for widget in frame.winfo_children(): #deletes old widgets
    widget.destroy()
  
  filename= filedialog.askopenfilename(initialdir="/", title="Select a File", 
                                        filetypes=(("executables", "*.exe"), ("All files", "*.*")))
  apps.append(filename) #store to array
  print(filename)
  for app in apps:
    label =tk.Label(frame, text=app, bg="grey") #label them
    label.pack()

def runApps(): #executes app when run app button is clicked
  for app in apps:
    os.startfile(app)   

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp) # open file with command = addApp function

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps) #command = runs the runApps function

runApps.pack() #this adds the button to the apps

root.mainloop()