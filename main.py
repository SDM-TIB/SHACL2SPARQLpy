# -*- coding: utf-8 -*-
import argparse
from SHACL2SPARQLpy.Eval import *
import time

if __name__ == '__main__':
    start = time.time()

    parser = argparse.ArgumentParser(description='SHACL Constraint Validation over a SPARQL Endpoint')
    parser.add_argument('-d', metavar='schemaDir', type=str, default=None,
                        help='Directory containing shapes')
    parser.add_argument('endpoint', metavar='endpoint', type=str, default=None,
                        help='SPARQL Endpoint')
    parser.add_argument('outputDir', metavar='outputDir', type=str, default=None,
                        help='Name of the directory where results of validation will be saved')
    parser.add_argument('--selective', action='store_true', default=False,
                        help="Use more selective queries", required=False)

    parser.add_argument("-m", metavar="maxSize", type=int, default=256,
                        help='max number of instances allowed to be in a query', required=False)

    parser.add_argument('-j', '--json', action='store_true', default=False, required=False,
                        help='Indicates that the SHACL shape schema is expressed in JSON')

    args = parser.parse_args()

    Eval(args)

    end = time.time()
    print("Total program runtime:", end - start, "seconds")
