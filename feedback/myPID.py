# code from https://itzwieseltal.wordpress.com/2020/06/02/python-pid-regler/
class myPID:
    def __init__(self, dt, max, min, kp, kd, ki):
        self.dt = dt
        self.max = max
        self.min = min
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.err = 0
        self.int = 0

    def run(self, set, act):
        error = set - act

        if error <= 1 and error >= -1:
            return 0

        P = self.kp * error
        self.int += error * self.dt
        I = self.ki * self.int
        D = self.kd * (error - self.err) / self.dt
        output = P + I + D
        if output > self.max:
            output = self.max
        elif output < self.min:
            output = self.min

        self.err = error
        return (output)
