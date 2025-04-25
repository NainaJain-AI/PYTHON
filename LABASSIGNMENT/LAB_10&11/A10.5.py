import numpy as np
def formated(names):
 for name in names:
 
  left=name.ljust(15,"_")
  right=name.rjust(15,"_")
  center=name.center(15,"_")
  print(left,right,center)
  
names=np.array(input("").split())
formated(names)




