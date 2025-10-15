import argparse

import sys

parser = argparse.ArgumentParser(description='Text transformation utility')

parser.add_argument('--reverse', action='store_true', help='Reverse the text')
parser.add_argument('--uppercase', action='store_true', help='Convert text to uppercase')
parser.add_argument('--count', action='store_true', help='Count words and characters')
parser.add_argument('--size', action='store_true', help='Display memory footprint of the text')
parser.add_argument('--quiet', action='store_true', help='Suppress extra messages')
parser.add_argument('text', type=str, help='Input text to transform')
args = parser.parse_args()
text = args.text

if args.reverse:
    text = text[::-1]
if args.uppercase:
    text = text.upper()
if args.count:
    words = len(text.split())
    chars = len(text)
    if not args.quiet:
        print(f'Word count: {words}, Character count: {chars}')
if args.size:
    size = sys.getsizeof(text)
    if not args.quiet:
        print(f'Memory size: {size} bytes')
if not args.quiet:
    print('Transformed text:')
print(text)
