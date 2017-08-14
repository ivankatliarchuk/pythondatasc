#!/usr/bin/env python

import re

# Aug 14 08:41:25 ivanka-virt sshd[923]: Server listening on 0.0.0.0 port 22.
line = 'Aug 14 08:41:25 ivanka-virt sshd[923]: Server listening on 0.0.0.0 port 22.'
pattern = '''[A-Z][a-z]{2}\s{1,2}\d{2}\s{1,2}\d{2}:\d{2}:\d{2}\s{1,2}\w*-\w*\s{1,2}sshd\[\d*\]:\s{1,2}Server listening on \d{1,2}.\d{1,2}.\d{1,2}.\d{1,2}\s{1,2}'''
match = re.search(pattern=pattern, string=line)

print match.group(0)

pattern = '^(.*?)\s(\w+)\s(\w+):.*?Server\slist.*?on.*$'
match = re.search(pattern, line)

print match.groups()
