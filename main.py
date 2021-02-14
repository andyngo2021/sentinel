import tkinter as tk 
from tkinter import ttk 
from tkinter import simpledialog
from Sentinel import Sentinel
import sys

activities = []

root = tk.Tk()
root.title('Sentinel')
root.geometry('500x300')

# Create a bar to hold tabs in
tab_bar = ttk.Notebook(root)

# Main Tab - Start/Pause the reminders
main_tab = ttk.Frame(tab_bar)
tab_bar.add(main_tab, text='Main Menu')


sentinel_thread = Sentinel(activities)
# Allows us to kill threads with the exit of the main program
sentinel_thread.daemon = True

def save_changes():
    # This method saves the current activities to a text file
    with open('activities.txt', 'w+') as out:
        for activity in activities:
            out.write(activity + '\n')
    

def start():
    sentinel_thread.start()

def stop():
    save_changes()
    sys.exit()

start_btn = tk.Button(main_tab, text="Start", command=start)
stop_btn = tk.Button(main_tab, text="Exit", command=stop)
start_btn.pack()
stop_btn.pack()
# Activities Tab - Add/Delete activities
activities_tab = ttk.Frame(tab_bar)
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
        pass



content = tk.StringVar()
add_btn = tk.Button(activities_tab, text="Add Activity", command=add_activity)
del_btn = tk.Button(activities_tab, text="Delete Activity", command=delete_selected_activity)
activity_list = tk.Listbox(activities_tab)
activity_list.pack(padx=15, pady=15, fill='x')
add_btn.pack()
del_btn.pack()


# Settings Tab - Control the frequency, etc.
settings_tab = ttk.Frame(tab_bar)
tab_bar.add(settings_tab, text='Settings')

def enable_on_startup(value):
    state = value.get()
    if state:
        # Then make THIS python file execute on system start up
        pass
    else:
        # Then DONT' have it start on startup
        pass

start_up = tk.IntVar()
startup_btn = tk.Checkbutton(settings_tab, text=' Automatically start on startup', variable=start_up, onvalue=1, offvalue=0, command=lambda:enable_on_startup(start_up))
# startup_btn.pack()


# Add the tab_bar object to root
tab_bar.pack(expand=1, fill='both')


def on_open():
    # Read in the saved activities
    with open('activities.txt', 'r') as fin:
        for line in fin.readlines():
            activities.append(line.strip())
            activity_list.insert(tk.END, line.strip())
    # Read in previous button state for startup
    with open('startup.txt', 'r') as fin:
        global start_up
        try:
            num = int(fin.readline().strip())
            start_up.set(num)
        except:
            pass

def on_closing():
    # Call on the method to write activities into a txt file
    save_changes()
    # Write the current button state into the text file
    with open('startup.txt', 'w+') as fout:
        fout.write(str(start_up.get()))
    root.destroy()



# Initialize buttons and stuff
on_open()
# Main loop that allows to the program to run
root.protocol('WM_DELETE_WINDOW', on_closing)
root.mainloop()