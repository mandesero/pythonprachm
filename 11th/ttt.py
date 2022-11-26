import sys

print(bytes.fromhex(sys.stdin.read()).decode('utf-8'))