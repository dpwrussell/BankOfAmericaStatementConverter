# Bank of America Statement Converter

The Bank of America txt statement is poorly formatted and also contains a
windows en dash. This script converts it into a simple CSV file.

I have elected to drop some basically useless information from the statement,
but the script is self explanatory so can be edited as needed.

Note that it also converts dates to DD/MM.

## Usage:
```
./boa-convert.py [-h] [--account] [--payments] infile outfile
```

```
Convert Bank of America statement .txt to .csv

positional arguments:
  infile      The .txt statement file
  outfile     The .csv output file

optional arguments:
  -h, --help  show this help message and exit
  --account   Include account number in output
  --payments  Include payments in output
```
