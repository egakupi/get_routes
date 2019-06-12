import argparse
import re
from os.path import isfile
from src.parse_file import parse_file
from src.graph import Graph

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="Path of file")
parser.add_argument("source", type=str, help="3-letter (IATA) or 4-letter (ICAO) code of the source airport.")
parser.add_argument("destination", type=str, help="3-letter (IATA) or 4-letter (ICAO) code of the destination airport.")
parser.add_argument("transfers", type=int, default=3, help="Number of transfers")
args = parser.parse_args()

file = args.file
source = args.source
destination = args.destination
transfers = args.transfers

if not isfile(file):
    print('File \'{0}\' doesn\'t exist.'.format(file))
    exit(-1)

if not re.match(r'\b[A-Z]{3,4}\b', args.source):
    print('The source airport is not correct.')
    exit(-1)

if not re.match(r'\b[A-Z]{3,4}\b', args.destination):
    print('The destination airport is not correct.')
    exit(-1)

if not 0 <= args.transfers < 4:
    print('Number of transfer should be 0..3')
    exit(-1)

g = parse_file(args.file)
g = Graph(g)
findall = g.find_all_paths('DYU', 'AER', edge_number=2)
for f in findall:
    print(f)