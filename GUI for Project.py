# GUI
# Cut down to gender, race/ethnicity, & education level for this
import tkinter as tk


window = tk.Tk()
window.title("Wage Gap Calculator")
window.geometry("1000x600") # width x height


from tkinter import*

# Gender Radio Button
canvas = tk.Canvas(window, width=200, height=50, bg='white')
canvas.pack()
canvas.create_text(100, 25, text="Enter gender:", font=("Arial", 15))
def show():
    lbl.config(text=f"Selected: {opt.get()}")
# Selected option variable  
opt = StringVar(value="Male")
# Radio buttons  
for lang in ["Male", "Female", "Non-binary", "Prefer not to say"]:
    Radiobutton(window, text=lang, variable=opt, value=lang).pack()

# Race/Ethnicity Listbox
canvas = tk.Canvas(window, width=200, height=50, bg='white')
canvas.pack()
canvas.create_text(100, 25, text="Enter race/ethnicity:", font=("Arial", 15))
def showrace():
    label.config(text=f"Selected: {listbox.get(ACTIVE)}")
# Should show be different for each box?  
racelistbox = Listbox(window)
for item in ["PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER"]:
    racelistbox.insert(END, item)
racelistbox.pack()
 
# Should likely save the chosen options as variables?

# Education Level Textbox
canvas = tk.Canvas(window, width=100, height=50, bg='white')
canvas.pack()
canvas.create_text(50, 25, text="Enter age:", font=("Arial", 15))
def showeducation():
    label.config(text=f"Selected: {listbox.get(ACTIVE)}")
educationlistbox = Listbox(window)
for item in ["PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER"]:
    educationlistbox.insert(END, item)
educationlistbox.pack()


# See Statistics Button  
Button(window, text="See my statistics:", command=show).pack()
lbl = Label(window, text=" ")
lbl.pack()

# Probably pops open another tab to show the data

# Always put this at the end
window.mainloop()

