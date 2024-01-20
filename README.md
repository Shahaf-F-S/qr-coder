# QR-Coder

> A QR handling module for writing and reading QR.

## Installation:

```
pip install qr-coder
```

## example

```python
from qrcoder import encode, decode

data = "hello world"

print(data == decode(encode(data.encode())).decode())
```