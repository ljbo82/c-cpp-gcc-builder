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

DIR  = "projects"

class test_proj_version(TestBase):

	def setUp(self):
		self.cwd = DIR

	@TestBase.BuildTest
	def test_reject_from_command_line(self):
		result = self.make('PROJ_VERSION=some_val')
		self.assert_unexpected_origin('PROJ_VERSION', 'command line', result)

	@TestBase.BuildTest
	def test_reject_from_enviroment(self):
		result = self.make(env='PROJ_VERSION=some_val')
		self.assert_unexpected_origin('PROJ_VERSION', 'environment', result)

	@TestBase.BuildTest
	def test_reject_empty_value(self):
		result = self.make('-f proj_version_empty.mk')
		self.assert_missing_value('PROJ_VERSION', result)

	@TestBase.BuildTest
	def test_reject_invalid_value(self):
		result = self.make('-f proj_version_invalid.mk')
		self.assert_var_error('PROJ_VERSION', 'Invalid semantic version', result)

	@TestBase.BuildTest
	def test_undefined_uses_default_value(self):
		result = self.make('print-vars VARS=PROJ_VERSION')
		self.assert_success(result, 'PROJ_VERSION = 0.1.0')

if __name__ == '__main__':
	unittest.main()
