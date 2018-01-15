#!/usr/bin/python

import os
import subprocess
import sys

def dumpOut(tables, pargs):
	print("Dumping SDE into files...")
	for table in tables:
		tableToFile(table, pargs["-d"] + table + ".sdex", pargs["-u"], pargs["-p"])

def tableToFile(table, dumpfile, user, passwd):
	print("Dump table " + table) 
	subprocess.call("sdeexport -o create -t " + table + " -f " + dumpfile + " -u " + user + " -p " + passwd, shell=True) 

def dumpIn(dir, pargs):
	print ("Importing into SDE...")
	
	if not dir.endswith("/"):
		dir = dir + "/"

	for file in [file for file in os.listdir(dir) if file.lower().endswith(".sdex")]:
		fileToTable(file[:-5], dir + file, pargs['-u'], pargs['-p'])

def fileToTable(table, file, user, passwd):
	print("Read dump " + file + " to table " + table + "...")
	subprocess.call("sdeimport -o create -t " + table + " -f " + file + " -u " + user + " -p " + passwd, shell=True)

def printArgs():
	print("""dumpsde.py usage:

	dumpsde out <table0,table1,..> [options]
		-d <export directory>  default: current working directory
		-u <sde username>      default: sde 
		-p <sde password>      default: sde

	dumpsde in <directory with sdex files> [options] 
		-u <sde username>      default: sde
		-p <sde password>      default: sde
""")

def defaultArgs():
	pargs = {}
	pargs["-d"] = "./"
	pargs["-p"] = "sde"
	pargs["-u"] = "sde"
	return pargs

def parseArgs(args):
	pargs = defaultArgs()

	key = None
	val = None
	for arg in args:
		if key == None:
			key = arg
		elif val == None:
			val = arg
		else:
			pargs[key] = val
			key = val = None

	return pargs


if len(sys.argv) > 2:
	operation = sys.argv[1];
	pargs = parseArgs(sys.argv[3:])

	if operation == "out":
		tables = sys.argv[2].split(',')
		dumpOut(tables, pargs)
	elif operation == "in":
		dumpIn(sys.argv[2], pargs)
else:
	printArgs()
