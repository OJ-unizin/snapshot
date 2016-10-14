import unittest

from testcase1 import TestCase1
from testcase2 import TestCase2
from testcase3 import TestCase3

class TestSuite(unittest.TestSuite):
  def suite():
      suite = unittest.TestSuite()
      suite.addTest(TestCase1('test_loginpage_webElements'))
      suite.addTest(TestCase2('test_snapshot_webElements'))
      suite.addTest(TestCase3('test_iframe_webElements'))
      return suite

if __name__ == '__main__':
   unittest.main()
