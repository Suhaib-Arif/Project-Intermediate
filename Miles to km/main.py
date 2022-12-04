import tkinter as tk

def MILES_KM():
    
    converted=round(int(input.get()) * 1.609344,2)
    ret_value.config(text=converted)

window= tk.Tk()
window.title("Miles to KM Converter")
window.minsize(width=200,height=150)
window.config(padx=20,pady=20)


input=tk.Entry()
input.config(width=10)
input.grid(row=0,column=1)


miles=tk.Label()
miles.config(text="Miles")
miles.grid(row=0,column=2)

is_equal_to=tk.Label(text="is equal to")
is_equal_to.grid(row=1,column=0)

value=0
ret_value=tk.Label(text=f"{value}")
ret_value.grid(row=1,column=1)

KM=tk.Label(text="KM")
KM.grid(row=1,column=2)

calculate=tk.Button(text="Calculate",command=MILES_KM)
calculate.grid(row=2,column=1)



tk.Label()
window.mainloop()
