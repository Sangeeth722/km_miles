from tkinter import *

window = Tk()
window.minsize(width=200,height=100)
window.title("MILE TO KM CONVERTER")
window.config(padx=20,pady=20)
x = 0

def miles_km():
    if x == 0:
        miles = float(entry.get())
        km = miles * 1.6
        round_km = round(km ,2)

        km_label_output.config(text=f"{round_km}")
    else:
        km_2 = float(entry.get())
        miles_2 = km_2 / 1.609
        round_2 = round(miles_2,2)
        km_label_output.config(text=f"{round_2}")

def swap_button():
    #swap the km_label and miles_label

    global x
    x = 1

    km_label.grid(row=0,column=2)
    miles_label.grid(row=1,column=2)





#Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
#label.config(padx=30,pady=50)

miles_label =Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

km_label_output = Label()
km_label_output.grid(row=1, column=1)


entry = Entry(width=10)
entry.grid(row=0,column=1)

#button
button = Button(text="Calculate",command=miles_km)
button.grid(row=2,column=1)

swap_button = Button(text="swap",command=swap_button)
swap_button.grid(row=2,column=2)


window.mainloop()