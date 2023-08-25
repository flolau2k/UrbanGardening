
# code from https://itzwieseltal.wordpress.com/2020/06/02/python-pid-regler/
class myPID :
	def __init__(self, dt, max, min, kp, kd, ki) :
		self.dt  = dt
		self.max = max
		self.min = min
		self.kp  = kp
		self.kd  = kd
		self.ki  = ki
		self.err = 0
		self.int = 0
	def run(self,set,act):
		error = set - act

		P = self.kp * error

		self.int += error * self.dt
		I = self.ki * self.int

		D = self.kd * (error - self.err) / self.dt

		output = P + I + D

		if output > self.max :
			output = self.max
		elif output < self.min :
			output = self.min

		self.err = error
		return(output)
  
 
def main():
	pid = myPID(0.1, 100, -100, 0.1, 0.01, 0.5)
	val = 20
	for i in range(100) :
		inc = pid.run(0, val)
		print('val:','{:7.3f}'.format(val),' inc:','{:7.3f}'.format(inc))
		val += inc

if __name__ == "__main__":
	main()

# pid = myPID(0.1, 100, -100, 0.1, 0.01, 0.5)

# with open("values.txt", "r") as f:
# 	for line in f:
# 		inc = pid.run(7, float(line))
# 		print(f"output: {inc}\n")
	