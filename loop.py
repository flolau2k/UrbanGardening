from random import random
from time import sleep
import matplotlib.pyplot as plt
# import numpy as np
from myPID import myPID


pid = myPID(0.1, 100, -100, 0.5, 0, 0)

x = list(range(10))
ph = 7
ph_hist = [ph] * 10

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.set_xlim(0, 10)
ax.set_ylim(5, 9)
line1, = ax.plot(x, ph_hist, 'b-')

while (True):
    ph += random() * 2 - 1
    inc = pid.run(7, ph)
    act = " - "
    if inc > 0:
        act = "PH up"
    elif inc < 0:
        act = "PH down"
    print(f"ph = {ph:.2f}, act = {act}")
    ph += inc
    ph_hist.append(ph)
    if len(ph_hist) > 10:
        ph_hist.pop(0)
    line1.set_ydata(ph_hist)
    # ax.relim()
    # ax.autoscale_view()
    # fig.canvas.draw()
    fig.canvas.flush_events()
    sleep(0.5)
