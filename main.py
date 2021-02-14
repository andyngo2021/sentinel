import tkinter as tk 
from tkinter import ttk 
from tkinter import simpledialog
from Sentinel import Sentinel
import sys
from tkinter import font as tkFont
import pyglet

# Load in the Poppins font
pyglet.font.add_file('Assets/Poppins-SemiBold.ttf')
POPPINS = ('Poppins SemiBold', 25)


# Holds a list of activities the user enters
activities = []

# Instantiate a tk object
root = tk.Tk()
root.title('Sentinel')
# Size of the window (wxh)
root.geometry('550x300')
# Set the icon
root.iconphoto(False, tk.PhotoImage(file='Assets/icon.png'))

# Custom style for background
s = ttk.Style()
s.configure('new.TFrame', background='#cae8e0')

# Create a bar to hold tabs in
tab_bar = ttk.Notebook(root)

# Main Tab - Start/Pause the reminders
main_tab = ttk.Frame(tab_bar, style='new.TFrame')
tab_bar.add(main_tab, text='Main Menu')

# Creates a thread that can be stopped/started
sentinel_thread = Sentinel(activities)
# Allows us to kill threads with the exit of the main program
sentinel_thread.daemon = True

# This method saves the current activities to a text file
def save_changes():
    try:
        with open('Assets/activities.txt', 'w+') as out:
            for activity in activities:
                out.write(activity + '\n')
    except:
        pass

# This method starts the Sentinel Thread, allowing toast notifications to appear in the background while the main Tk window runs
def start():
    if len(activities)==0:
        # Notify that they need to add activities
        tk.messagebox.showwarning(title='NOT ENOUGH ACTIVITIES', message='Please add at least one activity before starting Sentinel!')
        print('Insufficient amount of activities')
    else:
        sentinel_thread.start()

# This method is called when you press the X button :D
def on_closing():
    # Call on the method to write activities into a txt file
    save_changes()
    root.destroy()


start_btn = tk.Button(main_tab, text="START", command=start, padx=45, pady=30, bg='#71ff4d', font=POPPINS)
stop_btn = tk.Button(main_tab, text="EXIT", command=on_closing, padx=70, pady=30, bg='#ff584d', font=POPPINS)
start_btn.pack(side='left', padx=25)
stop_btn.pack(side='right', padx=25)


# Activities Tab - Add/Delete activities
activities_tab = ttk.Frame(tab_bar, style='new.TFrame')
tab_bar.add(activities_tab, text='Activities')

# Functions needed for Listbox buttons
def add_activity():
    activity_name = simpledialog.askstring("Add Activity", "What is the name of the activity?")
    activity_list.insert(tk.END, activity_name)
    activities.append(activity_name)

def delete_selected_activity():
    try:
        index = activity_list.curselection()
        activities.pop(index[0])
        activity_list.delete(index)
    except:
        tk.messagebox.showwarning(title='Error', message='Please select an activity to delete!')


content = tk.StringVar()
add_btn = tk.Button(activities_tab, text="Add Activity", command=add_activity, padx=60, pady=10, bg='#71ff4d', font=('Poppins SemiBold', 10))
del_btn = tk.Button(activities_tab, text="Delete Activity", command=delete_selected_activity, padx=60, pady=10, bg='#ff584d', font=('Poppins SemiBold', 10))
activity_list = tk.Listbox(activities_tab)
activity_list.pack(padx=15, pady=15, fill='x')
add_btn.pack(side='left', padx=15)
del_btn.pack(side='right', padx=15)

# Add the tab_bar object to root
tab_bar.pack(expand=1, fill='both')


def on_open():
    global activities
    # Read in the saved activities
    with open('Assets/activities.txt', 'r') as fin:
        for line in fin.readlines():
            activities.append(line.strip())
            activity_list.insert(tk.END, line.strip())


# Initialize buttons and stuff
on_open()
# Main loop that allows to the program to run
root.protocol('WM_DELETE_WINDOW', on_closing)
root.resizable(False, False)
root.mainloop()