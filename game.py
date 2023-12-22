import os
import argparse
import argparse_range
from argparse_range import range_action

msg="Please specify the following  grid size for game of life \n"
parser=argparse.ArgumentParser(description=msg)
parser.add_argument("--grid", nargs=2, type=int, help="provide two integers with a space to define the grid x y")
parser.add_argument("--probability", type=float, help="A number between 0-1",action=range_action(0, 1))
#parser.add_argument("--number", type=int, help="an integer number")
args=vars(parser.parse_args())
grid=args['grid']
prob=args['probability']

