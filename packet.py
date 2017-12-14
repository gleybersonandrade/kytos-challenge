"""Defines Packet classes and related items."""

# System imports
from enum import IntEnum

class Type(IntEnum):
    """Enumeration of Packet Types."""

    OFPT_HELLO = 0
    OFPT_ERROR = 1
    OFPT_ECHO_REQUEST = 2
    OFPT_ECHO_REPLY = 3
    OFPT_VENDOR = 4
    OFPT_FEATURES_REQUEST = 5
    OFPT_FEATURES_REPLY = 6
    OFPT_GET_CONFIG_REQUEST = 7
    OFPT_GET_CONFIG_REPLY = 8
    OFPT_SET_CONFIG = 9
    OFPT_PACKET_IN = 10
    OFPT_FLOW_REMOVED = 11
    OFPT_PORT_STATUS = 12
    OFPT_PACKET_OUT = 13
    OFPT_FLOW_MOD = 14
    OFPT_PORT_MOD = 15
    OFPT_STATS_REQUEST = 16
    OFPT_STATS_REPLY = 17
    OFPT_BARRIER_REQUEST = 18
    OFPT_BARRIER_REPLY = 19
    OFPT_QUEUE_GET_CONFIG_REQUEST = 20
    OFPT_QUEUE_GET_CONFIG_REPLY = 21

class Packet(object):
    """Representation of an OpenFlow Packet."""

    def __init__(self, header, buffer_id = None, total_len = None, in_port = None, reason = None, pad = None, data = None):
        """Create a Packet with the optional parameters below."""
        self._header = header
        self._buffer_id = buffer_id
        self._total_len = total_len
        self._in_port = in_port
        self._reason = reason
        self._pad = pad
        self._data = data

class Header(object):
    """Representation of an OpenFlow Packet Header."""

    def __init__(self, version, type, length, xid):
        """Create a Header with the parameters below."""
        self._version = version
        self._type = type
        self._length = length
        self._xid = xid

    @property
    def content(self):
        """Describes the packet header content."""
        version = "Version: 0X0" + str(self._version)
        for packet_type in Type:
            if (packet_type.value == self._type):
                type = "Type: " + str(packet_type.name)
                break
        length = "Length: " + str(self._length)
        xid = "Transaction ID: " + str(self._xid)
        return "Header\n\t%s \n\t%s \n\t%s \n\t%s\n" % (version, type, length, xid)
