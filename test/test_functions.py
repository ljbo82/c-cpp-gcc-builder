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
	def call_function(call, has_return=True, make_flags=None, env=None):
		if has_return:
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

		return TestBase.make(make_flags, env)

	@TestBase.BuildTest
	def test_fn_semver_cmp(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME = project
			PROJ_TYPE = app

			# Declaring a variable using a restricted name:
			fn_semver_cmp := some_val

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_reserved_variable('fn_semver_cmp', result)

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
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME = project
			PROJ_TYPE = app

			# Declaring a variable using a restricted name:
			fn_semver_check_compat := some_val

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_reserved_variable('fn_semver_check_compat', result)

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

		result = self.call_function('fn_semver_check_compat,4,5,1',False)
		self.assert_success(result)

		result = self.call_function('fn_semver_check_compat,5,4', False)
		self.assert_failure(result, '5+')

		result = self.call_function('fn_semver_check_compat,4.3,4.2', False)
		self.assert_failure(result, '4.3+')

		result = self.call_function('fn_semver_check_compat,4.3.2,4.3.1', False)
		self.assert_failure(result, '4.3.2+')

	@TestBase.BuildTest
	def test_fn_check_not_origin(self):
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME = project
			PROJ_TYPE = app

			# Declaring a variable using a restricted name:
			fn_check_not_origin := some_val

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_reserved_variable('fn_check_not_origin', result)

		result = self.call_function('fn_check_not_origin,VAR,environment', False, make_flags='VAR=val')
		self.assert_success(result)

		result = self.call_function('fn_check_not_origin,VAR,command line', False, env='VAR=val')
		self.assert_success(result)

		result = self.call_function('fn_check_not_origin,VAR,environment', False, env='VAR=val')
		self.assert_failure(result, 'environment')

		result = self.call_function('fn_check_not_origin,VAR,command line', False,'VAR=val')
		self.assert_failure(result, 'command line')

	@TestBase.BuildTest
	def test_fn_test_patterns(self):
		# Check reserved usage -------------------------------------------------
		self.create_file('Makefile', textwrap.dedent(f'''\
			PROJ_NAME = project
			PROJ_TYPE = app

			# Declaring a variable using a restricted name:
			fn_test_patterns := some_val

			include {TestBase.CPB_DIR}/builder.mk
			''')
		)
		result = self.make()
		self.assert_error_reserved_variable('fn_test_patterns', result)
		# ----------------------------------------------------------------------

		# Check matching -------------------------------------------------------
		result = self.call_function('fn_test_patterns,http://% https://% git://%,http://someurl.com')
		self.assert_success(result,'http://%')

		result = self.call_function('fn_test_patterns,http://% https://% git://%,https://someurl.com')
		self.assert_success(result,'https://%')

		result = self.call_function('fn_test_patterns,http://% https://% git://%,git://someurl.com')
		self.assert_success(result,'git://%')

		result = self.call_function('fn_test_patterns,http://% https://% git://%,hg://someurl.com')
		self.assert_success(result)
		self.assertEqual('', result.output[0])
		# ----------------------------------------------------------------------

		# Check find and replace -----------------------------------------------
		result = self.call_function('fn_test_patterns,http://% https://% git://%,http://someurl.com,://%')
		self.assert_success(result)
		self.assertEqual('http', result.output[0])

		result = self.call_function('fn_test_patterns,http://% https://% git://%,http://someurl.com,://%,X')
		self.assert_success(result,'httpX')


		result = self.call_function('fn_test_patterns,http://% https://% git://%,https://someurl.com,://%')
		self.assert_success(result)
		self.assertEqual('https', result.output[0])

		result = self.call_function('fn_test_patterns,http://% https://% git://%,https://someurl.com,://%,Y')
		self.assert_success(result,'httpsY')


		result = self.call_function('fn_test_patterns,http://% https://% git://%,git://someurl.com,://%')
		self.assert_success(result)
		self.assertEqual('git', result.output[0])

		result = self.call_function('fn_test_patterns,http://% https://% git://%,git://someurl.com,://%,Z')
		self.assert_success(result,'gitZ')


		result = self.call_function('fn_test_patterns,http://% https://% git://%,hg://someurl.com,://%')
		self.assert_success(result)
		self.assertEqual('', result.output[0])

		result = self.call_function('fn_test_patterns,http://% https://% git://%,hg://someurl.com,://%,W')
		self.assert_success(result)
		self.assertEqual('', result.output[0])
		# ----------------------------------------------------------------------

if __name__ == '__main__':
	unittest.main()
