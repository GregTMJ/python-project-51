#!/usr/bin/env python
import sys

from page_loader import download
from page_loader.cli import parse_args


def main():
    """
    Main function that starts our project's scripts
    """
    args = parse_args()

    try:
        file_path = download(args.url, args.output)

    except Exception:
        sys.exit(1)


if __name__ == '__main__':
    main()
