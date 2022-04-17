import math
math.cos(math.pi / 4)
0.70710678118654757 #output
math.log(1024, 2)
10.0 #output

import random
random.choice(['apple', 'pear', 'banana'])
'apple' #output
random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33] #output
random.random()    # random float
0.17970987693706186 #output
random.randrange(6)    # random integer chosen from range(6)
4 #output

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
1.6071428571428572 #output
statistics.median(data)
1.25 #output
statistics.variance(data)
1.3720238095238095 #output