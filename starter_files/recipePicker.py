import tkinter as tk
from PIL import ImageTk

bg_colour = "#3d6466"

# initiallize app
root = tk.Tk()
root.title("Recipe Picker")

# Place app in the center of the screen
# root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

# Create frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
logo_widget.image = logo_img
logo_widget.pack()

tk.Label

# run app
root.mainloop()

# https://www.youtube.com/watch?v=5qOnzF7RsNA&list=WL&index=7&t=2236s
