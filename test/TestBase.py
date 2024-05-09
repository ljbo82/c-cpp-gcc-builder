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
import tempfile
import textwrap

from pathlib import Path
from enum import Enum

class FindMode(Enum):
	'''
	Contains the mode used for find methods.
	'''
	FIND_ALL = 1,
	FIND_ANY = 2

class Result:
	'''
	Result of a shell command execution.

	Attributes:
		exitCode (int): Result of command execution.

		output (list): Process output (list of lines).
	'''
	def __init__(self, core_result):
		self.exitCode = core_result.returncode
		self.output = (core_result.stdout if core_result.returncode == 0 else core_result.stderr).strip().split('\n')

class TestBase(unittest.TestCase):
	CPB_DIR = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../core'))
	'''Directory where the build system is located.'''

	DEMOS_DIR = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../demos'))
	'''Directory where demo applications are located.'''

	MIN_VALID_APP_MAKEFILE = textwrap.dedent(f'''\
		PROJ_NAME = project
		PROJ_TYPE = app

		include {CPB_DIR}/builder.mk
		''')
	'''Minimal makefile for an application project. '''

	MIN_VALID_LIB_MAKEFILE = textwrap.dedent(f'''\
		PROJ_NAME = project
		PROJ_TYPE = lib

		include {CPB_DIR}/builder.mk
		''')
	'''Minimal makefile for a lib project.'''

	MIN_VALID_CUSTOM_MAKEFILE = textwrap.dedent(f'''\
		PROJ_NAME = project
		PROJ_TYPE = custom

		include {CPB_DIR}/builder.mk
		''')
	'''Minimal makefile for a custom project.'''

	@staticmethod
	def get_native_host():
		result = TestBase.exec(f'CPB_DIR={TestBase.CPB_DIR} make --no-print-directory -C {TestBase.DEMOS_DIR}/c-app print-vars VARS=NATIVE_HOST')
		TestBase.assert_success(result)
		return result.output[0].split(' ')[2]

	@staticmethod
	def create_file(path, contents=None):
		'''
		Creates a text file

		Args:
			path (str): Path of a file.

			contents (str): File contents.
		'''
		parent_dir = Path(path).parent.absolute()
		os.makedirs(parent_dir, exist_ok = True)
		with open(path, "w") as f:
			if contents is not None:
				f.write(contents)

	@staticmethod
	def BuildTest(subdir=None):
		'''
		Marks a test method to run in a temporary directory.

		Args:
			subdir (str): Optional subdirectory inside temporary directory.
		'''
		def decorator(func):
			@functools.wraps(func)
			def wrapper(self):
				with tempfile.TemporaryDirectory() as tmpDir:
					cwd = tmpDir
					if subdir is not None:
						cwd = os.path.abspath(os.path.join(cwd, subdir))
						os.mkdir(cwd)

					os.chdir(cwd)
					func(self)

			return wrapper

		if callable(subdir):
			decorator = TestBase.BuildTest(None)
			return decorator(subdir)

		return decorator

	@staticmethod
	def DemoTest(demo_dir, output_dir='output'):
		'''
		Marks a test method to run inside a demo directory.

		Args:
			demo_dir (str): Mandatory. Demo subdirectory inside TestBase.DEMOS_DIR.

			output_dir (str): Optional. Output directory after execution to be removed.
		'''
		def decorator(func):
			@functools.wraps(func)
			def wrapper(self):
				os.chdir(os.path.join(TestBase.DEMOS_DIR,demo_dir))
				os.environ['CPB_DIR'] = TestBase.CPB_DIR
				if output_dir is not None:
					if output_dir == '.':
						raise ValueError('Invalid output_dir: \'.\'')

					os.environ['O'] = output_dir

				try:
					func(self)
				finally:
					os.unsetenv('CPB_DIR')
					if output_dir is not None:
						if os.path.exists(output_dir):
							shutil.rmtree(output_dir, True)

						os.unsetenv('O')

			return wrapper

		if callable(demo_dir):
			raise ValueError('Missing demo_dir')
			# decorator = TestBase.DemoTest(output_dir)
			# return decorator(demo_dir)

		return decorator

	@staticmethod
	def exec(command):
		'''
		Executes a shell command.

		Args:
			command (str): shell command to be executed.

		Returns:
			Returns a Result instance.
		'''
		return Result(subprocess.run(\
			command, \
			capture_output = True, \
			text = True,\
			shell = True))

	@staticmethod
	def make(make_flags=None, env=None):
		'''
		Executes a make invocation.

		Args:
			make_flags (str): arguments to be passed to make invocation.

			env (str): environment variables to be defined during invocation.

		Returns:
			Returns a Result instance.
		'''
		make_command = f"{'' if env is None else env + ' '}make{'' if make_flags is None else ' ' + make_flags}"

		return TestBase.exec(make_command)

	@staticmethod
	def find(what, where, find_mode=FindMode.FIND_ANY):
		'''
		Finds for strings occurrences.

		Args:
			what (str or list): String or a list of strings to be searched.

			where (str or list): String of list of strings to be inspected.

			find_mode (FindMode=FindMode.FIND_ANY): Defines if all or any
				occurrence of `what` entries should be found inside `where`.

		Returns:
			A tuple with a boolean value indicating if find succeded and an entry:
				* If search fails, entry is the string not found.
				* If search succeeds:
					* If find_mode is FindMode.FIND_ANY, entry is the first matched string.
					* If find_mode is FindMode.FIND_ALL, entry is `what`
		'''
		if not isinstance(where, list):
			where = [where]

		if not isinstance(what, list):
			what = [what]

		found = False
		for whatEntry in what:
			found = False

			for whereEntry in where:
				if whatEntry in whereEntry:
					found = True
					break

			if not found and find_mode is FindMode.FIND_ALL:
				return (False, whatEntry)

			if found and find_mode is FindMode.FIND_ANY:
				return (True, whatEntry)

		return (found, what)

	@staticmethod
	def find_line(find, lines, exact_match=False):
		'''
		Returns the index of the first line containing a given string.

		Args:
			find (str): String to be searched.

			lines (list): List of lines to be inspected.

			exactMatch (bool=False): Defines if searched string should match
			    exactly with inspected line.

		Returns:
			The index of the first line containing seached string. If
			searched line is not found, returns -1
		'''
		index = 0
		for line in lines:
			if (find in line) if not exact_match else (find == line):
				return index

			index += 1

		return -1

	# region Assert methods
	# --------------------------------------------------------------------------
	@staticmethod
	def assert_contains(what, where):
		result = TestBase.find(what, where, find_mode=FindMode.FIND_ALL)
		if not result[0]:
			raise AssertionError(f"{repr(result[1])} was NOT found")

	@staticmethod
	def assert_not_contains(what, where):
		result = TestBase.find(what, where, find_mode=FindMode.FIND_ANY)
		if result[0]:
			raise AssertionError(f"{repr(result[1])} was FOUND")

	@staticmethod
	def assert_find_line(find, lines, exact_match=False):
		line = TestBase.find_line(find, lines, exact_match)
		if line == -1:
			raise AssertionError(f"{repr(find)} was NOT found")

		return line

	@staticmethod
	def assert_success(result, output_message=None, exact_match=False):
		if result.exitCode != 0:
			raise AssertionError("Execution failed")

		if output_message is not None:
			TestBase.assert_find_line(output_message, result.output, exact_match)

	@staticmethod
	def assert_failure(result, output_message=None, exact_match=False):
		if result.exitCode == 0:
			raise AssertionError("Execution succeeded")

		if output_message is not None:
			TestBase.assert_find_line(output_message, result.output, exact_match)

	@staticmethod
	def assert_error_var(var_name, var_message, result):
		TestBase.assert_failure(result, f'[{var_name}] {var_message}')

	@staticmethod
	def assert_error_missing_value(var_name, result):
		TestBase.assert_error_var(var_name, 'Missing value', result)

	@staticmethod
	def assert_error_unexpected_origin(var_name, given_origin, result):
		TestBase.assert_error_var(var_name, f'Unexpected origin: "{given_origin}"', result)

	@staticmethod
	def assert_error_whitespaces(var_name, result):
		TestBase.assert_error_var(var_name, 'Value cannot have whitespaces', result)

	@staticmethod
	def assert_error_invalid_value(var_name, result):
		TestBase.assert_error_var(var_name, 'Invalid value', result)

	@staticmethod
	def assert_error_reserved_variable(var_name, result):
		TestBase.assert_error_var(var_name, 'Reserved variable', result)
	# --------------------------------------------------------------------------
	#endregion

if __name__ == '__main__':
	raise RuntimeError("Pending discovery support")
