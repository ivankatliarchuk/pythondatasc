#!/usr/bin/env python

import time
import urllib2

def elapsed_time_dec(function_to_time):
    def wrapper(*args, **kw):
        print args
        print kw
        t0 = time.time()
        function_to_time(*args)
        t1 = time.time()
        print "Elapsed time: {}".format(t1 - t0)
    return wrapper

@elapsed_time_dec
def downloadn_webpage(value):
    url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
    response = urllib2.urlopen(url, timeout=20)
    return response.read()

def elapsed_time():
    t0 = time.time()
    webpage = downloadn_webpage()
    print webpage
    t1 = time.time()
    print "Elapsed time: {}".format(t1 - t0)


downloadn_webpage(4)


