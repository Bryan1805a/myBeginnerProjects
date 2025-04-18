import tkinter as tk
from tkinter.messagebox import showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Window
        self.title("Temperature Coverter")
        self.geometry("350x80")
        
        # Label
        self.label = tk.Label(self, text="Fahrenheit")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        # Fahrenheit entry
        self.fahrenheit_var = tk.StringVar(value="")
        self.fahrenheit_entry = tk.Entry(self, textvariable=self.fahrenheit_var)
        self.fahrenheit_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Convert button
        self.convert_button = tk.Button(self, text="Covert",)
        self.convert_button["command"] = self.convert_button_clicked
        self.convert_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Result label
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=1, column=1)
        
    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9
        
    def convert_button_clicked(self):
        try:
            f = float(self.fahrenheit_var.get())
            c = self.fahrenheit_to_celsius(f)
            result = f"{f} Fahrenheit = {c:.2f} Celcius"
            self.result_label.config(text=result)
        except ValueError:
            showerror(title="Error", message=ValueError)
            
        

if __name__ == "__main__":
    app = App()
    app.mainloop()