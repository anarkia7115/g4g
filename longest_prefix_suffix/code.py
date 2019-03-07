#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():

    sys.stdin.readline()
    # loop every line
    for l in sys.stdin:
        l = l.strip()
        # print(l)
        lps = 0  # init lps
        curr_prefix = ""  # init prefix
        # loop every char
        for ch in l[:-1]:
            curr_prefix += ch

            # curr prefix length
            i = len(curr_prefix)

            # check match suffix
            if l[-i:] == curr_prefix:
                lps = i  # record lps

        # print lps
        print(lps)


if __name__ == "__main__":
    main()