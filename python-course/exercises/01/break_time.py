import time
import webbrowser

total_count = 3
break_count = 0

print("Break time program started on " + time.ctime())
while(break_count < total_count):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=rc2jsjnt-HY")
    break_count += 1
