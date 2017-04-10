# -*- coding: UTF-8 -*-

import math


## 计算两个点的欧氏距离
def computerEuclideanDistance(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return distance

d_a = computerEuclideanDistance(3, 104, 18, 90)
d_b = computerEuclideanDistance(2, 100, 18, 90)
d_c = computerEuclideanDistance(1, 81, 18, 90)
d_d = computerEuclideanDistance(101, 10, 18, 90)
d_e = computerEuclideanDistance(99, 5, 18, 90)
d_f = computerEuclideanDistance(98, 2, 18, 90)

print "d_a: ", d_a
print "d_b: ", d_b
print "d_c: ", d_c
print "d_d: ", d_d
print "d_e: ", d_e
print "d_f: ", d_f
