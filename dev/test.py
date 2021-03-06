#!/usr/bin/env python2.7

import sys
import os.path
dev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, dev_path)

import logging
_logger = logging.getLogger()
_logger.setLevel(logging.DEBUG)
logging.getLogger('boto').setLevel(logging.INFO)

ch = logging.StreamHandler()

FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(FMT)
ch.setFormatter(formatter)
_logger.addHandler(ch)

import svn.local
import svn.remote
import pprint

#r = svn.remote.RemoteClient('https://opsvn.openpeak.com/svn/adam2/trunk')
#r = svn.local.LocalClient('/Users/dustin/development/php/adam2')
r = svn.local.LocalClient('working_copy')
pprint.pprint(r.info())

#print(r.cat('sfs/package/DEBIAN/postinst'))

#import dateutil.parser
#import datetime
#
#from_ = datetime.datetime.now().replace(day=21)
#for e in r.log_default(timestamp_from_dt=from_):
#    print(e)
#
#sys.exit(0)

#i = r.info()
#print(i)
sys.exit(0)

print(i.attrib['kind'])
print(i.attrib['path'])
print(i.attrib['revision'])

print(i.find('url').text)
print(i.find('relative-url').text)

repo = i.find('repository')
print(repo.find('root').text)
print(repo.find('uuid').text)

commit = i.find('commit')
print(commit.find('author').text)
print(commit.find('date').text)

#print(r.info().items())
#print(r.info().getchildren())

#import pprint
#pprint.pprint(r.info())

#r.checkout('/tmp/checkout_2')
#r.export('/tmp/export_1')

#l = svn.local.LocalClient('/Users/dustin/development/php/adam2')
