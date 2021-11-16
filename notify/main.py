from notifypy import Notify
import time


title = input('Enter the title  : ')
message = input('Enter the message  :  ')
timer = int(input('Enter the timer (in sec )  : '))
repeat = int(input('Enter the snooze(in sec)  : '))

def notify():
    notification = Notify()
    notification.title = title
    notification.message = message
#    notification.icon = ""
#    notification.audio = ""
    notification.send()
    time.sleep(repeat)


time.sleep(timer)
notify()

