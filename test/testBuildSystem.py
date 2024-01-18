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

C_APP_DEMO_DIR       = "../demos/c-app"
INVALID_PROJECTS_DIR = "invalid_projects"

class BuildSystemTest(unittest.TestCase, TestBase):

	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR)
	def test_linux_standard_verbosity(self):
		result = self.make()

		self.assertEqual(0, result.exitCode)
		self.assert_contains([ \
			"[CC] output/build/src/main.c.o", \
			"[LD] output/build/hello", \
			"[DIST] output/dist/bin/hello", \
		], result.output)
		self.assert_not_contains(['gcc', 'cp'], result.output)

	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR)
	def test_linux_verbose_build(self):
		result = self.make(make_flags="V=1")
		self.assertEqual(0, result.exitCode)

		line = self.assert_find_line("[CC] output/build/src/main.c.o", result.output)
		self.assert_contains( \
			"gcc -MMD -MP -Isrc -Wall -O2 -s -c src/main.c -o output/build/src/main.c.o", \
			result.output[line + 1])

		line = self.assert_find_line("[LD] output/build/hello", result.output)
		self.assert_contains( \
			"gcc -o output/build/hello output/build/src/main.c.o -s", \
			result.output[line + 1])

		line = self.assert_find_line("[DIST] output/dist/bin/hello", result.output)
		self.assert_contains( \
			"/bin/cp output/build/hello output/dist/bin/hello", \
			result.output[line + 1])

	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=".build")
	def test_linux_custom_output(self):
		result = self.make('O=.build')

		self.assertEqual(0, result.exitCode)
		self.assert_contains([ \
			"[CC] .build/build/src/main.c.o", \
			"[LD] .build/build/hello", \
			"[DIST] .build/dist/bin/hello", \
		], result.output)
		self.assert_not_contains(['gcc', 'cp'], result.output)

	@TestBase.BuildTest(cwd=f"{INVALID_PROJECTS_DIR}/path with spaces", output_dir=None)
	def test_reject_path_with_spaces(self):
		result = self.make()
		self.assertNotEqual(0, result.exitCode)
		self.assert_contains("whitespaces", result.output)

	@TestBase.BuildTest(cwd=C_APP_DEMO_DIR, output_dir=None)
	def test_reject_proj_name_from_command_line(self):
		result = self.make(make_flags='PROJ_NAME=some_val')
		self.assert_unexpected_origin('PROJ_NAME', 'file', 'command line', result)

	@TestBase.BuildTest(cwd=INVALID_PROJECTS_DIR, output_dir=None)
	def test_reject_empty_proj_name(self):
		result = self.make(make_flags='-f empty_proj_name.mk')
		self.assert_missing_value('PROJ_NAME', result)

	@TestBase.BuildTest(cwd=INVALID_PROJECTS_DIR, output_dir=None)
	def test_reject_proj_name_with_spaces(self):
		result = self.make(make_flags='-f proj_name_spaces.mk')
		self.assert_no_whitespaces('PROJ_NAME', result)

if __name__ == '__main__':
	unittest.main()
