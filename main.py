import sys
from tests.test_connection import test_connection
from tests.test_connection_fanout import test_connection_fanout
from tests.test_connection_add import test_connection_add
from tests.test_removal import test_removal
from tests.test_removal_add import test_removal_add
from tests.test_encoding import test_encoding
from tests.test_encoding_2_2 import test_encoding_2_2

def main() -> int:

    #test_connection()
    #test_connection_fanout()
    #test_connection_add()
    #test_removal()
    #test_removal_add()
    #test_encoding()
    test_encoding_2_2()

    return 0

if __name__ == '__main__':
    sys.exit(main())