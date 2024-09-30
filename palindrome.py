import argparse


def pars_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--in_file', help='The path to the file with a possible list of palindromes',
                        type=str, metavar='incoming.txt', required=True)
    parser.add_argument('-o', '--out_file', help='The path to the file with the filtered list of palindromes',
                        type=str, metavar='outcoming.txt', required=True)
    return parser.parse_args()


def is_palindrome(raw_string):
    return raw_string.lower() == raw_string.lower()[::-1]


def find_palindrome(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as in_file, open(out_path, 'w', encoding='utf-8') as out_file:
        for line in in_file.readlines():
            if is_palindrome(line.rstrip()):
                out_file.write(line)


def main():
    try:
        args = pars_args()
        find_palindrome(args.in_file, args.out_file)
        print('Done')
    except FileNotFoundError:
        print('The incoming file was not found')


if __name__ == '__main__':
    main()
