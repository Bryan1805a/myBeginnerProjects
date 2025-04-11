import tkinter as tk

class FullFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Profile App")
        self.root.geometry("500x450")
        self.root.configure(bg="#f2f2f2") # Light gray background
        
        self.font_title = ("Arial", 16, "bold")
        self.font_normal = ("Arial", 12)
        
        # Hobbies Section
        hobbies_frame = tk.LabelFrame(root, text="Select your hobbies", font=self.font_title, bg="#f2f2f2", padx=10, pady=10)
        hobbies_frame.pack(fill="x", padx=20, pady=10)
        
        self.music_var = tk.BooleanVar()
        self.reading_var = tk.BooleanVar()
        self.travel_var = tk.BooleanVar()
        
        # Checkbuttons
        tk.Checkbutton(hobbies_frame, text="Music", variable=self.music_var, font=self.font_normal, bg="#f2f2f2").pack(anchor="w")
        tk.Checkbutton(hobbies_frame, text="Reading", variable=self.reading_var, font=self.font_normal, bg="#f2f2f2").pack(anchor="w")
        tk.Checkbutton(hobbies_frame, text="Travel", variable=self.travel_var, font=self.font_normal, bg="#f2f2f2").pack(anchor="w")
        
        # Language Section
        language_frame = tk.LabelFrame(root, text="Favorite programming language", font=self.font_title, bg="#f2f2f2", padx=10, pady=10)
        language_frame.pack(fill="x", padx=20, pady=10)
        
        # Radiobutton
        self.language_var = tk.StringVar(value="")
        
        tk.Radiobutton(language_frame, text="Python", variable=self.language_var, value="Python", font=self.font_normal, bg="#f2f2f2").pack(anchor="w")
        tk.Radiobutton(language_frame, text="Java", variable=self.language_var, value="Java", font=self.font_normal, bg="#f2f2f2").pack(anchor="w")
        tk.Radiobutton(language_frame, text="JavaScript", variable=self.language_var, value="JavaScript", font=self.font_normal, bg="#f2f2f2").pack(anchor="w")
        
        # Buttons frame
        button_frame = tk.Frame(root, bg="#f2f2f2")
        button_frame.pack(pady=15)
        
        # Submit button
        submit_button = tk.Button(button_frame, text="Submit", command=self.submit, font=self.font_normal, bg="#4CAF50", fg="white", width=10)
        submit_button.grid(row=0, column=0, pady=10)
        
        # Reset button
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset, font=self.font_normal, bg="#f44336", fg="white", width=10)
        reset_button.grid(row=0, column=1, padx=10)
        
        # Output label
        self.result_label = tk.Label(root, text="", font=self.font_normal, bg="#f2f2f2", fg="blue")
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
            lang_text = "No language selected."
        else:
            lang_text = f"Favorite: {language}"
            
        if hobbies:
            hobbies_text = "Hobbies: " + ", ".join(hobbies)
        else:
            hobbies_text = "No hobbies selected."
        
        self.result_label.config(text=lang_text + "\n" + hobbies_text)
        
    def reset(self):
        self.music_var.set(False)
        self.reading_var.set(False)
        self.travel_var.set(False)
        self.language_var.set("")
        self.result_label.config(text="")

root = tk.Tk()
app = FullFormApp(root)
root.mainloop()