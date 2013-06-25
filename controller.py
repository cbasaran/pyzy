import rulebase, iopin

class Controller:
    
    def __init__(self):
        self.name = 'unknown'
        self.rulebase = rulebase.Rulebase()
        self.in1,self.in2 = iopin.IOPin(), iopin.IOPin()
        self.out = iopin.IOPin()
        self.integral,self.integral_limit = False,0.0
        self.prev_signal = 0.0
        return

    def signal(self, i1, i2):
        prem = self.fetch_prem(self.in1.fuzzify(i1), self.in2.fuzzify(i2))
        s = self.defuzzify(prem) * self.out.coef
        if self.integral: s += self.prev_signal
        s = max(self.out.min, min(self.out.max, s))
        prev_signal = s
        return s

    def reset(self): return 

    def fetch_prem(self, mf1, mf2):
        prem = [[] for x in mf2 ]
        for j,v2 in enumerate(mf2):
            prem[j] = [ 0 for x in mf1 ]
            for i,v1 in enumerate(mf1):
                prem[j][i] = min(v1, v2)
        return prem

    def defuzzify(self, prem):
        num, den = 0.0, 0.0
        for j in range(self.in2.size()):
            for i in range(self.in1.size()):
                area = self.out.area_of(prem[j][i])
                num += area * self.out.center(
                        self.out.lingmap[self.rulebase.rule(i,j)])
                den += area
        return num / den

    def __str__(self):
        return 'Controller %s [\n%s\n%s\n%s\n%s\n]' % (
                self.name, self.in1, self.in2, self.out, 
                self.rulebase)

    def __repr__(self):
        return 'Controller %s [\n%s\n%s\n%s\n%s\n]' % (
                self.name, self.in1, self.in2, self.out, 
                self.rulebase)
