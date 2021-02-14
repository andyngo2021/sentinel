import threading
from win10toast import ToastNotifier
import time
import random

# This class is responsible for the toast notifications
class Sentinel(threading.Thread):
    
    def __init__(self, activities):
        threading.Thread.__init__(self)
        self.toaster = ToastNotifier()
        self.activities = activities
    
    def run(self):
        while True:
            self.toaster.show_toast('Time to take a break!', 'Either stand up look away from your screen for 20 seconds, or do this:\n' + random.choice(self.activities), icon_path='Assets/icon.ico', duration=10)
            time.sleep(1200) # Every 20 minutes
        
        while toaster.notification_active():
            time.sleep(0.1)
