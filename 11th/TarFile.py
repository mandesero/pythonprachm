import sys, tarfile
from io import BytesIO

buff = bytes.fromhex(sys.stdin.read().replace(' ', '').replace('\n', ''))
stream = BytesIO(buff)

with tarfile.open(fileobj=stream) as tar:
    files = [file for file in tar.getmembers() if file.isfile()]
    print(sum(map(lambda x: x.size, files)), len(files))
