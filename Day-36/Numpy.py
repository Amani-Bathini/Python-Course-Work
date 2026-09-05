'''
import numpy as np
arr1 = np.array([1,2,3,4,5])
print("1-dim",arr1,sep='\n',end='\n\n')
'''
'''
import numpy as np
arr2 = np.array([[1,2,3],[4,5,6]])
print("2-dim",arr2,sep='\n',end='\n\n')
'''
'''
import numpy as np
arr3 = np.array([[1,2],[3,4],[5,6]])
print("multi-dim",arr3,sep='\n')
'''
'''
import numpy as np
zeros = np.zeros((3,4))
print(zeros)
ones = np.ones((3,4))
print(ones)
identity = np.eye(4)
print(identity)
full_array = np.full((10,2),20)
print(full_array)
'''
'''
import numpy as np
range_arr = np.arange(2,51,2)
print(range_arr)
'''
'''
import numpy as np
lin_space = np.linspace(0,100,5)
print(lin_space)
'''
'''
import numpy as np
rand_arr = np.random.randint(100)
print(rand_arr)
'''
'''
import numpy as np
np.random.seed(40)
rand_arr = np.random.randint(100)
print(rand_arr)
'''
'''
import numpy as np
rand_float = np.random.rand()
print(rand_float)
'''
'''
import numpy as np
rand_float = np.random.rand(4)
print(rand_float)
'''
'''
import numpy as np
rand_int = np.random.randint(1,6,(4,3))
print(rand_int)
'''
'''
import numpy as np
rand_int = np.random.randint(1,6,8)
print(rand_int)
'''
'''
import numpy as np
l = ['html','css','javascript','python','mysql']
rand_choice = np.random.choice(l,3)
print(rand_choice)
'''
'''
import numpy as np
arr = np.array([[1,2],[4,5],[6,7],[8,7],[1,2],[8,9]])
print(arr.shape)
'''
'''
import numpy as np
reshaped = arr.reshape(4,3)
print(reshaped)
'''
'''
import numpy as np
a = np.array([[1,2,3,4],[1,2,3,4]])
flattened = a.flatten()
print(flattened)
'''
'''
import numpy as np
transposed = arr.T
print(transposed)
'''
'''
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[:3])
print(arr[::2])
'''
'''
import numpy as np
matrix = np.array(([10,20,30],[40,50,60],[70,80,90]))
print(matrix[0:3,1])
print(matrix[1:3,2])
print(matrix[0:2,0:2])
print(matrix[1:3,1:3])
'''
'''
import numpy as np
arr = np.array([4,9,16,25,36])
print(arr+10)
print(arr*2)
print(arr**0.5)
'''
'''
import numpy as np
arr = np.array([4,9,16,25,36])
print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
'''
'''
import numpy as np
a = np.array([1,2,3,4,5])
print(np.mean(a))
print(np.var(a))
print(np.std(a))
'''
'''
import numpy as np
arr = np.array([1,2,3,4,5])
print(np.cumsum(arr))
print(np.cumprod(arr))
'''
'''
import numpy as np
arr = np.array([1,2,3,4,5,5,6,6,7,8,8,3])
print(arr%2==0)
print(arr[arr%2==0])
'''
'''
import numpy as np
arr = np.array([3,1,4,1,5,9,2,6])
sorted_arr = np.sort(arr)
print(sorted_arr)
'''
'''
import numpy as np
unique_vals = np.unique(arr)
print(unique_vals)
'''
'''
import numpy as np
arr = np.array([10,20,30])
view_arr = arr.view()
view_arr[0] = 100
print(arr,view_arr)
'''
'''
import numpy as np
copy_arr = arr.copy()
copy_arr[0] = 200
print(arr,copy_arr)
'''
'''
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
'''
'''
import numpy as np
A = np.array([[1,2],[3,4]])
print(np.linalg.det(A))
'''
'''
import numpy as np
A = np.array([[1,2],[3,4]])
print(np.linalg.inv(A))
'''
'''
import numpy as np
A = np.array([[1,2],[3,4]])
eigenvalues,eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)
'''
'''
import numpy as np
A = np.array([[1,2],[3,4]])
C = np.array([5,11])
solution = np.linalg.solve(A,C)
print(solution)
'''
'''
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
vertical_stack = np.vstack((A,B))
horizontal_stack = np.hstack((A,B))
print(vertical_stack)
print(horizontal_stack)
'''

import numpy as np
split_arr = np.split(np.array([1,2,3,4,5,6]),3)
print(split_arr)