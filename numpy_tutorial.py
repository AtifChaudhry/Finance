import numpy as np

## Zero vectors and matricies
vec0_10 = np.zeros(10)
print vec0_10
mat0_2_3 = np.zeros((2,3))
print mat0_2_3

## Unit vector and matricies
vec1_5 = np.ones(10)
print vec1_5
mat1_5_5 = np.ones((5,5))
print mat1_5_5

## Random Matrix
vec_16 =np.random.random(16)
print vec_16
mat_4_4 = np.random.random((4,4))
print mat_4_4
print mat_4_4[0,0] + mat_4_4[3,3]
 
## Reshaping Arrays
vec_r4_12 = np.arange(4,12)
print vec_r4_12
mat_r2_4 = vec_r4_12.reshape(2, 4)
print mat_r2_4
mat_r4_2 = mat_r2_4.reshape(4,2)
print mat_r4_2
print mat_r4_2.reshape(1, 8)[0]

## Slice/Dice Arrays
mat_sq3 = np.arange(1,10).reshape(3,3)
print mat_sq3
print mat_sq3[0,0:2]
print mat_sq3[1,1:2]
# Get the four "corners" of the matrix as sub-matricies
print "top left = \n",     mat_sq3[:2,:2]
print "top right = \n",    mat_sq3[:2,1:]
print "bottom left = \n",  mat_sq3[1:,:2]
print "bottom right = \n", mat_sq3[1:,1:]
# Get the three column vectors
print "col0 = ", mat_sq3[:,0]
print "col1 = ", mat_sq3[:,1]
print "col2 = ", mat_sq3[:,2]
# Get the three row vectors
print "row0 = ", mat_sq3[0,:]
print "row1 = ", mat_sq3[1,:]
print "row2 = ", mat_sq3[2,:]

## Indexing Arrays
rndRow = np.random.random(10)
print rndRow
fibIdx = np.array([1,1,2,3,5])
print rndRow[fibIdx]
boolIdx = np.array([True, False, True, False, True, True, True, True, False]).reshape(3,3)
print mat_sq3[boolIdx]

## Numeric Operation on Arrays
print mat_sq3
print "Average = %i" % np.average(mat_sq3)
print "Median = %i" % np.median(mat_sq3)
print "Sum = %i" % np.sum(mat_sq3)
print "Stddev = %.2f" % np.std(mat_sq3)
print "Better than average (%i): \n" % np.average(mat_sq3), mat_sq3 > np.average(mat_sq3)

## Cloning Arrays
clone = mat_sq3.copy()
clone[1,1] += 10
print clone
print mat_sq3

## Matrix-Scalar Operations
print "mat + 1\n", mat_sq3 + 1
print "mat * 5\n", mat_sq3 * 5
print "mat / 2.0\n", mat_sq3 / 2.0

## Matix-Matrix Operations
print "mat + mat\n", mat_sq3 + mat_sq3
print "mat * mat\n", mat_sq3 * mat_sq3
print "mat - mat/2.0\n", mat_sq3 - (mat_sq3/2.0)
print "1/mat\n", 1/np.array(mat_sq3, dtype=float)

## Assigning scalar values to submatrices
clamped = np.array(mat_sq3, dtype=float)
sq3_avg = np.average(mat_sq3)
sq3_std = np.std(mat_sq3)
clamped[mat_sq3 > (sq3_avg + sq3_std)] = sq3_avg + sq3_std
clamped[mat_sq3 < (sq3_avg - sq3_std)] = sq3_avg - sq3_std
print "Clamped\n", clamped

## Tradional matrix multiplication
print "mat x I = \n", np.dot(mat_sq3, np.array([[1,0,0], [0,1,0], [0,0,1]]))
print "mat x mat = \n", np.dot(mat_sq3, mat_sq3)
print "vec . vec = %i" % np.dot(np.arange(1,10), 10-np.arange(1,10))
