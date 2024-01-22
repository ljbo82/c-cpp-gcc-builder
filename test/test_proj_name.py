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

class test_proj_name(TestBase):

	def setUp(self):
		self.cwd = DIR

	@TestBase.BuildTest
	def test_reject_from_command_line(self):
		result = self.make('-f proj_name_undefined.mk PROJ_NAME=some_val')
		self.assert_unexpected_origin('PROJ_NAME', 'command line', result)

	@TestBase.BuildTest
	def test_reject_from_environment(self):
		result = self.make(make_flags='-f proj_name_undefined.mk', env='PROJ_NAME=some_val')
		self.assert_unexpected_origin('PROJ_NAME', 'environment', result)

	@TestBase.BuildTest
	def test_reject_undefined(self):
		result = self.make('-f proj_name_undefined.mk')
		self.assert_missing_value('PROJ_NAME', result)

	@TestBase.BuildTest
	def test_reject_empty_value(self):
		result = self.make('-f proj_name_empty.mk')
		self.assert_missing_value('PROJ_NAME', result)

	@TestBase.BuildTest
	def test_reject_value_with_spaces(self):
		result = self.make('-f proj_name_spaces.mk')
		self.assert_no_whitespaces('PROJ_NAME', result)

if __name__ == '__main__':
	unittest.main()
