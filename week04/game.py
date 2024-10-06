
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def game():

    reward = 0
    dice = 0
    count=0
    result=[]

    while count<1000:
        while True and count<1000:
            count+=1
            temp = np.random.randint(1, 7)
            if temp==1 or temp==2:
                        break
            else:
                        reward+=4

        result.append(reward)  
        reward=0          

    return result


result=game()

y_axis=Counter(result)
print(y_axis)

plt.bar(y_axis.keys(), y_axis.values())
plt.show()


            
       
