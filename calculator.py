import tkinter as tk
from tkinter import messagebox # Import for error popups

# --- Core Logic (Mostly Unchanged) ---

def button_click(item):
    """Handles button clicks (numbers and operators)."""
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    """Clears the display and the current expression."""
    global expression
    expression = ""
    input_text.set("0")

def button_equal():
    """Evaluates the expression and displays the result."""
    global expression
    try:
        # Use str() and eval() for simple expression evaluation
        result = str(eval(expression))
        input_text.set(result)
        # Set expression to the result for continuous calculation
        expression = result
    except (ZeroDivisionError):
        input_text.set("Error: Div by Zero")
        messagebox.showerror("Calculation Error", "Cannot divide by zero.")
        expression = ""
    except (SyntaxError):
        input_text.set("Error")
        messagebox.showerror("Calculation Error", "Invalid input expression.")
        expression = ""
    except Exception as e:
        input_text.set("Error")
        messagebox.showerror("Calculation Error", f"An unexpected error occurred: {e}")
        expression = ""

# --- GUI Setup with Enhanced Styling ---

# 1. Initialize the main window
root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg='#282c34') # Dark background for a modern look
root.resizable(False, False) # Prevent window resizing

# Global variable to store the expression string
expression = ""

# StringVar to hold the text displayed in the input field
input_text = tk.StringVar()
input_text.set("0")

# --- Styling Configuration ---
FONT_DISPLAY = ('Arial', 32, 'bold')
FONT_BUTTON = ('Arial', 16)
COLOR_BACKGROUND = '#282c34'   # Dark Gray/Blue
COLOR_DISPLAY = '#FFFFFF'      # White
COLOR_NUM_BUTTONS = '#555A64'  # Medium Gray
COLOR_OP_BUTTONS = '#FF9500'   # Standard Orange
COLOR_SPECIAL_BUTTONS = '#4C4C4C' # Darker Gray (for C, =)

# 2. Create the display (Entry widget)
input_field = tk.Entry(
    root,
    font=FONT_DISPLAY,
    textvariable=input_text,
    bd=0, # Border width removed for a flat look
    bg=COLOR_BACKGROUND,
    fg=COLOR_DISPLAY,
    justify='right',
    insertwidth=0, # Remove the cursor insertion line
    highlightthickness=0 # Remove the default focus border
)
input_field.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)


# 3. Define the buttons and their colors
# (text, row, col, color_key, command_function)
buttons_config = [
    ('C', 1, 0, 'special', button_clear), ('/', 1, 3, 'operator', lambda: button_click('/')),
    ('7', 2, 0, 'number', lambda: button_click('7')), ('8', 2, 1, 'number', lambda: button_click('8')),
    ('9', 2, 2, 'number', lambda: button_click('9')), ('*', 2, 3, 'operator', lambda: button_click('*')),
    ('4', 3, 0, 'number', lambda: button_click('4')), ('5', 3, 1, 'number', lambda: button_click('5')),
    ('6', 3, 2, 'number', lambda: button_click('6')), ('-', 3, 3, 'operator', lambda: button_click('-')),
    ('1', 4, 0, 'number', lambda: button_click('1')), ('2', 4, 1, 'number', lambda: button_click('2')),
    ('3', 4, 2, 'number', lambda: button_click('3')), ('+', 4, 3, 'operator', lambda: button_click('+')),
    ('0', 5, 0, 'number', lambda: button_click('0')), ('.', 5, 1, 'number', lambda: button_click('.')),
    ('=', 5, 2, 'special', button_equal),
]

# 4. Create and place the button widgets in a loop
for (text, row, col, color_key, command) in buttons_config:
    # Determine background and foreground color based on the key
    if color_key == 'operator':
        bg_color = COLOR_OP_BUTTONS
        fg_color = 'white'
    elif color_key == 'special':
        bg_color = COLOR_SPECIAL_BUTTONS
        fg_color = 'white'
    else: # number
        bg_color = COLOR_NUM_BUTTONS
        fg_color = 'white'

    # Configure the button
    button = tk.Button(
        root, 
        text=text, 
        fg=fg_color, 
        bg=bg_color, 
        command=command, 
        height=2, 
        width=5, 
        font=FONT_BUTTON,
        relief='flat', # Use a flat look
        activebackground=bg_color, # Prevent color change when clicked
        activeforeground='light gray' # Slightly dim the text when clicked
    )
    
    # The '0' button spans two columns for a standard calculator layout
    if text == '0':
        button.grid(row=row, column=col, columnspan=2, sticky='nsew', padx=5, pady=5)
    # The '=' button should occupy the remaining space
    elif text == '=':
        button.grid(row=row, column=col, columnspan=2, sticky='nsew', padx=5, pady=5)
    else:
        button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

# 5. Configure row and column weights for expansion (Crucial for button size)
for i in range(1, 6): # Rows 1 to 5 (the button rows)
    root.grid_rowconfigure(i, weight=1)
for i in range(4): # Columns 0 to 3
    root.grid_columnconfigure(i, weight=1)

# 6. Start the main event loop
root.mainloop()