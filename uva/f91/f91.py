# UVa: f91

from sys import stdin

def f91(n):
    return n - 10 if n >= 101 else f91(f91(n + 11))

for test_case in map(int, stdin.read().split()):
    if not test_case:
        break
    print(f"f91({test_case}) = {f91(test_case)}")