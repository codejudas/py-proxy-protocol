import pyproxy
from pyproxy.socket import ProxyProtocolSocket

sock = ProxyProtocolSocket(pyproxy.const.PROTOCOL_V1, src_addr=('9.9.9.9', 69))
sock.connect(('127.0.0.1', 81))
sock.send("""GET /test HTTP/1.0
Host: nothing.com


""".encode('ascii'))

res = sock.recv(4096)
print(res)
