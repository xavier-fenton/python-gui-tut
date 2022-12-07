import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps= []

if os.path.isfile('save.txt'): # when adding files, then closing the app this saves the file as save.txt. Which then stores the files to the app. Each time the file is opened, it will show our saved apps. 
  with open('save.txt', 'r') as f:
    tempApps = f.read()
    tempApps = tempApps.split(',') #removes comma
    apps = [x for x in tempApps if x.strip()] #removes empty spaces


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


for app in apps:
  label = tk.Label(frame, text=app) #displays our applications from save.txt
  label.pack()


root.mainloop()

with open('save.txt', 'w') as f:
  for app in apps:
    f.write(app + ',')
    
    
    
    
# Challanges for myself:
# I could try write a way of just showing the app name. So we don't see the directory.