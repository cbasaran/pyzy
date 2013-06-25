
class IOPin:
    def __init__(self,name="unknown"):
        self.lingmap = dict()
        self.lingvec = list()
        self.min,self.max,self.coef = (-1.0,1.0,1.0)
        self.name = name

    def fuzzify(self, x):
        step = (self.max - self.min) / (self.size() - 1)
        a,b = (self.min - step, self.min + step)
        mf = list()
        x = min(max(self.min, x * self.coef), self.max)
        for i in range(self.size()):
            mf += [self.certainty(x, a, b)]
            a,b = a + step, b + step
        return mf

    def certainty(self, x, a, b):
        m,p = 2.0 * (1.0 / (b - a)), (a + b) / 2.0
        if x <= a or x >= b: return 0
        return m * ( (x - a) if (x < p) else (b - x))

    def area_of(self, h):
        return self.width() * h * (1.0 - h / 2.0) / 2.0

    def center(self, i):
        return self.min + i * self.width()

    def width(self):
        if self.size() == 1: raise "Div0"
        return (self.max-self.min) / (self.size() - 1)

    def makeling(self):
        self.lingmap = { l : i for (i,l) in enumerate(self.lingvec) }

    def pushling(self, l):
        self.lingvec += [l]
    
    def size(self): return len(self.lingvec)

    def __repr__(self):
        return "pin %4s: [ %20s ] min %6.2f max %6.2f coef %6.2f" % (self.name, 
                ",".join(self.lingvec), self.min, self.max, self.coef)
