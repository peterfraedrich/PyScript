#!/usr/bin/env python

import sys
from datetime import datetime

class doSomething:
    def __init__ (self, var):
        self.variable = var 
        return

    def get(self):
        return self.variable


def main():
    d = doSomething("hello")
    print d.get()
    return

if __name__ == '__main__':
    main()
