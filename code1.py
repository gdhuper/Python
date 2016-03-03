import time
import webbrowser

total_breaks = 2
break_count = 0

print("Time program started on: " + time.ctime())
while(break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("google.com")
    break_count = break_count + 1

