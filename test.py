import numpy as np 
a = np.array([1, 2, 1, 1, -3, -4, 7, 8, 9, 10, -2, 1, -3, 5, 6, 7, -10])
# zero_crossings = a[1:] * a[:-1] 
# print(zero_crossings)
# print((np.sign(zero_crossings) == -1).sum())
print(np.sign(a[a!=0]))
print(np.diff(np.sign(a[a!=0])))
print((np.diff(np.sign(a[a!=0]))!=0).sum())
a = np.array([ 1,  2,  1,  0, -1, -2, -1,  0,  1,  0])
print((np.diff(np.sign(a[a!=0]))!=0).sum())
