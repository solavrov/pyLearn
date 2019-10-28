from numpy import array as array, dot as dot, transpose as t
from numpy import linalg as alg

a = array([[1, 2, 3],
           [2, 5, 3],
           [3, 3, 9]])

b = array([[1],
           [1],
           [1]])

c = dot(a, b)

d = array([[1, 2],
           [-3, 4]])

# print(c)

print(alg.det(a))

eigen_all = alg.eig(a)
print(eigen_all)
eigen_vectors = eigen_all[1]
print('\neigen vectors:\n', eigen_vectors)
print('\ninv eigen vectors:\n', alg.inv(eigen_vectors))

trans_a = dot(t(eigen_vectors), dot(a, eigen_vectors))
print('\ntransformed a:\n', trans_a, '\n')

v0 = array([eigen_vectors[:, 0]])
v1 = array([eigen_vectors[:, 1]])
v2 = array([eigen_vectors[:, 2]])
print(v0, v1, v2)
print('v0.v1=', dot(v0, t(v1)))
print('v1.v2=', dot(v1, t(v2)))
print('v0.v2=', dot(v0, t(v2)))
