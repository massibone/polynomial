#x**2 + 2x + 3 = 0 we have [ 1 2 3]
# 2x**2 + 3x + 4 = 0 we have [2 3 4]

import numpy as np

p = np.poly1d([1,2,3])

print (p)

root=p.roots
print ("Solution for p : ",root)

#4x**3 + 3x**2 + 2x + 6 = 0
p2=np.poly1d([4,3,2,6])

root2=p2.roots


print("Solution for ")
print(p2 ,":")
print(root2)

