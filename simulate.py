import simpy
import math


def temperature_curve(env):
    time = 0
    amplitute = 10
    frequency = 0.07
    offset = 15

    while True:
        extra_term = math.sin(2 * math.pi * frequency * time)
        temperature = offset + amplitute * extra_term
        yield env.timeout(1)
        time += 1
        print(f"Time: {time} hours, Temperature: {temperature:.2f}C")

def ph_curve(env):
    time = 0
    amplitute = 2
    frequency = 0.07
    offset = 7

    while True:
        extra_term = math.sin(2 * math.pi * frequency * time)
        ph = offset + amplitute * extra_term
        yield env.timeout(1)
        time += 1
        print(f"Time: {time} hours, Ph: {ph:.2f}C")
        with open("values.txt", "a") as f:
            f.write(f"{ph}\n")

env = simpy.Environment()
env.process(ph_curve(env))
env.run(until=24)
