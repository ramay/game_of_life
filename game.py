import os
import argparse
import numpy as np
from argparse_range import range_action

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

print(garray.shape)


def isValid(np_shape: tuple, index: tuple):
    if min(index) < 0:
        return False
    for ind,sh in zip(index,np_shape):
        if ind >= sh:
            return False
    return True

for i in range(grid[0]):
 for j in range(grid[1]):
   print(i,j)
   x_p=i+1
   x_m=i-1
   y_p=j+1
   y_m=j-1
   print(x_p,j)
   if(isValid(garray.shape,(x+1,j))):
      print("yay")
      
   else:
      print("nay")



   #check how many neighbors are 1s 
    
   #check how many neighbors are 0s

print(range(grid[0]))
print(grid[0])
print(garray.shape)


