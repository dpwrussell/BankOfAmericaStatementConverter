# Bank of America Statement Converter

The Bank of America txt statement is poorly formatted and also contains a
windows en dash. This script converts it into a simple CSV file.

I have elected to drop some basically useless information from the statement,
but the script is self explanatory so can be edited as needed.

Note that it also converts dates to DD/MM.

## Usage:
```
./boa-convert.py statement.txt statement.csv
```
