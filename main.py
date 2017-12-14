"""kytos-challenge main function."""

# System imports
import sys

# Local imports
from utils import *

if __name__ == "__main__":
    packet = unpack_packet('raw/ofpt_hello.dat')
    sys.stdout.write(packet._header.content)
