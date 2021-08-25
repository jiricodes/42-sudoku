#! /usr/bin/python3

import sys
def parse_input(input):
	pass

def parse_output(output):
	pass

def read_lines(filename):
	file = open(filename, 'r')
	lines = file.readlines()
	file.close()
	return lines

def main():
	filename=sys.argv[1]
	mode=sys.argv[2]

	raw_input=read_lines(filename)
	if mode == "in":
	elif mode == "out":

	else:
		print("Wrong mode")
		exit()
	

if __name__ == "__main__":
	main()