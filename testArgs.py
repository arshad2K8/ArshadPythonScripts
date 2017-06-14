__author__ = 'arshad'
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity",
                    help="increase output verbosity")
args = parser.parse_args()

print args.square
print  args.verbosity