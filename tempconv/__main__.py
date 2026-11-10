import sys

from tempconv.core import convert


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    value, src, dst = float(argv[0]), argv[1], argv[2]
    print(convert(value, src, dst))
    return 0


if __name__ == "__main__":
    sys.exit(main())
