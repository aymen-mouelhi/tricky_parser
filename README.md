## Introduction

This package helps parsing a specif format of a web data file.

## Installation

Start by cloning the repository:
```
git clone https://github.com/aymen-mouelhi/tricky_parser.git
cd tricky_parser
```
Then
```
pip install -r requirements.txt
python setup.py install
```

## Usage
The parser can be used by calling the parse.py file.
The file expects the to be cleaned file path. By default it will generate csv files in the same location from where you launch the script.

 
You can also specify the path the folder in which the cleaned files will be stored.
Additionally you can select whether you want the files in csv, json or excel.
```
python parse.py --filepath ./file.xls --output_folder ./json --output_format json
```

For more information, you can run:
```
python parse.py -h
```

## Tests
To run tests simply run the following command:
```
python test_parser.py
```