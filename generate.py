import argparse
import json
import os
import pylatex as pl
import contractlib.generator

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', nargs='?', help="Input JSON file name", type=str, required=True)
parser.add_argument('-o', '--output', nargs='?', help="Output LaTeX file name", type=str, required=True)
args = parser.parse_args()

args.input = os.path.abspath(args.input)

with open(args.input, 'r') as f:
    data = json.loads(f.read())

doc = contractlib.generator.generate(data)

with open(args.output, 'w') as f:
    f.write(doc.dumps())
