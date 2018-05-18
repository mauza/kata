
import base64
import gzip

with open('../data/gpsBase64Gzip','r') as f:
    with open('../data/output', 'wb') as w:
        base64.decode(f, w)

with gzip.open('../data/output', 'rb') as f:
    file_content = f.read()
    with open('../data/output', 'wb') as w:
        w.write(file_content)

