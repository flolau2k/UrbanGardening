# code from https://itzwieseltal.wordpress.com/2020/06/02/python-pid-regler/
class baseP:
    def __init__(self, lower_bound, upper_bound):
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def regulate(self, act):
        if act < self.lower_bound:
            return -1

        if act > self.upper_bound:
            return 1
