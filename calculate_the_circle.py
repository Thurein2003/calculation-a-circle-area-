import math
import time
a = time.time()
x = math.pi
y = float(input("enter the radius: "))
area = x * (y ** 2)
print ("the area of the circle is: ",area)
print("time taken : "+ str ( time.time()-a))