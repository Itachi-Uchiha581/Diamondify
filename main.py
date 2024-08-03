import argparse
import os
from diamondify import Diamondify


def main():
    parser = argparse.ArgumentParser(
        prog="Diamondify",
        description="Ever wrote that code that you knew was so trash that it burnt your eyes open? Ya, Diamondify fixes that",
        epilog="Make your code shine like a diamond!"
    )

    # Input group
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-f", "--file", help="Input file to process")
    input_group.add_argument("-d", "--directory", help="Input directory to process")

    # Output is optional with a default value
    parser.add_argument("-o", "--output", default="./output", help="Output directory (default: ./output)")

    # Model is always required
    parser.add_argument("-m", "--model", help="Model to use for processing", default="gpt-4o")

    args = parser.parse_args()

    # Check if the output is a file
    if os.path.isfile(args.output) or '.' in os.path.basename(args.output):
        parser.error("Output must be a directory, not a file")

    # Ensure output is a directory
    os.makedirs(args.output, exist_ok=True)

    # Check if the input exists
    if args.file:
        if not os.path.isfile(args.file):
            parser.error(f"Input file does not exist: {args.file}")
    elif args.directory:
        if not os.path.isdir(args.directory):
            parser.error(f"Input directory does not exist: {args.directory}")

    # Your main logic here
    if args.file:
        cleaner = Diamondify(args.model, args.file, args.output, True)
        cleaner()
    else:
        cleaner = Diamondify(args.model, args.file, args.output, False)
        cleaner()


if _name_ == "_main_":
    main()