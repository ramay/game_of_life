import os
import argparse
import numpy as np
from argparse_range import range_action
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# This function checks if the index exists in an array
def isValid(np_shape: tuple, index: tuple):
    #print(index,"**",np_shape)
    if min(index) < 0:
        return False
    for ind,sh in zip(index,np_shape):
        if ind >= sh:
            return False
    return True

# This function updates each cell based on it's neighbors
def change_garray(garray,grid):
    for i in range(grid[0]):
        for j in range(grid[1]):
            neibs=0
            if(isValid(garray.shape,(i+1,j))):
                neibs+= garray[i+1][j]
            if(isValid(garray.shape,(i-1,j))):
                neibs+= garray[i-1][j]
            if(isValid(garray.shape,(i,j+1))):
                neibs+= garray[i][j+1]
            if(isValid(garray.shape,(i,j-1))):
                neibs+= garray[i][j-1]
            if(isValid(garray.shape,(i+1,j+1))):
                neibs+= garray[i+1][j+1]
            if(isValid(garray.shape,(i-1,j-1))):
                neibs+= garray[i-1][j-1]
            if(isValid(garray.shape,(i-1,j+1))):
                neibs+= garray[i-1][j+1]
            if(isValid(garray.shape,(i+1,j-1))):
                neibs+= garray[i+1][j-1]
            #   print("My neibs are",neibs)
            
            if(garray[i][j]==1):
                    if(neibs < 2 ):
                        garray[i][j]=0
                    elif((neibs > 2) & (neibs <=3)):
                        garray[i][j]=1
                    elif(neibs > 3):
                        garray[i][j]=0
            if((garray[i][j]==0) & (neibs==3)):
                    garray[i,j]=1    
    return(garray)




msg="Please specify the following  grid size for game of life \n"
parser=argparse.ArgumentParser(description=msg)
parser.add_argument("--grid", nargs=2, type=int, help="provide two integers with a space to define the grid x y")
parser.add_argument("--probability", type=float, help="A number between 0-1",action=range_action(0, 1))
#parser.add_argument("--number", type=int, help="an integer number")
args=vars(parser.parse_args())
grid=args['grid']
prob=args['probability']

# create a array of size grid

garray=np.zeros(grid)
print(grid[0],grid[1],prob)
total_ones=int(prob*(grid[0]*grid[1]))
print(total_ones)

x=np.random.randint( 0,high=garray.shape[0],size=total_ones*5)
y=np.random.randint( 0,high=garray.shape[1],size=total_ones*5)
# Assign 1s randomly to the grid

print([x,y])

coord = list(set(tuple(zip(x, y))))


if(len(coord) < total_ones):
    print("Error, not enough unique ")
    exit(1)

print(len(coord))

coord=coord[0:total_ones]

for x,y in coord:
    print(x,y)
    garray[x,y]=1

print("Initial Garry")
print(garray)





def update(frame,matrix,grid):
    # Update the matrix with new random values
    print("grid",grid)
    matrix = change_garray(matrix,grid)
    print("Matrix***",matrix)
    # Update the data in the matshow plot
    mat.set_array(matrix)
    return matrix
     
#    x+=1
#    print(garray)
#print("dfsd",change_garray(garray,grid))
fig, ax = plt.subplots()
mat = ax.matshow(garray, cmap='viridis')
#print(mat)
#print("Test")
#plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update,fargs=(garray,grid),frames=10)
#plt.show()

writergif = animation.PillowWriter(fps=10)
ani.save('filename.gif',writer=writergif)



