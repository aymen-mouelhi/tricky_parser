import argparse
from parser import TrickyParser

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple parser for web data files')
    parser.add_argument("--filepath", required=True, type=str, help="Your file")
    parser.add_argument("--output_folder", default=".", type=str, help="The folder in which you would like to store "
                                                                       "your cleaned files")
    parser.add_argument("--output_format", default="csv", type=str, choices=["csv", "json", "excel"],
                        help="The format of the generated files")

    args = parser.parse_args()

    parser = TrickyParser(args.filepath, args.output_folder, args.output_format)
    parser.generate_clean_files()
