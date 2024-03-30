#!/bin/python3

import re
import os
import sys

dir = "."
if len(sys.argv) > 1:
	dir = sys.argv[1]

def file_to_string(file):
	with open(file) as file:
		return file.read()

def list_makefiles(dir):
	makefiles = []
	for currentpath, folders, files in os.walk(dir):
		for file in files:
			if file.endswith(".mk"):
				makefiles.append(os.path.join(currentpath, file))

	return makefiles

def var_declarations(str):
	vars = set()
	for match in re.findall(r'[\.A-Z]+[_A-Z0-9]*\s*[:\?]*=', str):
		vars.add(re.sub(r'\s*[:\?]*=','',match))

	return vars

def var_uses(str):
	vars = set()
	for match in re.findall(r'\$\([\.A-Z]+[_A-Z0-9]*\)', str):
		vars.add(re.sub(r'\$\(|\)','',match))

	return vars

vars = set()
for makefile in list_makefiles(dir):
	file_contents = file_to_string(makefile)
	for var in var_declarations(file_contents):
		vars.add(var)

	for var in var_uses(file_contents):
		vars.add(var)

vars.discard("OS")
vars.discard("OUTPUT_DIRECTORY")
vars.discard("PROCESSOR_ARCHITECTURE")
vars.discard(".SHELLSTATUS")
vars.discard("MAKEFILE_LIST")
vars.discard(".DEFAULT_GOAL")
vars.discard("MAKE_RESTARTS")
vars.discard("MAKE_TERMOUT")
vars.discard("MAKE_TERMERR")
vars.discard(".RECIPEPREFIX")
vars.discard(".VARIABLES")
vars.discard(".FEATURES")
vars.discard(".INCLUDE_DIRS")
vars.discard(".EXTRA_PREREQS")
vars.discard("MAKEFILES")
vars.discard("VPATH")
vars.discard("SHELL")
vars.discard("MAKESHELL")
vars.discard("MAKE")
vars.discard("MAKE_VERSION")
vars.discard("MAKE_HOST")
vars.discard("MAKELEVEL")
vars.discard("MAKEFLAGS")
vars.discard("GNUMAKEFLAGS")
vars.discard("MAKECMDGOALS")
vars.discard("CURDIR")
vars.discard("SUFFIXES")
vars.discard(".LIBPATTERNS")

vars = sorted(vars)
for var in vars:
	print(var)
