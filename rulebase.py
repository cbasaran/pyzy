
class Rulebase:

    def __init__(self):
        return

    #def resize(self, x, y):
    #    self.rulebase = [ [0] * x ] * y
    #    self.size = {'I1':x, 'I2':y }

    def rule(self, i, j):
        return self.rulebase[j][i]

    def set(self, i, j, l):
        self.rulebase[j][i] = l

    def __repr__(self):
        return "\n".join ( [ ",".join(x) for x in self.rulebase ])
