#!/usr/python3.6.0/bin/python3.6

# -*- coding: utf-8 -*-
import re
import sys

from scrapy.cmdline import execute

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])

    args = [sys.argv[0], "crawl", "zongheng"]

    sys.exit(execute(args))
# coding = utf-8
