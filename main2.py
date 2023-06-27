from win10toast import ToastNotifier
import time

def show_noti(title, message):
    ToastNotifier().show_toast(title,message,duration=3)
while True:   
    show_noti("Please Drink Water Now!!","Remember to Drink Water! Dehydration can affect your productivity and focus. Take a break and quench your thirst.")
    time.sleep(900)
 