#!/usr/bin/python3
for a in range(0, 8):
    for b in range(a + 1, 10):
        print(f"{a:d}{b:d}", end=", ")
print(f"{a + 1:d}{b:d}")

