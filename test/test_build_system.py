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
import os

DIR  = "projects"

class BuildSystemTest(TestBase):

	def setUp(self):
		self.cwd = DIR

	@TestBase.BuildTest(cwd='path with spaces')
	def test_reject_path_with_spaces(self):
		result = self.make()
		self.assert_failure(result, "whitespaces")

	#region var: PROJ_NAME
	# --------------------------------------------------------------------------
	@TestBase.BuildTest
	def test_proj_name_reject_from_command_line(self):
		result = self.make('-f proj_name_undefined.mk PROJ_NAME=some_val')
		self.assert_unexpected_origin('PROJ_NAME', 'command line', result)

	@TestBase.BuildTest
	def test_proj_name_reject_from_environment(self):
		result = self.make(make_flags='-f proj_name_undefined.mk', env='PROJ_NAME=some_val')
		self.assert_unexpected_origin('PROJ_NAME', 'environment', result)

	@TestBase.BuildTest
	def test_proj_name_reject_undefined(self):
		result = self.make('-f proj_name_undefined.mk')
		self.assert_missing_value('PROJ_NAME', result)

	@TestBase.BuildTest
	def test_proj_name_reject_empty_value(self):
		result = self.make('-f proj_name_empty.mk')
		self.assert_missing_value('PROJ_NAME', result)

	@TestBase.BuildTest
	def test_proj_name_reject_value_with_spaces(self):
		result = self.make('-f proj_name_spaces.mk')
		self.assert_no_whitespaces('PROJ_NAME', result)
	# --------------------------------------------------------------------------
	#endregion

	#region var: PROJ_VERSION
	# --------------------------------------------------------------------------
	@TestBase.BuildTest
	def test_proj_version_reject_from_command_line(self):
		result = self.make('PROJ_VERSION=some_val')
		self.assert_unexpected_origin('PROJ_VERSION', 'command line', result)

	@TestBase.BuildTest
	def test_proj_version_reject_from_enviroment(self):
		result = self.make(env='PROJ_VERSION=some_val')
		self.assert_unexpected_origin('PROJ_VERSION', 'environment', result)

	@TestBase.BuildTest
	def test_proj_version_reject_empty_value(self):
		result = self.make('-f proj_version_empty.mk')
		self.assert_missing_value('PROJ_VERSION', result)

	@TestBase.BuildTest
	def test_proj_version_reject_invalid_value(self):
		result = self.make('-f proj_version_invalid.mk')
		self.assert_var_error('PROJ_VERSION', 'Invalid semantic version', result)

	@TestBase.BuildTest
	def test_proj_version_undefined_uses_default_value(self):
		result = self.make('print-vars VARS=PROJ_VERSION')
		self.assert_success(result, 'PROJ_VERSION = 0.1.0')
	# --------------------------------------------------------------------------
	#endregion

	#region var: PROJ_TYPE
	# --------------------------------------------------------------------------
	@TestBase.BuildTest
	def test_proj_type_reject_from_command_line(self):
		result = self.make('-f proj_type_undefined.mk PROJ_TYPE=some_val')
		self.assert_unexpected_origin('PROJ_TYPE', 'command line', result)

	@TestBase.BuildTest
	def test_proj_type_reject_from_environment(self):
		result = self.make(make_flags='-f proj_type_undefined.mk', env='PROJ_TYPE=some_val')
		self.assert_unexpected_origin('PROJ_TYPE', 'environment', result)

	@TestBase.BuildTest
	def test_proj_type_reject_empty_value(self):
		result = self.make('-f proj_type_empty.mk')
		self.assert_missing_value('PROJ_TYPE', result)

	@TestBase.BuildTest
	def test_proj_type_reject_undefined(self):
		result = self.make('-f proj_type_undefined.mk')
		self.assert_missing_value('PROJ_TYPE', result)

	@TestBase.BuildTest
	def test_proj_type_reject_value_with_spaces(self):
		result = self.make('-f proj_type_spaces.mk')
		self.assert_no_whitespaces('PROJ_TYPE', result)

	@TestBase.BuildTest
	def test_proj_type_reject_invalid_value(self):
		result = self.make('-f proj_type_invalid.mk')
		self.assert_invalid_value('PROJ_TYPE', result)
	# --------------------------------------------------------------------------
	#endregion

	@TestBase.BuildTest
	def test_target_deps_with_other_targets(self):
		result = self.make('deps print-vars')
		self.assert_failure(result, 'deps cannot be invoked along with other targets (extra targets: print-vars)')

	#region target: print-vars
	# --------------------------------------------------------------------------
	@TestBase.BuildTest
	def test_target_print_vars_with_other_targets(self):
		result = self.make('print-vars help')
		self.assert_failure(result, 'print-vars cannot be invoked along with other targets')

	@TestBase.BuildTest
	def test_target_print_vars_no_vars(self):
		result = self.make('print-vars VARS=')
		self.assert_missing_value('VARS', result)
	# --------------------------------------------------------------------------
	#endregion

	#region var: DEBUG
	# --------------------------------------------------------------------------
	@TestBase.BuildTest
	def test_debug_reject_empty_value(self):
		result = self.make('-f debug_empty.mk')
		self.assert_missing_value('DEBUG', result)

	@TestBase.BuildTest
	def test_debug_reject_value_with_spaces(self):
		result = self.make('-f debug_spaces.mk')
		self.assert_no_whitespaces('DEBUG', result)

	@TestBase.BuildTest
	def test_debug_type_reject_invalid_value(self):
		result = self.make('DEBUG=invalid')
		self.assert_invalid_value('DEBUG', result)

	@TestBase.BuildTest
	def test_debug_undefined_uses_default_value(self):
		result = self.make('print-vars VARS=DEBUG')
		self.assert_success(result, 'DEBUG = 0')
	# --------------------------------------------------------------------------
	#endregion

	#region BUILD_SUBDIR
	# --------------------------------------------------------------------------
	@TestBase.BuildTest
	def test_build_subdir_reject_value_with_spaces(self):
		result = self.make('BUILD_SUBDIR=\ path\ with\ spaces')
		self.assert_no_whitespaces('BUILD_SUBDIR', result)

	@TestBase.BuildTest
	def test_build_subdir_reject_invalid_path(self):
		result = self.make('BUILD_SUBDIR=../dir_outside_build')
		self.assert_var_error('BUILD_SUBDIR', 'Invalid path', result)

	@TestBase.BuildTest
	def test_build_subdir_reject_reserved_var(self):
		result = self.make('O_BUILD_DIR=test')
		self.assert_use_of_reserved_variable('O_BUILD_DIR', result)

	@TestBase.BuildTest
	def test_build_subdir_test_inspect_valid_value(self):
		result = self.make('BUILD_SUBDIR=subDir print-vars VARS=O_BUILD_DIR')
		self.assert_success(result, 'O_BUILD_DIR = output/build/subDir')

	@TestBase.BuildTest(cwd='../../demos/c-app')
	def test_build_subdir_test_valid_value(self):
		result = self.make('BUILD_SUBDIR=subDir')
		self.assert_success(result)
		self.assertTrue(os.path.exists('output/build/subDir/hello'))
	# --------------------------------------------------------------------------
	#endregion

	#region DIST_SUBDIR
	# --------------------------------------------------------------------------
	@TestBase.BuildTest
	def test_dist_subdir_reject_value_with_spaces(self):
		result = self.make('DIST_SUBDIR=\ path\ with\ spaces')
		self.assert_no_whitespaces('DIST_SUBDIR', result)

	@TestBase.BuildTest
	def test_dist_subdir_reject_invalid_path(self):
		result = self.make('DIST_SUBDIR=../dir_outside_build')
		self.assert_var_error('DIST_SUBDIR', 'Invalid path', result)

	@TestBase.BuildTest
	def test_dist_subdir_reject_reserved_var(self):
		result = self.make('O_DIST_DIR=test')
		self.assert_use_of_reserved_variable('O_DIST_DIR', result)

	@TestBase.BuildTest
	def test_dist_subdir_test_inspect_valid_value(self):
		result = self.make('DIST_SUBDIR=subDir print-vars VARS=O_DIST_DIR')
		self.assert_success(result, 'O_DIST_DIR = output/dist/subDir')

	@TestBase.BuildTest(cwd='../../demos/c-app')
	def test_dist_subdir_test_valid_value(self):
		result = self.make('DIST_SUBDIR=subDir')
		self.assert_success(result)
		self.assertTrue(os.path.exists('output/dist/subDir/bin/hello'))
	# --------------------------------------------------------------------------
	#endregion

if __name__ == '__main__':
	unittest.main()
