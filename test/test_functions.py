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

class test_functions(TestBase):
	@staticmethod
	def call_function(call, hasReturn=True):
		if hasReturn:
			TestBase.create_file('Makefile', textwrap.dedent(f'''\
				include {TestBase.CPB_DIR}/functions.mk
				$(info $(call {call}))
				.PHONY: all
				all:
					@true
				''')
			)
		else:
			TestBase.create_file('Makefile', textwrap.dedent(f'''\
				include {TestBase.CPB_DIR}/functions.mk
				$(call {call})
				.PHONY: all
				all:
					@true
				''')
			)

		return TestBase.make()

	@TestBase.BuildTest
	def test_fn_semver_cmp(self):
		result = self.call_function('fn_semver_cmp,1,2')
		self.assert_success(result, '-3')

		result = self.call_function('fn_semver_cmp,2,1')
		self.assert_success(result, '3')

		result = self.call_function('fn_semver_cmp,1.0,2.0')
		self.assert_success(result, '-3')

		result = self.call_function('fn_semver_cmp,2.0,1.0')
		self.assert_success(result, '3')

		result = self.call_function('fn_semver_cmp,1.0,1.1')
		self.assert_success(result, '-2')

		result = self.call_function('fn_semver_cmp,1.1,1.0')
		self.assert_success(result, '2')

		result = self.call_function('fn_semver_cmp,1.0.0,1.1.0')
		self.assert_success(result, '-2')

		result = self.call_function('fn_semver_cmp,1.1.0,1.0.0')
		self.assert_success(result, '2')

		result = self.call_function('fn_semver_cmp,1.0.0,1.0.1')
		self.assert_success(result, '-1')

		result = self.call_function('fn_semver_cmp,1.0.1,1.0.0')
		self.assert_success(result, '1')

		result = self.call_function('fn_semver_cmp,1,1')
		self.assert_success(result, '0')

		result = self.call_function('fn_semver_cmp,1.0,1')
		self.assert_success(result, '0')

		result = self.call_function('fn_semver_cmp,1.0,1.0')
		self.assert_success(result, '0')

		result = self.call_function('fn_semver_cmp,1.0.0,1')
		self.assert_success(result, '0')

		result = self.call_function('fn_semver_cmp,1.0.0,1.0')
		self.assert_success(result, '0')

		result = self.call_function('fn_semver_cmp,1.0.0,1.0.0')
		self.assert_success(result, '0')

	@TestBase.BuildTest
	def test_fn_semver_check_compat(self):
		result = self.call_function('fn_semver_check_compat,4,4', False)
		self.assert_success(result)

		result = self.call_function('fn_semver_check_compat,4.3,4.3', False)
		self.assert_success(result)

		result = self.call_function('fn_semver_check_compat,4.3.0,4.3.0', False)
		self.assert_success(result)

		result = self.call_function('fn_semver_check_compat,4.3,4.4', False)
		self.assert_success(result)

		result = self.call_function('fn_semver_check_compat,4.3.3,4.3.4', False)
		self.assert_success(result)

		result = self.call_function('fn_semver_check_compat,4,5', False)
		self.assert_failure(result, '4+')

		result = self.call_function('fn_semver_check_compat,5,4', False)
		self.assert_failure(result, '5+')

		result = self.call_function('fn_semver_check_compat,4.3,4.2', False)
		self.assert_failure(result, '4.3+')

		result = self.call_function('fn_semver_check_compat,4.3.2,4.3.1', False)
		self.assert_failure(result, '4.3.2+')

if __name__ == '__main__':
	unittest.main()
