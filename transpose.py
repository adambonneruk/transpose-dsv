import itertools
import sys
import os
import re
from csv import reader, writer

if sys.argv[1] == '--help': #activiate help mode
	print ("-----Help Mode-----\n")
	print("Usage: transpose.(py|exe) FILE DELIMITER_FLAG [CUSTOM_DELIMITER]")
	# standard argument <required argument> [optional option]	curly braces {default values} parenthesis (miscellaneous info)
	# syntax taken from: https://stackoverflow.com/questions/21503865/how-to-denote-that-a-command-line-argument-is-optional-when-printing-usage
	print("")
	print("Transpose a given .csv/.dsv file's X and Y axis")
	print("")
	print("Supported Switches/Arguments.")
	print("  -c, --comma\t comma delimiter \",\"")
	print("  -p, --pipe\t pipe delimiter \"|\"")
	print("  -t, --tab\t tab delimiter \"\t\"")
	print("  -h, --hash\t comma delimiter \"#\"")
	print("  -r, --caret\t caret (hat) delimiter \"^\"")
	print("  -x, --custom\t custom delimiter, follow with [CUSTOM_DELIMITER]")
	print("      --help\t display this help message")
	print("")
	print("Usage Examples:")
	print("  comma seperated file called example.csv:")
	print("\ttranspose example.csv -c")
	print("")
	print("  hash seperated file called hashes.hsv:")
	print("\ttranspose hashes.hsv -h")
	print("")
	print("  custom hat-and-pipe seperated extract.mi:")
	print("\ttranspose extract.mi -x ^|")
	print("")
	print("")
	print("Adam Bonner, 2020, https://github.com/adambonneruk/transpose-dsv")
	print("")
else:
	print("-----Transpose Mode-----\n")
	infile = sys.argv[1]
	outfile = "transposed_"+infile
	csvdelim = sys.argv[2]
	print('Input File: "' + str(infile) + '"')
	print('Output File: "' + str(outfile) + '"')
	print('Delimeter: "' + str(csvdelim) + '"')
	###################################################################
	if re.search("^(-x|--custom$)", sys.argv[2]):
		print("-----Custom Delim Mode-----\n")
	elif re.search("^(-[cpthr]|--(comma|pipe|tab|hash|caret))$", sys.argv[2]):
		print("-----Normal Delim Mode-----\n")
	else:
		print("-----Delim Error-----\n")

#os.system("cls")
#os.system("echo CSV Transpose Tool - Adam Bonner - 2016-05-23 - Ver 1.00 - www.adambonner.co.uk")
#os.system("echo --------------------------------------------------------------------------------")
#
#print('Input File: "' + str(infile) + '"')
#print('Output File: "' + str(outfile) + '"')
#print('Delimeter: "' + str(csvdelim) + '"')
#
#print('\nWorking...')

#with open(infile) as f:
#	with open(outfile, 'w', newline="\n", encoding="utf-8") as fw:
#		writer(fw, delimiter=csvdelim).writerows(zip(*reader(f, delimiter=csvdelim)))
#
#print('...Done!')