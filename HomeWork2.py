
import numpy as np

# Create matrix A with size (3,5) containing random numbers


A=np.random.rand(3,5)


# Find the size and length of matrix A


print (np.size(A))
print()
print (len(A))
print()

# Resize (crop/slice) matrix A to size (3,4)




A=A[0:3,0:4]


# Find the transpose of matrix A and assign it to B



B=np.transpose(A)


# Find the minimum value in column 1 of matrix B




print (np.min(B[:,1]))
print()

# Find the minimum and maximum values for the entire matrix A




print (A.min())
print()

# Create vector X (an array) with 4 random numbers


X=np.random.rand(4)



# Create a function and pass vector X and matrix A in it.
# In the new function mulitply vector X with matrix A and assign the result to D


def mult(mat,vec):
    return mat.dot(vec)


D=mult(A,X)
print (D)
print()

# Create a complex number Z with absolute and real parts != 0

Z=1+2j


# Show its real and imaginary parts as well as it’s absolute value


print (np.real(Z))
print()
print (np.imag(Z))
print()
print (np.abs(Z))
print()

# Multiply result D with the absolute value of Z and record it to C

C=D*np.abs(Z)

# Convert matrix B from a matrix to a string and overwrite B




B=np.array2string(B) 


print ('Souvik is done with Homework 2')

