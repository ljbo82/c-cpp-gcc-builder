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

DEMO_DIR = "../demos/c-app"

class DemoCAppTest(unittest.TestCase, TestBase):

	def __init__(self, *args, **kwargs):
		unittest.TestCase.__init__(self, *args, **kwargs)
		TestBase.__init__(self, DEMO_DIR)

	@TestBase.BuildTest
	def test_linux_standard_verbosity(self):
		result = self.make()

		self.assertEqual(0, result.exitCode)
		self.assert_contains([ \
			"[CC] output/build/src/main.c.o", \
			"[LD] output/build/hello", \
			"[DIST] output/dist/bin/hello", \
		], result.output)
		self.assert_not_contains(['gcc', 'cp'], result.output)

	@TestBase.BuildTest
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

	@TestBase.BuildTest(output_dir=".build")
	def test_linux_custom_output(self):
		result = self.make('O=.build')

		self.assertEqual(0, result.exitCode)
		self.assert_contains([ \
			"[CC] .build/build/src/main.c.o", \
			"[LD] .build/build/hello", \
			"[DIST] .build/dist/bin/hello", \
		], result.output)
		self.assert_not_contains(['gcc', 'cp'], result.output)

if __name__ == '__main__':
	unittest.main()
