
import re
import sys

def main():
	m = re.search('(?<=abc)def', 'abcdef')
	m.group(0)