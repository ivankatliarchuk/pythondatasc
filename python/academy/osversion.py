#!/usr/bin/env python

import platform

print platform.linux_distribution()
print platform.version()

sys_info = ' '.join(platform.linux_distribution())
print sys_info
print dict(platform)