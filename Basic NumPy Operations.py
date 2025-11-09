import numpy as np

arrayA = np.array([10, 20, 30, 40, 50])
arrayB = np.array([5, 4, 3, 2, 1])

print("Addition:", arrayA + arrayB)
print("Subtraction:", arrayA - arrayB)
print("Multiplication:", arrayA * arrayB)
print("Division:", arrayA / arrayB)

print("Mean:", arrayA.mean())
print("Maximum:", arrayA.max())
print("Minimum:", arrayA.min())
print("Dot Product:", arrayA.dot(arrayB))
print("Reshape:", arrayA.reshape(5,1))