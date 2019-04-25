#!/usr/bin/env python3

import hashlib
import string

HASHFILE = "/Users/robertnash/Comp_Sci/389Rspring19/assignments/9_Crypto_I/hashes.txt"
PASSFILE = "/Users/robertnash/Comp_Sci/389Rspring19/assignments/9_Crypto_I/passwords.txt"


def crack():
    hashes = open(HASHFILE, 'r').read().splitlines()
    passwords = open(PASSFILE, 'r').read().splitlines()
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:

            salted_pass = c + p
            digest = hashlib.sha256(salted_pass).hexdigest()

            for h in hashes:
               if h == digest:
                    print(p + ":" + h)


if __name__ == "__main__":
    crack()
