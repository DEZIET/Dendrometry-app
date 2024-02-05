from math import sqrt 
import numpy as np
import math as m
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

d = [31,25,30]
h = [20,21,23]
D = []
ni = [2,20,23,50,77]
di = [12,14,16,18,20]

for i in range(len(d)):
    
    arg = d[i]/(sqrt(h[i]-1.3))
    D.append(arg)
    

#transformacja
d = np.array(d)
D = np.array(D)
d = d.reshape(-1 , 1)
D = D.reshape(-1 , 1)

# Utworzenie modelu regresji liniowej i dopasowanie
model = LinearRegression()
model.fit(d, D)

# Wartości przewidywane przez model regresji liniowej
D_pred = model.predict(d)

# Współczynniki a i b w równaniu y = a*x + b
a = model.coef_
b = model.intercept_

hi = []
for i in range(len(di)):

    arg = ((di[i]/(b+a*di[i]))**2)+1.3
    hi.append(arg)
    
print(hi)

hi = np.array(hi)
di = np.array(di)
hi = hi.reshape(-1 , 1)
di = di.reshape(-1 , 1)

import matplotlib.pyplot as plt

plt.plot(di, hi, color='red', linewidth=2, label='funkcja nasluda')
plt.xlabel('d')
plt.ylabel('h')
plt.legend()
plt.show()
