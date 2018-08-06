import unittest
from mock import Mock

from pyproxy.encode import encode_v1
from pyproxy.const import PROXY_PROTOCOL
from pyproxy.socket import ProxyProtocolSocket


class BaseProxyProtocolSocketTest(unittest.TestCase):

    def get_socket(self, version, src_addr=None):
        """Helper to return a ProxyProtocolSocket with appropriate methods mocked out"""
        socket = ProxyProtocolSocket(version, src_addr=src_addr)
        socket.sendall = Mock(name='mock-sendall')
        socket.send = Mock(name='mock-send')
        socket.getpeername = Mock(name='mock-getpeername')
        socket.getsockname = Mock(name='mock-getsockname')
        return socket


class ProxyProtocolSocketConstructorTest(BaseProxyProtocolSocketTest):
    def test_constructor_invalid_version(self):
        with self.assertRaises(ValueError) as exc:
            self.get_socket('fake-version')

        self.assertEqual('Invalid version "fake-version"', exc.exception.message)

    def test_constructor_invalid_src_addr(self):
        with self.assertRaises(ValueError) as exc:
            self.get_socket(PROXY_PROTOCOL.V1, src_addr='1.1.1.1')

        self.assertEqual('Invalid src_addr "1.1.1.1". Must be tuple of form (ip, port).',
                         exc.exception.message)

        with self.assertRaises(ValueError) as exc:
            self.get_socket(PROXY_PROTOCOL.V1, src_addr=('1.1.1.1', '2.2.2.2', 3))

        self.assertEqual('Invalid src_addr "(\'1.1.1.1\', \'2.2.2.2\', 3)". Must be tuple of form '
                         '(ip, port).', exc.exception.message)

        with self.assertRaises(ValueError) as exc:
            self.get_socket(PROXY_PROTOCOL.V1, src_addr=('1.1.1.1',))

        self.assertEqual('Invalid src_addr "(\'1.1.1.1\',)". Must be tuple of form (ip, port).',
                         exc.exception.message)

    def test_constructor_invalid_port(self):
        with self.assertRaises(ValueError) as exc:
            self.get_socket(PROXY_PROTOCOL.V1, src_addr=('1.1.1.1', 'port'))

        self.assertEqual('Invalid port "port" provided in src_addr. Must be an integer.',
                         exc.exception.message)

    def test_constructor_v1(self):
        socket = self.get_socket(PROXY_PROTOCOL.V1)

        self.assertEqual(PROXY_PROTOCOL.V1, socket.proxy_version)

    def test_constructor_v1_with_src_addr(self):
        socket = self.get_socket(PROXY_PROTOCOL.V1, src_addr=('1.1.1.1', 100))

        self.assertEqual(PROXY_PROTOCOL.V1, socket.proxy_version)
        self.assertEqual('1.1.1.1', socket.pp_src_ip)
        self.assertEqual(100, socket.pp_src_port)

    def test_constructor_v2(self):
        socket = self.get_socket(PROXY_PROTOCOL.V2, src_addr=('2.2.2.2', 200))

        self.assertEqual(PROXY_PROTOCOL.V2, socket.proxy_version)
        self.assertEqual('2.2.2.2', socket.pp_src_ip)
        self.assertEqual(200, socket.pp_src_port)


class ProxyProtocolSocketHeaderTest(BaseProxyProtocolSocketTest):
    def test_send_pp_header_v1_no_src_addr(self):
        """Test sending pp header with default src addr provided by socket"""
        socket = self.get_socket(PROXY_PROTOCOL.V1)
        socket.getsockname.return_value = ('1.1.1.1', 1000)
        socket.getpeername.return_value = ('2.2.2.2', 2000)

        socket._send_pp_header()

        expected_header = encode_v1('TCP4', '1.1.1.1', '2.2.2.2', 1000, 2000)
        socket.sendall.assert_called_once_with(expected_header)

    def test_send_pp_header_v1_with_src_addr(self):
        """Test sending pp header with user provided src addr"""
        socket = self.get_socket(PROXY_PROTOCOL.V1, src_addr=('6.6.6.6', 666))
        socket.getsockname.return_value = ('1.1.1.1', 1000)
        socket.getpeername.return_value = ('2.2.2.2', 2000)

        socket._send_pp_header()

        expected_header = encode_v1('TCP4', '6.6.6.6', '2.2.2.2', 666, 2000)
        socket.sendall.assert_called_once_with(expected_header)
