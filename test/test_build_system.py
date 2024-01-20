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

from TestBase import TestBase
import unittest

C_APP_DEMO_DIR = "../demos/c-app"
PROJECTS_DIR   = "projects"

class BuildSystemTest(unittest.TestCase, TestBase):

	@TestBase.BuildTest(cwd=f"{PROJECTS_DIR}/path with spaces", output_dir=None)
	def test_reject_path_with_spaces(self):
		result = self.make()
		self.assertNotEqual(0, result.exitCode)
		self.assert_contains("whitespaces", result.output)


	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=None)
	def test_proj_name_reject_from_command_line(self):
		result = self.make('PROJ_NAME=some_val')
		self.assert_unexpected_origin('PROJ_NAME', 'file', 'command line', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_name_reject_empty(self):
		result = self.make('-f proj_name_empty.mk')
		self.assert_missing_value('PROJ_NAME', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_name_reject_value_with_spaces(self):
		result = self.make('-f proj_name_spaces.mk')
		self.assert_no_whitespaces('PROJ_NAME', result)


	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=None)
	def test_proj_version_reject_from_command_line(self):
		result = self.make('PROJ_VERSION=some_val')
		self.assert_unexpected_origin('PROJ_VERSION', 'file', 'command line', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_version_reject_empty(self):
		result = self.make('-f proj_version_empty.mk')
		self.assert_missing_value('PROJ_VERSION', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_version_reject_invalid(self):
		result = self.make('-f proj_version_invalid.mk')
		self.assert_var_error('PROJ_VERSION', 'Invalid semantic version', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_version_reject_invalid(self):
		result = self.make('-f proj_version_invalid.mk')
		self.assert_var_error('PROJ_VERSION', 'Invalid semantic version', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_version_default_value(self):
		result = self.make('-f proj_version_default.mk print-vars VARS=PROJ_VERSION')
		self.assertTrue(result.exitCode == 0)
		self.assert_contains('PROJ_VERSION = 0.1.0', result.output)


	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=None)
	def test_proj_type_reject_from_command_line(self):
		result = self.make('PROJ_TYPE=some_val')
		self.assert_unexpected_origin('PROJ_TYPE', 'file', 'command line', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_type_reject_empty(self):
		result = self.make('-f proj_type_empty.mk')
		self.assert_missing_value('PROJ_TYPE', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_type_reject_value_with_spaces(self):
		result = self.make('-f proj_type_spaces.mk')
		self.assert_no_whitespaces('PROJ_TYPE', result)

	@TestBase.BuildTest(cwd=PROJECTS_DIR, output_dir=None)
	def test_proj_type_reject_invalid(self):
		result = self.make('-f proj_type_spaces.mk')
		self.assert_no_whitespaces('PROJ_TYPE', result)


	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=None)
	def test_target_deps_with_other_targets(self):
		result = self.make('deps print-vars')
		self.assertNotEqual(0, result.exitCode)
		self.assert_contains('deps cannot be invoked along with other targets (extra targets: print-vars)', result.output)


	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=None)
	def test_target_print_vars_with_other_targets(self):
		result = self.make('print-vars help')
		self.assertNotEqual(0, result.exitCode)
		self.assert_contains('print-vars cannot be invoked along with other targets (extra targets: help)', result.output)

	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=None)
	def test_target_print_vars_no_vars(self):
		result = self.make('print-vars VARS=')
		self.assert_missing_value('VARS', result)

if __name__ == '__main__':
	unittest.main()
