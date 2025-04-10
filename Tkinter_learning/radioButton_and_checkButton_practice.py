import tkinter as tk

class HobbyAndLanguageForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection App")
        self.root.geometry("900x600")
        
        # Create label for choosing Hobby
        tk.Label(root, text="Choose your hobbies:", font=("Arial", 13)).pack(pady=10)
        
        # Variables for hobbies
        self.music_var = tk.BooleanVar()
        self.reading_var = tk.BooleanVar()
        self.travel_var = tk.BooleanVar()
        
        # Create Checkbutton for hobbies
        tk.Checkbutton(root, text="Music", variable=self.music_var).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Reading", variable=self.reading_var).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Travel", variable=self.travel_var).pack(anchor="w", padx=20)
        
        # Label for choosing language (Radiobuttons)
        tk.Label(root, text="Choose your favorite language:", font=("Arial", 13)).pack(pady=10)
        
        # Variables for choosing language
        self.language_var = tk.StringVar(value="")
        
        # Radiobutton
        tk.Radiobutton(root, text="Python", variable=self.language_var, value="Python").pack(anchor="w", padx=10)
        tk.Radiobutton(root, text="Java", variable=self.language_var, value="Java").pack(anchor="w", padx=10)
        tk.Radiobutton(root, text="JavaScript", variable=self.language_var, value="JavaScript").pack(anchor="w", padx=10)
        
        # Submit button
        tk.Button(root, text="Submit", command=self.submit).pack(pady=10)
        tk.Button(root, text="Reset all", command= self.reset_form).pack(pady=5)
        
        # Output label
        self.result_label = tk.Label(root, text="", font=("Arial", 13))
        self.result_label.pack(pady=10)
        
    def submit(self):
        hobbies = []
        if self.music_var.get():
            hobbies.append("Music")
        if self.reading_var.get():
            hobbies.append("Reading")
        if self.travel_var.get():
            hobbies.append("Travel")
        
        language = self.language_var.get()
        
        if not language:
            lang_text = "No language selected"
        else:
            lang_text = f"Favorite Language: {language}"
            
        if hobbies:
            hobby_text = "Hobbies: " + ", ".join(hobbies)
        else:
            hobby_text = "No hobbies selected."
            
        self.result_label.config(text=hobby_text + "\n" + lang_text)
        
    def reset_form(self):
        self.music_var.set(False)
        self.reading_var.set(False)
        self.travel_var.set(False)
        self.language_var.set("")
        self.result_label.config(text="")

root = tk.Tk()
app = HobbyAndLanguageForm(root)
root.mainloop()