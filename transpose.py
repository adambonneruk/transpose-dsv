import itertools
import sys
import os

from csv import reader, writer

infile = sys.argv[1]
outfile = "transposed_"+infile
csvdelim = sys.argv[2]

os.system("cls")
os.system("echo CSV Transpose Tool - Adam Bonner - 2016-05-23 - Ver 1.00 - www.adambonner.co.uk")
os.system("echo --------------------------------------------------------------------------------")

print('Input File: "' + str(infile) + '"')
print('Output File: "' + str(outfile) + '"')
print('Delimeter: "' + str(csvdelim) + '"')

print('\nWorking...')

with open(infile) as f:
	with open(outfile, 'w', newline="\n", encoding="utf-8") as fw:
		writer(fw, delimiter=csvdelim).writerows(zip(*reader(f, delimiter=csvdelim)))

print('...Done!')