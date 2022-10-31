import os.path
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

calendar=Calendar(root,selectmode='day',tooltipbackground='green', locale='en_US')
calendar.grid(row=0,column=0, sticky=tk.NSEW)

events = {}

if os.path.exists('tasks.txt'):
    with open('tasks.txt') as file:
        lines = file.readlines()
        
        for line in lines:
            if not line:
                continue
            
            date, task = line.split(';')
            
            if not date or not task:
                continue
            
            if date not in events:
                events[date] = []
            
            events[date].append(task)
            calendar.calevent_create(datetime.strptime(date, '%m/%d/%y'), task)


action_frame = tk.Frame(root)
action_frame.columnconfigure(0, weight=1)
action_frame.rowconfigure(0, weight=3)
action_frame.rowconfigure(1, weight=1)
action_frame.grid(row=0, column=1, sticky=tk.NSEW)

label = tk.Label(action_frame, bg='azure', width=20, height=20)
label.grid(row=0, column=0, sticky=tk.NSEW)

entry = tk.Entry(action_frame, width=15, bd=3)
entry.grid(row=1, column=0)

button_frame = tk.Frame(action_frame)
button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.grid(row=2, column=0)

write_button = tk.Button(button_frame,text='Lisa', command=lambda: write_event(), height=2, width=10)
write_button.grid(row=0, column=0)

read_button = tk.Button(button_frame, text='Vaata', command=lambda: update(), height=2, width=10)
read_button.grid(row=0, column=1)

def write_event():
    task = entry.get()
    if not task:
        return
    
    key = calendar.get_date()
    
    if key not in events:
        events[key] = []

    events[key].append(task)
    calendar.calevent_create(datetime.strptime(key, '%m/%d/%y'), task)
    save_to_file(key, task)
    update()
    entry.delete(0, tk.END)


def update():
    key = calendar.get_date()
    label.config(text='\n\n'.join(events[key]) if key in events else 'Ülesanded puuduvad')


def save_to_file(date, task):
    with open('tasks.txt', 'a+') as file:
        file.write(f"{date};{task}\n")


root.mainloop()