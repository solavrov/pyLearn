import numpy as np

A = np.array([[1, 1, 1, 1], [18.56842, 24.77806, 21.73271, 21.31403]])
L = np.dot(np.linalg.inv(np.dot(A, np.transpose(A))), A)
P = (np.identity(4) - np.dot(np.transpose(A), L))

w = np.array([[0.2381944], [0.2473083], [0.2462570], [0.2682404]])
S = np.array([[156.2568, 184.1724, 121.3665, 107.1022],
              [184.1724, 314.6176, 160.9563, 239.6796],
              [121.3665, 160.9563, 309.5928, 146.6842],
              [107.1022, 239.6796, 146.6842, 215.1583]])

grad = 2 * np.dot(S, w)
d = -np.dot(P, grad)

check = np.dot(-np.transpose(grad), d)






