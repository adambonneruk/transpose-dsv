# transpose-dsv (in Python) ![](icon/design/16.png)
CLI-based transposing of delimiter-separated values (including .csv/comma-separated values).  Written in Python using Python 3.8.5 and VS Code

## Background
In May 2016, I was working with some rather large extract files that typically had many columns (more than 10k) but only a few rows (typicially less than 5000). Opening these files in Excel was impossible as it hit the column limit (~16,384). Therefore I developed this script to "Transpose" the columns and rows in the following manner:

```
-------------------------          -----------------------------------
|         |  W  |   V   |          |       | Alpha | Bravo | Charlie |
-------------------------          -----------------------------------
| Alpha   |  5  |   yes |  > to >  |   W   |   5   |   6   |   17    |
-------------------------          -----------------------------------
| Bravo   |  6  |    no |          |   V   |  yes  |  no   |  maybe  |
-------------------------          -----------------------------------
| Charlie | 17  | maybe |         
-------------------------          
```

## [Wikipedia](https://en.wikipedia.org/wiki/Delimiter-separated_values) description of ```.dsv``` and ```.csv```
### DSV
Formats that use delimiter-separated values (also DSV) store two-dimensional arrays of data by separating the values in each row with specific delimiter characters. Most database and spreadsheet programs are able to read or save data in a delimited format. Due to their wide support, DSV files can be used in data exchange among many applications.

A delimited text file is a text file used to store data, in which each line represents a single book, company, or other thing, and each line has fields separated by the delimiter.

### CSV
CSV, a specific subset of DSV, is more widely adpoted and used the comma character as a seperator. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields.

The CSV file format is not fully standardized. The basic idea of separating fields with a comma is clear, but that idea gets complicated when the field data may also contain commas or even embedded line breaks. CSV implementations may not handle such field data, or they may use quotation marks to surround the field. Quotation does not solve everything: some fields may need embedded quotation marks, so a CSV implementation may include escape characters or escape sequences.

## Icon
![](icon/design/256.png)

## Prerequisites
* Python 3
  * itertools
  * sys
  * os
* PyInstaller
* Notepad++

### Install Guide
```powershell
choco install python
# restart commandline for system path edits
pip install pyinstaller
```

## Usage
```powershell
CSV Transpose Tool
	
	used as: TransposeCSV[.py|.exe] inputfile.ext sep
	
	tested separators:
		| (escape using ^|)
		,
		#
```

## Note / Limitations
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Future Ideas (braindump)
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## VS Shortcuts
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
