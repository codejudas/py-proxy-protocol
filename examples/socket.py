import pyproxy
from pyproxy.socket import ProxyProtocolSocket

SERVER_HOST = '9.9.9.9'
SERVER_PORT = 9000

# Create a new socket that speaks proxy protocol
sock = ProxyProtocolSocket(pyproxy.const.PROTOCOL_V1, src_addr=(SERVER_HOST, SERVER_PORT))

# Connect to it - This sends the proxy protocol header
sock.connect(('127.0.0.1', 81))

# Send data as usual
sock.send("""GET /test HTTP/1.0
Host: nothing.com


""".encode('ascii'))

# Receive a response
res = sock.recv(4096)
print(res)
