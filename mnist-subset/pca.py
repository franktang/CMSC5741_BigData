import os.path
import numpy as np
import matplotlib.pyplot as plt
import operator
from matplotlib.mlab import PCA

def display(Xrow):
    ''' Display a digit by first reshaping it from the row-vector into the image.  '''
    plt.imshow(np.reshape(Xrow,(28,28)))
    plt.gray()
    plt.show()

def load_data(digit_list, num):
    ''' 
    Loads all of the images into a data-array (for digits 0 through 5). 

    The training data has 5000 images per digit and the testing data has 200, 
    but loading that many images from the disk may take a while.  So, you can 
    just use a subset of them, say 200 for training (otherwise it will take a 
    long time to complete.

    Note that each image as a 28x28 grayscale image, loaded as an array and 
    then reshaped into a single row-vector.

    Use the function display(row-vector) to visualize an image.
    
    '''
    digit_size = len(digit_list)
    X = np.zeros((num*digit_size,784),dtype=np.uint8)   #784=28*28
    for j in xrange(digit_size):
        digit = digit_list[j]
        print '\nReading digit %d' % digit,
        for i in xrange(num):
            if not i%100: print '.',
            pth = os.path.join('train%d' % digit,'%05d.pgm' % i)
            with open(pth, 'rb') as infile:
                header = infile.readline()
                header2 = infile.readline()
                header3 = infile.readline()
                image = np.fromfile(infile, dtype=np.uint8).reshape(1,784)
            X[j*num + i,:] = image
        print '\n'
    X = X.T
    return X
	
def mean_PCA(matrix):
    '''calculate the mean image'''
    mean_image = np.mean(matrix, axis=1)
    #Display mean image
    display(mean_image)

def image_PCA(matrix):
    '''calculate and display the eigenvectors'''
    eigenvector_size = 20
    eigenpair = []
    
    #calculate covariance matrix
    cov_matrix = np.cov(matrix)
    
    #calculate eigenpairs
    eigenvalue, eigenvector = np.linalg.eig(cov_matrix)
    for i in xrange(len(eigenvalue)):
        eigenpair.append((np.abs(eigenvalue[i]), eigenvector[:,i]))
    sorted(eigenpair, key=operator.itemgetter(0), reverse=True)
    pth = os.path.join("eigenvalues_for_space_%s.txt" % ('_'.join(str(e) for e in digit_space)))
    eigenvalue_file = open(pth, 'w')
	#Display first 20 eigenvectors
    for i in xrange(eigenvector_size):
        #since the eigenvector is in unit length and it has components whose value < 0
        #therefore, we need to scale and shift the vector with
        #new_eigen_vector = old_eigen_vecotr*127.5 + 127.5
        temp_eigenvector = eigenpair[i][1]*127.5
        temp_eigenvector = np.add(temp_eigenvector, np.ones(784)*127.5)
        display(temp_eigenvector.astype(np.uint8))
        eigenvalue_file.write(str(eigenpair[i][0]))
        eigenvalue_file.write("\n")
    eigenvalue_file.close()
        

#load data
digit_space = [0,1,2]
training_size = 5000
X = load_data(digit_space, training_size)

mean_PCA(X)
image_PCA(X)