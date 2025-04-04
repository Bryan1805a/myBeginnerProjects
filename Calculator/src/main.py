def main():
    import tkinter as tk
    from ui import CalculatorUI
    
    root = tk.Tk()
    root.title("Calculator")
    
    app = CalculatorUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()