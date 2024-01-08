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

x=np.random.randint( 0,high=garray.shape[0]+1,size=total_ones*2)
y=np.random.randint( 0,high=garray.shape[1]+1,size=total_ones*2,)
# Assign 1s randomly to the grid

print([x,y])

coord = set(tuple(zip(x, y)))

if(coord < total_ones):
    

print(len(set(coord)))