
import argparse
import os
import sys

def validate_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"ファイルが見つかりません: {path}")
    return path

def reverse_file(input_path, output_path):
    with open(input_path, 'r') as infile:
        content = infile.read()
    reversed_content = content[::-1]
    with open(output_path, 'w') as outfile:
        outfile.write(reversed_content)

def copy_file(input_path, output_path):
    with open(input_path, 'r') as infile:
        content = infile.read()
    with open(output_path, 'w') as outfile:
        outfile.write(content)

def duplicate_contents(input_path, n):
    with open(input_path, 'r') as infile:
        content = infile.read()
    duplicated_content = content * int(n)
    with open(input_path, 'w') as outfile:
        outfile.write(duplicated_content)  

def replace_string(input_path, needle, newstring):
    with open(input_path, 'r') as infile:
        content = infile.read()
    replaced_content = content.replace(needle, newstring)
    with open(input_path, 'w') as outfile:
        outfile.write(replaced_content)  


def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: python file_manipulator.py [command] [args...]")
        sys.exit(1)

    command = args[0]

    if command == 'reverse' and len(args) == 3:
        validate_file(args[1])
        reverse_file(args[1], args[2])
    
    elif command == 'copy' and len(args) == 3:
        validate_file(args[1])
        copy_file(args[1], args[2])
    
    elif command == 'duplicate-contents' and len(args) == 3:
        validate_file(args[1])
        duplicate_contents(args[1], args[2])
    
    elif command == 'replace-string' and len(args) == 4:
        validate_file(args[1])
        replace_string(args[1], args[2], args[3])
    
    else:
        print("Invalid command or arguments.")
        sys.exit(1)
    
if __name__ == "__main__":
    main()
