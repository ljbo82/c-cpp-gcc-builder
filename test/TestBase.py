# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import subprocess
import os
import shutil
import unittest
import functools

DIR = os.path.abspath(os.path.dirname(__file__))

class TestBase(unittest.TestCase):

	@property
	def cwd(self):
		try:
			return self.__cwd
		except:
			cwd = os.path.abspath(os.path.join(DIR, '.'))
			os.chdir(cwd)
			self.__cwd = cwd
			return cwd

	@cwd.setter
	def cwd(self, cwd):
		cwd = os.path.abspath(os.path.join(self.cwd, cwd))
		os.chdir(cwd)
		self.__cwd = cwd

	def BuildTest(output_dir='output', cwd=None):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(self):
				oldCwd = self.cwd
				if cwd is not None:
					self.cwd = cwd

				if output_dir is not None and os.path.exists(output_dir):
					shutil.rmtree(output_dir, True)

				try:
					func(self)
				finally:
					if output_dir is not None and os.path.exists(output_dir):
						shutil.rmtree(output_dir, True)

					if cwd is not None:
						self.cwd = oldCwd

			return wrapper

		if callable(output_dir):
			decorator = TestBase.BuildTest('output', None)
			return decorator(output_dir)

		return decorator

	@staticmethod
	def __run_command(command):
		return subprocess.run(\
			command, \
			capture_output = True, \
			text = True,\
			shell = True)

	def make(self, make_flags=None, env=None):
		make_command = f"{'' if env is None else env + ' '}make{'' if make_flags is None else ' ' + make_flags}"
		class Result:
			def __init__(self, core_result):
				self.exitCode = core_result.returncode
				self.output = (core_result.stdout if core_result.returncode == 0 else core_result.stderr).strip().split('\n')

		return Result(self.__run_command(make_command))

	@staticmethod
	def find_line(find, lines):
		'''
		Returns the index of the first line containing a given string.

		Args:
			find (str): String to be searched.
			lines (list): List of lines to be inspected.

		Returns:
			The index of the first line containing seached string. If
			searched line is not found, returns -1
		'''
		index = 0
		for line in lines:
			if find in line:
				return index

			index += 1

		return -1

	@staticmethod
	def assert_find_line(find, lines):
		line = TestBase.find_line(find, lines)
		if line == -1:
			raise AssertionError(f"{repr(find)} was NOT found")

		return line

	@staticmethod
	def contains(what, where, find_all=None, find_any=None):
		'''
		Checks if a string is found in another string or inside a list of strings

		Args:
			what(str or a list): searched value(s). Passing a list means that
			all entries should be found.

			where(str or list): Inspected values.

		Returns:
			True if string was found. Otherwise, returns False.
		'''
		if find_all is not None and find_any is not None:
			raise ValueError('find_all and find_any defined together')

		if find_all is not None:
			find_any = not find_all

		if find_any is not None:
			find_all = not find_any

		if find_all is None:
			find_all = True

		if find_any is None:
			find_any = False

		if not isinstance(where, list):
			whereEntries = [where]
		else:
			whereEntries = where

		if not isinstance(what, list):
			whatEntries = [what]
		else:
			whatEntries = what

		found = False
		for whatEntry in whatEntries:
			found = False

			for whereEntry in whereEntries:
				if whatEntry in whereEntry:
					found = True
					break

			if not found and find_all:
				return (False, whatEntry)

			if found and find_any:
				return (True, whatEntry)

		return (found, what)

	@staticmethod
	def assert_contains(what, where):
		result = TestBase.contains(what, where, find_all=True)
		if not result[0]:
			raise AssertionError(f"{repr(result[1])} was NOT found")

	@staticmethod
	def assert_not_contains(what, where):
		result = TestBase.contains(what, where, find_any=True)
		if result[0]:
			raise AssertionError(f"{repr(result[1])} was FOUND")

	@staticmethod
	def assert_var_error(varName, varMessage, result):
		if result.exitCode == 0:
			raise AssertionError("Execution succeeded")

		TestBase.assert_contains(f'[{varName}] {varMessage}', result.output)

	@staticmethod
	def assert_missing_value(varName, result):
		TestBase.assert_var_error(varName, 'Missing value', result)

	@staticmethod
	def assert_unexpected_origin(varName, givenOrigin, result):
		TestBase.assert_var_error(varName, f'Unexpected origin: "{givenOrigin}"', result)

	@staticmethod
	def assert_no_whitespaces(varName, result):
		TestBase.assert_var_error(varName, 'Value cannot have whitespaces', result)

	@staticmethod
	def assert_invalid_value(varName, result):
		TestBase.assert_var_error(varName, 'Invalid value', result)


if __name__ == '__main__':
	raise RuntimeError("Pending discovery support")
