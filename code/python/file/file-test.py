#!/usr/bin/env python

fname = 'test'

# \n include
with open(fname) as f:
	content = f.readlines()

# no \n include
with open(fname) as f:
	content = f.read().splitlines()

with open(fname) as f:
	for line in f:
		print line
