# implementation of array using numpy
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

print("\nArray Addition:", arr1 + 5)
print("\nsquar root array1:",np.sqrt(arr1))
print("Array Multiplication:", arr1 * 2)

print("\nSliced Array (first 3 elements):", arr1[:3])
print("Sum:", np.sum(arr1))