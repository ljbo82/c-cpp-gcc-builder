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
import textwrap

from TestBase import TestBase

class test_proj_type(TestBase):
	@TestBase.BuildTest
	def test_reject_from_command_line(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME := hello

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make('PROJ_TYPE=app')
		self.assert_error_unexpected_origin('PROJ_TYPE', 'command line', result)

	@TestBase.BuildTest
	def test_reject_from_environment(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME := hello

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make(env='PROJ_TYPE=app')
		self.assert_error_unexpected_origin('PROJ_TYPE', 'environment', result)

	@TestBase.BuildTest
	def test_reject_empty_value(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			EMPTY :=
			PROJ_NAME := hello
			PROJ_TYPE = $(EMPTY)

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_missing_value('PROJ_TYPE', result)

	@TestBase.BuildTest
	def test_reject_undefined(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME := hello

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_missing_value('PROJ_TYPE', result)

	@TestBase.BuildTest
	def test_reject_value_with_spaces(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME := hello
			PROJ_TYPE := value with spaces

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_whitespaces('PROJ_TYPE', result)

	@TestBase.BuildTest
	def test_reject_invalid_value(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME := hello
			PROJ_TYPE := invalid

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_invalid_value('PROJ_TYPE', result)

if __name__ == '__main__':
	unittest.main()
