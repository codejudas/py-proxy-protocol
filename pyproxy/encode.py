"""
This file contains methods and utilities for encoding a proxy protocol header
"""

def encode_v1(protocol, src_ip, dst_ip, src_port, dst_port):
    """
    Produce a Proxy Protocol V1 connection header according to https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt

    :param protocol: str one of TCP4, TCP6, UNKNOWN
    :param src_ip: str the ip address of the sender, either ipv4 or ipv6
    :param dst_ip: str the ip address of the receiver, either ipv4 or ipv6
    :param src_port: int the port of the receiver
    :param dst_port: int the port of the sender
    :returns binary string header in proxy protocol v1 format to send upon establishing a connection.
    """
    protocol = protocol.upper()
    assert protocol in ('TCP4', 'TCP6', 'UNKNOWN'), 'Unknown protocol {}'.format(protocol)
    header = 'PROXY {prot} {src_ip} {dst_ip} {src_port} {dst_port}\r\n'.format(
        prot=protocol,
        src_ip=src_ip,
        dst_ip=dst_ip,
        src_port=src_port,
        dst_port=dst_port,
    )
    return header.encode('ascii')


