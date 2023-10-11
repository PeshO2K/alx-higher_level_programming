#!/usr/bin/python3
"""
Module docs
"""


def print_stats(total_size, code_dict):
    print("File size: {:d}".format(total_size))
    for c in sorted(code_dict):
        print("{}: {}".format(c, code_dict[c]))


if __name__ == '__main__':
    from sys import stdin

    code_dict = {}
    total_size = 0
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    i = 0
    try:
        for line in stdin:
            stripped = line.split()
            if len(stripped) < 2:
                continue
            try:
                total_size += int(stripped[-1])
                code = int(stripped[-2])
                if code in valid_codes:
                    code_dict[code] = code_dict.get(code, 0) + 1
            except ValueError:
                pass

            i += 1
            if i % 10 == 0:
                print_stats(total_size, code_dict)
        print_stats(total_size, code_dict)
    except KeyboardInterrupt:
        print_stats(total_size, code_dict)
        raise
