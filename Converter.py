# Import modules
from tkinter import * 
from tkinter import ttk 

# Create the root window
root=Tk()
root.title('Decimal To Binary')
root.geometry('500x250')
root.minsize('500','250')

decimal_value = IntVar()

#Define the Result function
def result():
    """ Hundel the Binary Result"""
    value=decimal_value.get()
    # Unsig instruction
    # res=value%2
    # while value // 2 !=0:
    #     value=value // 2
    #     res=str(res)+str(value%2)

    # using built-in function
    binary_result = bin(value)[2:]  # Use Python's built-in bin function for conversion
    result_label.config(text=f'{decimal_value.get()} Decimal To Binary Is: {binary_result}')

# Main App Content
title=Label(root, text='Decimal To Binary', font=('Arial', 15, 'bold'), fg='#444444')
title.grid(row=0, padx=150, pady=(5,20))


label=Label(root, text='Enter A Decimal Value: ')
label.grid()

entry=Entry(root, textvariable=decimal_value, width=30, 
            font=('Source Sans Pro'+ 'sans-serif', 10, 'bold'),
            fg='#444444')
entry.grid(pady=(5,10))

# Entry Validation to allow only integer inputs
validate_input = root.register(lambda s: s.isdigit())
entry.config(validate="key", validatecommand=(validate_input, '%S'))

# Show the final result in a label
result_label=Label(root, text='',
            font=('Source Sans Pro'+ 'sans-serif', 12, 'bold'),
            fg='#444444',)
result_label.grid(row=5, pady=(10,10))

btn=Button(root, text='Convert', 
           bg='#04AA6D',
           fg='#ffffff',
           border=0,
           width=10,
           font=('Source Sans Pro'+ 'sans-serif', 12, 'bold'),
           command=result)
btn.grid(pady=(15,10))




root.mainloop()