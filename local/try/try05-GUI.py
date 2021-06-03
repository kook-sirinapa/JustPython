import tkinter as tk
from typing import Text

def show_output():
    number= int(number_input.get())

    if number <= 0:
        output_label.configure(text='Invalid Number')
        return output_label


    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'
    
    output_label.configure(text=output)

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=600)

title_lable = tk.Label(master=window, text='Please enter a number more than 0')
title_lable.pack(pady=20)
 
number_input = tk.Entry(master=window, width=20)
number_input.pack(pady=10)

ok_button = tk.Button(master=window, text='OK',command=show_output, width=15, height=2)
ok_button.pack()

output_label= tk.Label(master=window)
output_label.pack(pady=20)


window.mainloop()