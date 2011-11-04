#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def main():    
    here = os.path.abspath(os.path.dirname(__file__))
    for root, dirs, files in os.walk(here):
        for f in files:
            if f.endswith(('.pyc', '.orig', '.log', '.swp', '~')):
                full = os.path.join(root, f)
                print full
                os.remove(full)
    return 0

if __name__ == '__main__':
    main()

