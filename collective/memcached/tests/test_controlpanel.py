import unittest

from collective.memcached.testing import MEMCACHED_INTEGRATION_TESTING


class MemcachedControlPanelTest(unittest.TestCase):
    layer = MEMCACHED_INTEGRATION_TESTING

    def setup(self):
        self.portal = self.layer['portal']

    def test_controlpanel_exists(self):
        pass
