import tkinter as tk 
from tkinter import ttk 
from tkinter import simpledialog

activities = []

root = tk.Tk()
root.title('Sentinel')
root.geometry('500x300')

# Create a bar to hold tabs in
tab_bar = ttk.Notebook(root)

# Main Tab - Start/Pause the reminders
main_tab = ttk.Frame(tab_bar)
tab_bar.add(main_tab, text='Main Menu')

# Activities Tab - Add/Delete activities
activities_tab = ttk.Frame(tab_bar)
tab_bar.add(activities_tab, text='Activities')

# Functions needed for Listbox buttons
def add_activity():
    activity_name = simpledialog.askstring("Add Activity", "What is the name of the activity?")
    activity_list.insert(tk.END, activity_name)
    activities.append(activity_name)

def delete_selected_activity():
    index = activity_list.curselection()
    activities.pop(index[0])
    activity_list.delete(index)

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



# Add the tab_bar object to root
tab_bar.pack(expand=1, fill='both')

# Main loop that allows to the program to run
root.mainloop()