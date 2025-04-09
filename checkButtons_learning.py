import tkinter as tk

class CheckExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Checkbutton Example")
        self.root.geometry("300x200")
        
        self.var = tk.BooleanVar()
        
        self.check = tk.Checkbutton(root, text="I agree", variable=self.var, command=self.show_state)
        self.check.pack(pady=20)
        
        self.label = tk.Label(root, text="")
        self.label.pack()
        
    def show_state(self):
        if self.var.get():
            self.label.config(text="Checkbox is checked")
        else:
            self.label.config(text="Checkbox is unchecked")

root = tk.Tk()
app = CheckExample(root)
root.mainloop()