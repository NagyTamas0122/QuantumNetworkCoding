import sys
from tests.test_connection import test_connection

def main() -> int:

    test_connection()

    return 0

if __name__ == '__main__':
    sys.exit(main())