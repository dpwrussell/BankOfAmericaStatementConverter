#!/usr/bin/env python

import argparse
import os
import re
import csv


def fix_date(s):
    return s[3:5] + '.' + s[0:2]


def reduce_whitespace(s):
    return re.sub(r'\s+', ' ', s).strip()


def remove_whitespace(s):
    return re.sub(r'\s', '', s)


def remove_commas(s):
    return re.sub(r',', '', s)


def process_statement(infile, outfile):

    escape_char = re.compile(u'\x96', re.MULTILINE)
    transaction_regex = re.compile(r'^\s*(\d{2}\/\d{2})\s+(\d{2}\/\d{2})\s+(.*\w)\s+(\d{4})\s+(\d{4})\s+((?:-\s)?[\d\.,]+)\n?\s*((?:-\s)?[\d\.,]*\s\w{3})?$', re.MULTILINE)

    with open(infile, 'rU') as f:
        with open(outfile, 'wb') as csvfile:
            twriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            content = f.read()

            # Replace the en dash with a minus sign
            content = re.sub(escape_char, '-', content)

            transactions = re.findall(transaction_regex, content)
            for transaction in transactions:
                transaction_date = fix_date(transaction[0])
                posting_date = fix_date(transaction[1])
                description = reduce_whitespace(transaction[2])
                reference = transaction[3]
                account = transaction[4]
                amount = remove_commas(remove_whitespace(transaction[5]))
                foreign = ' (' + reduce_whitespace(transaction[6] + ')') if transaction[6] != '' else ''

                # Ignore payments
                if description != 'BA ELECTRONIC PAYMENT':

                    # Write transactions to CSV file
                    twriter.writerow([
                        transaction_date,
                        # posting_date,
                        description + foreign,
                        reference,
                        # account,
                        amount
                    ])


parser = argparse.ArgumentParser(
    description='Convert Bank of America statement .txt to .csv'
)
parser.add_argument('infile', type=str, help='The .txt statement file')
parser.add_argument('outfile', type=str, help='The .csv output file')

args = parser.parse_args()

if not os.path.isfile(args.infile):
    print 'Statement file does not exist: %s' % args.infile
    exit(1)

process_statement(args.infile, args.outfile)
