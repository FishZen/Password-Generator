import tkinter as tk
from tkinter import ttk
import random
import string

win = tk.Tk()
win.title('Password Generator')
win.geometry('300x400')

#main
#function 
def generate_password():
    length = length_var.get()
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_numbers = number_var.get()
    include_symbols = symbols_var.get()
    #record down what the user had chosen (eg: length = 8, include_upper = true (if user check))
    
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!\"#$&\'()*+,-./?<=>@%^_`{|}[]~;'
    
    password = ''
    if include_upper or include_lower or include_numbers or include_symbols:
        for i in range(length):
            characters = ''
            if include_upper: #if user tick uppercase check button
                characters += uppercase
            if include_lower: 
                characters += lowercase
            if include_numbers: 
                characters += digits
            if include_symbols: 
                characters += symbols
            password += random.choice(characters) #randomize the characters
        result_var.set(password)
        error_var.set('')
    else:
        error_var.set('Select at least one character type!')

fstyle = 'Times New Roman'
PG = tk.Label(win, text = 'Password Generator', font = (fstyle, 15))
PG.pack()

length_label = tk.Label(win, text = 'Length: ', font = (fstyle, 14))
length_label.pack(pady = 5)

length_var = tk.IntVar()
#value = 5, write this in the bracket if you want it to have a default value
length_entry = tk.Entry(win, textvariable = length_var, font = (fstyle, 13))
length_entry.pack(pady = 5)

#check buttons
upper_var = tk.BooleanVar() #boolean -> True / False
lower_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

upper_cButton = tk.Checkbutton(win, text = 'ABC', variable = upper_var, font = (fstyle, 12))
upper_cButton.pack(pady = 5)
lower_cButton = tk.Checkbutton(win, text = 'abc', variable = lower_var, font = (fstyle, 12))
lower_cButton.pack(pady = 5)
number_cButton = tk.Checkbutton(win, text = '123', variable = number_var, font = (fstyle, 12))
number_cButton.pack(pady = 5)
symbols_cButton = tk.Checkbutton(win, text = '@!#$', variable = symbols_var, font = (fstyle, 12))
symbols_cButton.pack(pady = 5)

#button (generate password)
GP_Button = tk.Button(win, text = 'Generate Password', font = (fstyle, 13), 
command = generate_password)
GP_Button.pack(pady = 10)

#entry (to put the password)
result_var = tk.StringVar() #variable to store the generated password
result_entry = tk.Entry(win, textvariable = result_var, font = (fstyle, 12))
result_entry.pack(pady = 10)

error_var = tk.StringVar()
error_label = tk.Label(win, textvariable = error_var, font = (fstyle, 13))
error_label.pack(pady = 5)

win.mainloop()