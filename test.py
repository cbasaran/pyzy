from pyzy import config
import random

cfg = config.Config()
controllers, args = cfg.read('fuzzy.conf')

random.seed(2)

for i in range(20):
    print controllers['Utilization'].signal(random.random(), 0.1)

