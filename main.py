import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.title('Sentinel')
root.geometry('500x500')

# Create a bar to hold tabs in
tab_bar = ttk.Notebook(root)

# Main Tab - Start/Pause the reminders
main_tab = ttk.Frame(tab_bar)
tab_bar.add(main_tab, text='Main Menu')

# Activities Tab - Add/Delete activities
activities_tab = ttk.Frame(tab_bar)
tab_bar.add(activities_tab, text='Activities')
# Scrolling Frame 
scroll_frame = tk.LabelFrame(activities_tab)
inner_frame = tk.Canvas(scroll_frame)
inner_frame.pack(side='left', fill='both', expand='yes')

# Add a scrollbar and allow it to actually scroll through a frame
scrollbar = ttk.Scrollbar(scroll_frame, orient='vertical', command=inner_frame.yview)
scrollbar.pack(side='right', fill='y')
inner_frame.configure(yscrollcommand=scrollbar.set)
inner_frame.bind('<Configure>', lambda e: inner_frame.configure(scrollregion=inner_frame.bbox('all')))

# activities_frame is a Frame object we can any object we want to
activities_frame = tk.Frame(inner_frame)
activities_frame.pack()
inner_frame.create_window((0,0), window=activities_frame, anchor='nw')
scroll_frame.pack(fill='both', expand='yes', padx=10, pady=10)
 
# Add activites to the scrolling frame
for i in range(50):
    tk.Button(activities_frame, text='Button ' +  str(i)).pack()

# Bar that holds the save changes button
bottom_bar = tk.LabelFrame(activities_tab)
bottom_bar.pack(fill='both', expand='yes', padx=10, pady=10)
save_changes_btn = tk.Button(bottom_bar, text='Save Changes')
save_changes_btn.grid(row=0, column=0, padx=15, pady=15)


# Settings Tab - Control the frequency, etc.
settings_tab = ttk.Frame(tab_bar)
tab_bar.add(settings_tab, text='Settings')



# Add the tab_bar object to root
tab_bar.pack(expand=1, fill='both')

# Main loop that allows to the program to run
root.mainloop()