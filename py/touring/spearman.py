import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn import datasets
import scipy.stats as stats
from math import sin, fabs, cos, pow, tan
from random import random


X = range(0, 100)

def randomWave():
  wave = [0] * (X[-1]+1)
  for x in X:
    wave[x] += random()*30
    for i in range(x):
      wave[x] += fabs(sin(i/15.0)) + cos(i/5)*2
  
  return wave


def randomWave2():
  wave = [0] * (X[-1]+1)
  for x in X:
    wave[x] += random()*8
    for i in range(x):
      wave[x] += fabs(sin(i/10.0)) + sin(i/10.0)*0.9

  return wave
      
def wave():
  wave = [0] * (X[-1]+1)
  for x in X:
    for i in range(x):
      wave[x] += fabs(sin(i/10.0)) + sin(i/10.0)*0.9
  
  return wave

Y = randomWave2()
Y_ranked = stats.rankdata(Y)

plt.figure()
plt.scatter(X,Y)
plt.scatter(X,Y_ranked)


print(stats.pearsonr(X, Y))
print(stats.spearmanr(X, Y))


plt.show()
