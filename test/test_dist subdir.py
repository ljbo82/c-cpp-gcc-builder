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

class test_dist_subdir(TestBase):

	def setUp(self):
		self.cwd = DIR

	@TestBase.BuildTest
	def test_reject_value_with_spaces(self):
		result = self.make('DIST_SUBDIR=\ path\ with\ spaces')
		self.assert_no_whitespaces('DIST_SUBDIR', result)

	@TestBase.BuildTest
	def test_reject_invalid_path(self):
		result = self.make('DIST_SUBDIR=../dir_outside_build')
		self.assert_var_error('DIST_SUBDIR', 'Invalid path', result)

	@TestBase.BuildTest
	def test_reject_reserved_var(self):
		result = self.make('O_DIST_DIR=test')
		self.assert_use_of_reserved_variable('O_DIST_DIR', result)

	@TestBase.BuildTest
	def test_test_inspect_valid_value(self):
		result = self.make('DIST_SUBDIR=subDir print-vars VARS=O_DIST_DIR')
		self.assert_success(result, 'O_DIST_DIR = output/dist/subDir')

	@TestBase.BuildTest(cwd='../../demos/c-app')
	def test_test_valid_value(self):
		result = self.make('DIST_SUBDIR=subDir')
		self.assert_success(result)
		self.assertTrue(os.path.exists('output/dist/subDir/bin/hello'))

if __name__ == '__main__':
	unittest.main()
