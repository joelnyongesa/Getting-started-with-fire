#!/usr/bin/env python3

import fire

class Calculator(object):
    def add(self, x, y):
        return x+y
    def multiply(self, x, y):
        return x*y
    
if __name__ == "__main__":
    fire.Fire(Calculator)