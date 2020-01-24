"""
Density plots for the bacteria bomb model
Created by Cameron Leighton 
Using https://python-graph-gallery.com/2d-density-plot/
"""
#imports the operators 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde
 
# Create data: 200 points
data = np.random.multivariate_normal([0, 1], [[1, 0.1], [0, 3]], 200)
x, y = data.T


#importing the data from the bacteria bomb model however the model failed
#environment = []
##create the environment
#with open ('fallen.csv') as f:
##open CSV 
#    readCSV = csv.reader(f,delimiter = ',')
##for each row in CSV it creates a new list 
#    for column in readCSV:
#        columnlist = []
##for each value in the column of the CSV it appends the interger
#        for value in cloumn:
##            print(float(value))
#            columnlist.append(int(value))
##the column list is then appended into the environment 
#        environment.append(columnlist)
 
# Create a figure with 6 plot areas
fig, axes = plt.subplots(ncols=6, nrows=1, figsize=(21, 5))
 
# Creates the scaterplot of data 
axes[0].set_title('Scatterplot')
axes[0].plot(x, y, 'ko')

 
# Thus we can cut the plotting window in several hexbins
nbins = 20
axes[1].set_title('Hexbin')
axes[1].hexbin(x, y, gridsize=nbins, cmap=plt.cm.magma)
 
# creates the 2D histogram
axes[2].set_title('2D Histogram')
axes[2].hist2d(x, y, bins=nbins, cmap=plt.cm.magma)
 
# Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
#uses the kernal density of the data 
k = kde.gaussian_kde(data.T)
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
 
# plot a density
axes[3].set_title('Calculate Gaussian KDE')
#plots the gaussian KDE 
axes[3].pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.cm.magma)
 
# add shading to the density 
axes[4].set_title('2D Density with shading')
#adds the shading to smooth the Guassian KDE
axes[4].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.magma)
 
# creates the contours on the density
axes[5].set_title('Contour')
axes[5].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.magma)
axes[5].contour(xi, yi, zi.reshape(xi.shape) )
#plots to a png and removes alot of the white space 
plt.savefig('density', bbox_inches ='tight')

#adds an axis to show the density 
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading ='gouraud', cmap=plt.cm.magma)
plt.colorbar()
plt.show()



