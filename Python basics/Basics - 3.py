import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

print("--------------------------------------------------")

# Using Keyboard module in Python

import keyboard

# It writes the content to output
keyboard.write("\n'GEEKS FOR GEEKS'\n")
  
# it blocks until Shift is pressed 
keyboard.wait('Shift')

print("Unblocked")

print("--------------------------------------------------")

keyboard.add_hotkey('ctrl + shift + a', print, args =('you entered', 'hotkey'))
  
keyboard.wait('Tab')

print("--------------------------------------------------")

# records keys untill "Enter" is pressed
rk = keyboard.record(until ='Enter')
  
keyboard.play(rk, speed_factor = 1)






