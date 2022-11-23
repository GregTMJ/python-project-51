#!/usr/bin/env python
import logging
import sys

from page_loader import download
from page_loader.cli import parse_args

logging.basicConfig(level=logging.INFO)


def main():
    """
    Main function that starts our project's scripts
    """
    args = parse_args()

    try:
        file_path = download(args.url, args.output)
        print(f"Downloaded to your computer as {file_path}")
    except Exception as e:
        logging.error(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
