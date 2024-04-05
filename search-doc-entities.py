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

def fn_declarations(file_contents):
	functions = set()
	for match in re.findall(r'fn_[_A-Za-z0-9]*\s*=', file_contents):
		functions.add(re.sub(r'\s*=','',match))

	return functions

def var_declarations(file_contents):
	vars = set()
	for match in re.findall(r'[\.A-Z]+[_A-Z0-9]*\s*[:\?]*=', file_contents):
		vars.add(re.sub(r'\s*[:\?]*=','',match))

	return vars

def var_uses(file_contents):
	vars = set()
	for match in re.findall(r'\$\([\.A-Z]+[_A-Z0-9]*\)', file_contents):
		vars.add(re.sub(r'\$\(|\)','',match))

	return vars

entities = set()
for makefile in list_makefiles(dir):
	file_contents = file_to_string(makefile)
	for var in var_declarations(file_contents):
		entities.add(var)

	for var in var_uses(file_contents):
		entities.add(var)

	for fn in fn_declarations(file_contents):
		entities.add(fn)

entities.discard("OS")
entities.discard("OUTPUT_DIRECTORY")
entities.discard("PROCESSOR_ARCHITECTURE")
entities.discard(".SHELLSTATUS")
entities.discard("MAKEFILE_LIST")
entities.discard(".DEFAULT_GOAL")
entities.discard("MAKE_RESTARTS")
entities.discard("MAKE_TERMOUT")
entities.discard("MAKE_TERMERR")
entities.discard(".RECIPEPREFIX")
entities.discard(".VARIABLES")
entities.discard(".FEATURES")
entities.discard(".INCLUDE_DIRS")
entities.discard(".EXTRA_PREREQS")
entities.discard("MAKEFILES")
entities.discard("VPATH")
entities.discard("SHELL")
entities.discard("MAKESHELL")
entities.discard("MAKE")
entities.discard("MAKE_VERSION")
entities.discard("MAKE_HOST")
entities.discard("MAKELEVEL")
entities.discard("MAKEFLAGS")
entities.discard("GNUMAKEFLAGS")
entities.discard("MAKECMDGOALS")
entities.discard("CURDIR")
entities.discard("SUFFIXES")
entities.discard(".LIBPATTERNS")

entities = sorted(entities)
for entity in entities:
	print(entity)
