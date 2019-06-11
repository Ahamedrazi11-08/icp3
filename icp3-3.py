import numpy as np
import random

#creating a random vector of size 15 having numbers between 1 to 20
k=np.random.randint(1,20, size=15)
print("original array")
print(k)

#Replacing max value with 0 in vector
k[k.argmax()]=0
print(k)