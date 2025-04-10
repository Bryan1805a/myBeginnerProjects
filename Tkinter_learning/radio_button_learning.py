import tkinter as tk

class LanguageSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Favorite Language")
        self.root.geometry("400x250")
        
        # Shared variable (StringVar or IntVar)
        self.choice = tk.StringVar(value="")
        
        # Title
        tk.Label(root, text="Choose your favorite language:", font=("Arial", 14)).pack(pady=10)
        
        # Radiobuttons
        tk.Radiobutton(root, text="Python", variable=self.choice, value="Python").pack(anchor="w", padx=20)
        tk.Radiobutton(root, text="Java", variable=self.choice, value="Java").pack(anchor="w", padx=20)
        tk.Radiobutton(root, text="JavaScript", variable=self.choice, value="JavaScript").pack(anchor="w", padx=20)
        
        # Submit button
        tk.Button(root, text="Submit", command=self.show_selection).pack(pady=10)
        
        # Output Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack()
        
    def show_selection(self):
        selected = self.choice.get()
        if selected:
            self.result_label.config(text=f"You selected: {selected}")
        else:
            self.result_label.config(text="Please select a language.")

root = tk.Tk()
app = LanguageSelector(root)
root.mainloop()