import locale
import tkinter  as tk
from tkinter import ttk
from tkcalendar import Calendar 
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'en_US')

root = tk.Tk()
root.geometry("600x420")  

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=3)

events = {
    '10/13/22': ['*Keemia testid \n \n *Pese nõud']
    
}

calendar=Calendar(root,selectmode='day',tooltipbackground='green', locale='en_US')
calendar.grid(row=0,column=0, sticky=tk.NSEW)

for date in events.keys():
    for task in events[date]:
        calendar.calevent_create(datetime.strptime(date, '%m/%d/%y'), task)

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=3)
frame.rowconfigure(1, weight=1)

frame.grid(row=0, column=1, sticky=tk.NSEW)

label = tk.Label(frame, bg='azure', width=20, height=20)
label.grid(row=0, column=0, sticky=tk.NSEW)

button = tk.Button(frame, text='Vaata', command=lambda: update(), height=2, width=10)
button.grid(row=1, column=0)

def update():
    key = calendar.get_date()
    label.config(text=events[key] if key in events else 'Ülesanded puuduvad')

root.mainloop()