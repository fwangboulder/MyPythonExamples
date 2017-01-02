#!/usr/bin/python
import time
import webbrowser
# by Fang Wang Jan 1 2017
#open a webbrowser every two hours
# repeat for five times
def takeABreak():
    start_time=time.ctime()
    print 'start time is ',start_time
    url="https://www.youtube.com/watch?v=8xg3vE8Ie_E"
    for i in range(5):
        time.sleep(2*3600)
        webbrowser.open(url)
        print 'played video at ', time.ctime()
takeABreak()

