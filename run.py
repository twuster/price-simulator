import argparse

parser = argparse.ArgumentParser(description='On-demand price simulator')
parser.add_argument(
    '--num_drivers',
    type=int,
    help='number of initial drivers (default: 50)'
)
parser.add_argument(
    '--num_passengers',
    type=int,
    help='number of initial passengers (default: 50)'
)

args = parser.parse_args()
print(args.num_drivers)
print(args.num_passengers)