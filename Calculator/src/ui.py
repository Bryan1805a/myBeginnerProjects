from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

class CalculatorUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.result_var = StringVar()
        
        self.label = Label(master, text="Enter calculation:")
        self.label.pack()
        
        self.entry = Entry(master, textvariable=self.result_var)
        self.entry.pack()
        
        self.calculator_button = Button(master, text="Calculate", command=self.calculate)
        self.calculator_button.pack()
        
        self.result_label = Label(master, text="")
        self.result_label.pack()
        
    def calculate(self):
        user_input = self.result_var.get()
        try:
            from logic.calculator import calculate_function
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid input format. Use: number operator number")
            number_1 = float(parts[0])
            operator = parts[1]
            number_2 = float(parts[2])
            
            result = calculate_function(number_1, number_2, operator)
            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
def main():
    root = Tk()
    calculate_ui = CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()