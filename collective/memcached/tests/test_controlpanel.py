import unittest
from zope.component import getMultiAdapter
from collective.memcached.testing import MEMCACHED_INTEGRATION_TESTING
from collective.memcached.testing import MEMCACHED_FUNCTIONAL_TESTING
from plone.app.testing import setRoles, TEST_USER_ID


class MemcachedControlPanelTest(unittest.TestCase):
    layer = MEMCACHED_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_controlpanel_exists(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name=u"memcached-settings")
        view = view.__of__(self.portal)
        self.assertTrue(view)
