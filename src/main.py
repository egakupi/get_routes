import argparse
import re
from os.path import isfile
from src.parse_file import parse_file
from src.graph import Graph

if __name__ == "__main__":
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

    if not re.match(r'\b[A-Z]{3,4}\b', source):
        print('The source airport \'{0}\' is not correct. Should be 3-letter (IATA) or 4-letter (ICAO) code.'
              .format(source))
        exit(-1)

    if not re.match(r'\b[A-Z]{3,4}\b', destination):
        print('The destination airport \'{0}\' is not correct. Should be 3-letter (IATA) or 4-letter (ICAO) code.'
              .format(destination))
        exit(-1)

    if not 0 <= transfers < 4:
        print('Number of transfer should be 0..3')
        exit(-1)

    g = Graph(parse_file(args.file))
    findall = g.find_all_paths(source, destination, edge_number=transfers)
    if findall:
        print('Routes from {0} to {1}:'.format(source, destination))
        for route in sorted(findall, key=len):
            print(*route, sep=', ')
    else:
        print('Routes from {0} to {1} are not found.'.format(source, destination))
