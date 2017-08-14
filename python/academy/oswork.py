#!/usr/bin/env python

import platform

print platform.linux_distribution()
print platform.version()

sys_info = ' '.join(platform.linux_distribution())
print sys_info

import subprocess

df_cmd = subprocess.check_output(['df', '-k'])
print df_cmd

users = {}
ps_cmd = subprocess.check_output(['ps', '-ef'])

for line in ps_cmd.splitlines()[1:]:
    user = line.split()[0]
    if users.get(user):
        users[user] += 1
    else:
        users[user] = 1
else:
    print users

for user, process_count in users.items():
    print "{} is running {} processes".format(user, process_count)

print '----'

for line in subprocess.check_output('ps -ef', shell=True).splitlines()[1:]:
    print line

print '----'

try:
    subprocess.check_output(['k'])
except Exception as e:
    print "A {} exception happended because {}".format(type(e).__name__, e.args)
else:
    print 'All good'


















