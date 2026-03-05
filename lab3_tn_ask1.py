import numpy as np


def activation(x):
    if x >= 0.5:
        return(1)
    else:
        return (0)

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 0, 0, 1])
N = 4
p = 2
w = np.zeros(p)
y_est = np.zeros(N)
step = 0.25

E = 10
while E > 0.0001:
  E = 0
  for k in range(N):
    a = 0
    for j in range(p):
      a = a + x[k,j] * w[j]
    y_est[k] = activation(a)
  E = E + abs(y[k] - y_est[k])
  w += step
w -= step

print(w)
