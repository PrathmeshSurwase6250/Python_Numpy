import numpy as py

a = py.array([1, 2, 3,4 ]) 
b = py.array([[1,2,3],[4,5,6]])
c = py.array([[[1,2,3],[4,5,6]], [[8,9,10] , [11,12,13] ]])
print(a)
print(b)
print(c)

data = py.array([1.0,2.3,3.1,4.8] , dtype=py.int32)
print(data)

#like a for loop list creation in arr

d = py.arange(1,100,2)
print(d)

reshapes = py.arange(1,11).reshape(2,5)
print(reshapes)

#ones

one = py.ones((2,4))
print(one)

zeros = py.zeros((2,6))

print(zeros)

random = py.random.random((2,4))
print(random)

linspace = py.linspace(-10,10,10)
print(linspace)

identitymatrix = py.identity((5))
print(identitymatrix)


a1 = py.arange(10)

a2 = py.arange(12).reshape(3,4)

a3 = py.arange(8).reshape(2,2,2)

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)


print(a1.shape)
print(a2.shape)
print(a3.shape)


print(a1.size)
print(a2.size)
print(a3.size)


print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

print(data.dtype)
print(a2.dtype)
print(a3.dtype)

a3 = a3.astype(py.int32)
print(a3.dtype)

p1 = py.arange(12).reshape(3,4)

p2 = py.arange(12 , 24).reshape(3,4)


print(p1* 2)

print(p1 > 10)


print(p1+p2)