from tkinter import *

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

# Create Label in our window
image = PhotoImage(file="C:/Users/roeig/CodingFolder/python/next/unit6/025.jpg")
img = Label(root, image=image)
img.pack()
root.mainloop()