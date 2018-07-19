import unittest
from pyproxy.encode import encode_v1

class EncodeV1Test(unittest.TestCase):

    def test_encodes_exact_bytes(self):
        header = encode_v1('TCP4', '1.1.1.1', '2.2.2.2', 1000, 80)
        expected_header =  b'\x50\x52\x4F\x58\x59'              # 'PROXY'
        expected_header =  b'\x20'
        expected_header += b'\x54\x43\x50\x34\x20'              # 'TCP4'
        expected_header =  b'\x20'
        expected_header += b'\x31\x2e\x31\x2e\x31\x2e\x31\x20'  # '1.1.1.1'
        expected_header =  b'\x20'
        expected_header += b'\x32\x2e\x32\x2e\x32\x2e\x32\x20'  # '2.2.2.2'
        expected_header =  b'\x20'
        expected_header += b'\x31\x30\x30\x30\x20'              # '1000'
        expected_header =  b'\x20'
        expected_header += b'\x38\x30'                          # '1000'
        expected_header += b'\x0d\x0a'                          # '\r\n'

        self.assertEquals(expected_header, header)
