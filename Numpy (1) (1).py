         
                    #----------Numpy----------#


# Numpy is one of the fundamental package which is used for scientific calculations.
# we can use Numpy as library to do calculations in data for mutidimentional array to 
        #  perform mathematical functions to operate on the data sets(array).
# Numpy is generally used for processing of array using the package called Numpy.
# we can use Numpy as logical operator, data types,for N-dimensional array,indexing,slicing etc..,
# NumPy can seamlessly and speedily integrate with a wide variety of databases.


          
          
import numpy as np

arr = np.array( [[ 1, 2, 3],[ 4, 2, 5]] ) 
print(arr)
type(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

import numpy as np
value = np.array([[1, 2, 4], [5, 8, 7]])
print(value)
dtype=float # float which floats the real values like 6 with 6.0 for Exact value. 
value=dtype
dtype
value = np.array((1,2,3))
value
print(value)
a=np.zeros((5,6))#The zeros() function will create a new array of the 
                    # specified size with the contents filled with zero values
a
c=np.full((5, 4), 6, dtype = 'complex') # with different numbers or values.
c

k=np.full((7,8),2, dtype = 'complex')
k
b= np.random.random((3, 5)) # Random values.
b
arr = np.array([[1, 2, 3, 4], # 3x4 arry to 2x2x3 array
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
  
newarr = arr.reshape(2, 2,3) 
print(arr)
print(newarr)
import pandas as pd
import numpy as np
value = [20,30,40,50,60]
np.mean(value)
np.median(value)
array = [[15, 16, 12, 35, 45],[15, 16, 22, 18, 20],[43, 1, 4, 1, 4, ]]
array1=pd.DataFrame(array)  
np.median(array1)
np.mean(array1)
np.median(array1,axis=0) # axis is working along the row.
np.median(array1,axis=1)
# stacking : which used for several arrays to get together with differnet axes by vstack or hstack.
a = np.array([[2,4],[6,8]])# inorder to underatand the data type we use []
b = np.array([[10,12],[14,16]])
np.vstack((a,b))
np.hstack((a,b))


import numpy as np
x=np.array([1,2,3,4,5])
print(x.ndim)
print(x.shape)
y=np.array([[[1,2,3]] ,[[4,5,6]]])
print(y.ndim)
z=np.array([[[0,1,2]],[[3,4,5]]],ndmin=3)
print(z.shape)

x= np.array([[[[[2,7,6],[2,4,7],[3,4,5,5,6,4,8],[6,4,3],[5,9,2],[2,4,6],[5,6,8]]]]])
y=np.size(x,2)
print(x.shape)
print(y)
print(x.ndim)




# splitting 
# np.hsplit: Split array along horizontal axis.
# np.vsplit: Split array along vertical axis.
 

import numpy as np 
  
a = np.array([[2, 3, 5, 8, 9, 10],[1, 4, 6, 9, 11, 13]]) 
np.hsplit(a, 3)
np.vsplit(a,2)

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

x=[2,4,6,8,10]
y=[1,2,3,4,5]
plt.plot(x,y)
plt.hist(x,y)
plt.show()
plt.bar(x,y)



        
        

mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3]) 
mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])
result = np.dot(mat1,mat2) # dot which is used for two equal length numbers into single number.
print(result)


# Multidimensional numpy array

import numpy as np # 1-D array

a=np.array([1,0])

b=np.array([0,1])
c=a+b
c


z=np.array([1,2])

y=2*z
y

z=np.array([23,3,455,67,6869])
z=4+z
z

# Basic visualizations in numpy
  # 1D plotting
x=np.linspace(0,2,4)
y=np.linspace(0,3,4)
plt.plot(x,y)
plt.plot(x, y, 'o') 
plt.plot(x,y,'r')

# 2d plotting
image = np.random.rand(40, 40)
plt.imshow(image)
plt.gray()
plt.show()

plt.pcolor(image)
plt.hot()

# 3D plotting

# Mayavi : A tool for easy and interactive visualization of data, 
 # with seamless integration with Python scientific libraries.(TVTk also one library for visuals).
 
# for gaming visuals 3D plotting is used.









