"""
This file contains methods and utilities for creating a raw TCP connection which uses the proxy protocol
"""
import socket

from pyproxy.const import PROTOCOL_V1, PROTOCOL_V2
import pyproxy.encode

class ProxyProtocolSocket(socket.socket):
    """
    Wrapper for native python sockets which will speak proxy protocol v1 or v2 to the receiver
    """

    def __init__(self, pp_version, family=socket.AF_INET, type=socket.SOCK_STREAM, src_addr=None):
        """
        :param pp_version:  Proxy protocol version to use, constant from const.py
        :param kwargs:      Any additional parameters passed to socket constructor
        """
        if pp_version not in (PROTOCOL_V1, PROTOCOL_V2):
            raise ValueError('Invalid version {}'.format(pp_version))

        self.proxy_version = pp_version
        self.src_address = src_addr
        super(ProxyProtocolSocket, self).__init__(family, type)

    def connect(self, address):
        """
        Initiate a connection to address

        :param address:     Tuple describing the address to connect to
        """
        super(ProxyProtocolSocket, self).connect(address)

        peer_address = self.getpeername()
        if not self.src_address:
            self.src_address = self.getsockname()
        
        # Send Proxy Protocol Header
        header = pyproxy.encode.encode_v1('TCP4', self.src_address[0], peer_address[0], self.src_address[1], peer_address[1])
        amt_sent = 0
        while amt_sent < len(header):
            amt_sent += self.send(header[amt_sent:])

