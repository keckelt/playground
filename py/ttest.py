import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


a = np.array([2,3,4,6,7,3,4,5])
b =np.array( [3,4,5,1,9,3,6,7])

a1 = a[0:5]
a2 = a[5:]
b1 = b[0:5]
b2 = b[5:]
asel = np.take(a,[0,2,3,5,7])
bsel = np.take(b,[0,2,3,5,7])

print(b)
print(bsel)
print(b1)
print(b2)

print(stats.ttest_ind(asel,a1))
print(stats.ttest_ind(asel,a2))
print(stats.ttest_ind(bsel,b1))
print(stats.ttest_ind(bsel,b2))




fig1, ax1 = plt.subplots()
ax1.boxplot([asel, a2], vert=False)
plt.yticks([1, 2], ['Selected', 'Num1: B',])
plt.show()