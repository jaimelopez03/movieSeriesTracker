from tkinter import *
from PIL import Image, ImageTk
import glob
import os
import cv2

class MST():
    def __init__(self):
        super().__init__()
        self.mstWindow = Tk()
        self.mstWindow.title("Movies & Series Tracker")
        self.mstWindow.geometry("1920x1080") 

        exitIcon = PhotoImage(file = r".\Images Movie DB\iconExit.png")
        addIcon = PhotoImage(file = r".\Images Movie DB\iconAdd.png")
        deleteIcon = PhotoImage(file = r".\Images Movie DB\iconDelete.png")
        saveIcon = PhotoImage(file = r".\Images Movie DB\iconSave.png")
        img_dir = ".\Images Movie DB\Movies" 
        self.mstWindow.iconbitmap("./Images Movie DB/iconMovie.ico")

        exitIcon = exitIcon.subsample(10, 10)
        addIcon = addIcon.subsample(10, 10) 
        deleteIcon = deleteIcon.subsample(10, 10)
        saveIcon = saveIcon.subsample(10, 10)
        
        
        self.exitButton = Button(text="Exit", fg="black", bg="red", border="8", command=self.closeOSMC, 
                                 image=exitIcon, compound=LEFT).place(x=1820, y=30)
        self.addButton = Button(fg="black", bg="#00ff00", border="8", image=addIcon, 
                                compound=LEFT).place(x=10, y=30)
        self.deleteButton = Button(fg="black", bg="#ff9900", border="8", image=deleteIcon, 
                                compound=LEFT).place(x=100, y=30)
        self.saveButton = Button(fg="black", bg="#3399ff", border="8", image=saveIcon, 
                                compound=LEFT).place(x=200, y=30)
        
        # references = []                                             
        for (self.mstWindow_, dirs, files) in os.walk(img_dir):
            if files:
                for file in files:
                    path = os.path.join(img_dir, file)
                    image = Image.open(path)
                    image = image.resize((220, 350))
                    photo = ImageTk.PhotoImage(image)
                    # img_label = Button(self.mstWindow, image=photo)
                    # img_label.pack()
                    # references.append(photo)
                    height = 2 
                    width = 7
                    frameX = 10
                    frameY = 110
                    frame4Each = Frame(self.mstWindow, height=250, width=400)
                    for x in range(width):
                        movieButton = Button(frame4Each, fg="black", border="8", image=photo)
                        movieLabel = Label(frame4Each, text="Movie Name")
                        
                        for y in range(height):
                            frame4Each.place(x=frameX, y=frameY)
                            movieButton.grid(column=x, row=y, padx=16.5, pady=15) 
                            movieLabel.grid(column=x, row=y+1)
                        
                        
                    
                
        # Start the event loop.
        self.mstWindow.mainloop()

    def closeOSMC(self):
        self.mstWindow.destroy()

run = MST()
