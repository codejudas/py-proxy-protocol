import unittest

from pyproxy.const import PROXY_PROTOCOL
from pyproxy.socket import ProxyProtocolSocket

from tests.integration import TestStreamServer


class ProxyProtocolV1SocketTest(unittest.TestCase):
    def setUp(self):
        self.mock_server = TestStreamServer()
        self.mock_server.start()
        print('Test server running on {}:{}'.format(
            self.mock_server.server_host, self.mock_server.server_port
        ))

        self.socket = ProxyProtocolSocket(PROXY_PROTOCOL.V1, src_addr=('1.1.1.1', 1000))

    def tearDown(self):
        # self.mock_server.stop()
        self.mock_server.join(timeout=0.1)
        self.socket.close()

    @property
    def mock_server_address(self):
        return (self.mock_server.server_host, self.mock_server.server_port)

    def test_proxy_protocol_v1(self):
        self.socket.connect(self.mock_server_address)
        resp = self.socket.recv(1024)

        self.assertEqual(
            'PROXY TCP4 1.1.1.1 127.0.0.1 1000 {}'.format(self.mock_server.server_port),
            resp
        )

        self.socket.sendall('Hello world')
        resp = self.socket.recv(1024)
        self.assertEqual('Hello world', resp)
