import tkinter as tk

class HobbiesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Choose your hobbies")
        self.root.geometry("400x300")
        
        # Tiltle label
        tk.Label(root, text="Select your hobbies", font=("Arial", 14)).pack(pady=10)
        
        # Variables for each checkbox
        self.music_var = tk.BooleanVar()
        self.reading_var = tk.BooleanVar()
        self.travel_var = tk.BooleanVar()
        
        # CheckButtons
        tk.Checkbutton(root, text="Music", variable=self.music_var).pack(anchor='w', padx=20)
        tk.Checkbutton(root, text="Reading", variable=self.reading_var).pack(anchor='w', padx=20)
        tk.Checkbutton(root, text="Travel", variable=self.travel_var).pack(anchor='w', padx=20)
        
        # Button to show selected
        tk.Button(root, text="Submit", command=self.show_selected).pack(pady=15)
        
        # Button to clear all selected
        tk.Button(root, text="Clear all", command=self.clear_selected).pack(pady=10)
        
        # Label to display result
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack()
        
    def show_selected(self):
        hobbies = []
        if self.music_var.get():
            hobbies.append("Music")
        if self.reading_var.get():
            hobbies.append("Reading")
        if self.travel_var.get():
            hobbies.append("Travel")
            
        if hobbies:
            self.result_label.config(text="You selected: " + ", ".join(hobbies))
        else:
            self.result_label.config(text="No hobbies selected.")
            
    def clear_selected(self):
        self.music_var.set(False)
        self.reading_var.set(False)
        self.travel_var.set(False)
        self.result_label.config(text="")

root = tk.Tk()
app = HobbiesApp(root)
root.mainloop()