"""Helper kytos-challenge functions."""

# System imports
from struct import *

# Local imports
from packet import *

def unpack_header(bytes):
    """Unpack packet header content."""
    header = unpack('>BBHI', bytes)
    return header[0], header[1], header[2], header[3]

def unpack_packet(packet_name):
    """Unpack packet content."""
    f = open(packet_name, 'rb')
    version, type, length, xid = unpack_header(f.read(8))
    header = Header(version, type, length, xid)
    packet = Packet(header)
    return packet
