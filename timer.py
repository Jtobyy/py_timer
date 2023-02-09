#!/usr/bin/python3
from argparse import ArgumentParser
from time import sleep


parser = ArgumentParser() # to accept integer as an argument
parser.add_argument("time", type=int) # define command line positional parameters
args = parser.parse_args() # runs the parser and places the extracted data in a argparse.Namespace object

print(f"Starting timer of {args.time} seconds")
for _ in range(args.time):
    print('.', end='', flush=True) # forcibly flush the stream (needed cause of the sleep() call)
    sleep(1)
print('Done!')

