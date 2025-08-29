import tkinter as tk
from math import sin, cos, tan, log, sqrt, pow, radians, degrees, e, pi

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        master.title("calculator")
        master.geometry("400x600")
        master.resizable(False, False)

        self.expression = ""

        self.entry_text = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.entry_text, font=('Arial', 20), bd=5, relief='sunken', justify='right')
        self.entry.pack(fill='both', ipadx=8, pady=10, padx=10)

        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'x^y'],
            ['1', '2', '3', '-', 'log'],
            ['0', '.', '=', '+', 'ln'],
            ['sin', 'cos', 'tan', '(', ')'],
            ['C', 'π', 'e', 'deg', 'rad']
        ]

        for row in buttons:
            frame = tk.Frame(master)
            frame.pack(expand=True, fill='both')
            for b in row:
                btn = tk.Button(frame, text=b, font=('Arial', 18), command=lambda x=b: self.click(x))
                btn.pack(side='left', expand=True, fill='both')

    def click(self, key):
        try:
            if key == "=":
                # Evaluate the expression safely
                expr = self.expression.replace('π', str(pi)).replace('e', str(e)).replace('^', '**')
                result = eval(expr)
                self.entry_text.set(str(result))
                self.expression = str(result)
            elif key == "C":
                self.expression = ""
                self.entry_text.set("")
            elif key == "sqrt":
                self.expression += "sqrt("
                self.entry_text.set(self.expression)
            elif key == "x^y":
                self.expression += "**"
                self.entry_text.set(self.expression)
            elif key == "log":
                self.expression += "log10("
                self.entry_text.set(self.expression)
            elif key == "ln":
                self.expression += "log("
                self.entry_text.set(self.expression)
            elif key == "sin":
                self.expression += "sin(radians("
                self.entry_text.set(self.expression)
            elif key == "cos":
                self.expression += "cos(radians("
                self.entry_text.set(self.expression)
            elif key == "tan":
                self.expression += "tan(radians("
                self.entry_text.set(self.expression)
            elif key == "deg":
                self.expression += "degrees("
                self.entry_text.set(self.expression)
            elif key == "rad":
                self.expression += "radians("
                self.entry_text.set(self.expression)
            else:
                self.expression += str(key)
                self.entry_text.set(self.expression)
        except Exception as e:
            self.entry_text.set("خطا")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = AdvancedCalculator(root)
    root.mainloop()
