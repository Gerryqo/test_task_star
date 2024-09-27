import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--in_file', help='The path to the file with a possible list of palindromes',
                    type=str, metavar='incoming.txt', required=True)
parser.add_argument('-o', '--out_file', help='The path to the file with the filtered list of palindromes',
                    type=str, metavar='outcoming.txt', required=True)
args = parser.parse_args()


def find_palindrome(raw_string):
    if str(raw_string.lower()) == str(raw_string.lower())[::-1]:
        return True


try:
    with open(args.in_file, 'r', encoding='utf-8') as in_file:
        for line in in_file.readlines():
            if find_palindrome(line.rstrip()):
                with open(args.out_file, 'a', encoding='utf-8') as out_file:
                    out_file.write(line)
    print('Done')
except FileNotFoundError:
    print('The incoming file was not found')
except Exception as e:
    print(e)
