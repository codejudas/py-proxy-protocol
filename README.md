py-proxy-protocol
-----------------

A simple library to speak [proxy-protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) in your python app with minimal headaches.
Why proxy-protocol? Its the `X-Forwarded-For` of TCP connections, its used by TCP proxies like HAProxy and Amazon NLBs, wouldn't it be nice if we could talk to those things?

**Note:** Current functionality is focused on the client side or the side that initiates the connection and sends their identity over proxy protocol. Future work may expand to include the server side and receiving this proxy protocol information however it is of lower priority because typically a reverse-proxy that understands proxy protocol would sit in front of your app like Nginx or HAProxy.

### Feature Set

Current features provided by the library:
- Create a socket that speaks Proxy Protocol V1 to the receiving end.

Future features:
- Create a socket that speaks Proxy Protocol V2 (binary)

### Installation

```
$ pip install py-proxy-protocol
...
```

And watch as nothing happens as this package is not published on pypi yet.
