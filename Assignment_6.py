import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Addition:", np.add(arr1, arr2))
print("Subtraction:", np.subtract(arr2, arr1))
print("Multiplication:", np.multiply(arr1, arr2))
print("Division:", np.divide(arr2, arr1))

print("Sine values:", np.sin(arr1))
print("Cosine values:", np.cos(arr1))

print("Exponential:", np.exp(arr1))
print("Natural Log:", np.log(arr1))

arr3=np.array([1,4,9,16])
print("Square root:", np.sqrt(arr3))
print("Power of 2:", np.power(arr3, 2))