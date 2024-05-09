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

import unittest

from TestBase import TestBase

class test_output_dir(TestBase):
	@TestBase.BuildTest()
	def test_reject_o_equal_proj_dir(self):
		self.create_file('Makefile', TestBase.MIN_VALID_APP_MAKEFILE)
		result = self.make('O=.')
		self.assert_failure(result)
		self.assert_contains(['[O]', 'Project root'], result.output)

	@TestBase.BuildTest()
	def test_default_output_dir(self):
		self.create_file('Makefile', TestBase.MIN_VALID_APP_MAKEFILE)
		result = self.make('print-vars VARS=\'O O_BASE\'')
		self.assert_success(result)
		self.assert_contains([
			f'O = output/{self.get_native_host()}/release',
			f'O_BASE = output'
		], result.output)

	@TestBase.BuildTest()
	def test_custom_output_dir(self):
		self.create_file('Makefile', TestBase.MIN_VALID_APP_MAKEFILE)
		result = self.make('print-vars VARS=\'O O_BASE\' O=build')
		self.assert_success(result)
		self.assert_contains([
			f'O = build',
			f'O_BASE = build'
		], result.output)

	@TestBase.BuildTest()
	def test_reject_o_outside_base_dir(self):
		self.create_file('Makefile', TestBase.MIN_VALID_APP_MAKEFILE)
		result = self.make('O_BASE=build O=output')
		self.assert_failure(result)
		self.assert_contains([
			'[O]',
			'outside O_BASE',
			'O=output',
			'O_BASE=build'], result.output)

	@TestBase.BuildTest()
	def test_reject_o_base_equal_proj_dir(self):
		self.create_file('Makefile', TestBase.MIN_VALID_APP_MAKEFILE)
		result = self.make('O_BASE=. O=output')
		self.assert_failure(result)
		self.assert_contains([
			'[O_BASE]',
			'Project root',
		], result.output)

if __name__ == '__main__':
	unittest.main()
