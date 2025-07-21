import tkinter as tk

def click(event):
    button_text = event.widget["text"]
    if button_text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(0, result)
        except:
            screen.delete(0, tk.END)
            screen.insert(0, "Error")
    elif button_text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, button_text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Input field
screen = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
screen.grid(row=0, column=0, columnspan=4)

# Button labels
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create buttons
for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font=("Arial", 18), padx=20, pady=20)
        btn.grid(row=i+1, column=j)
        btn.bind("<Button-1>", click)

# Run the app
root.mainloop()
