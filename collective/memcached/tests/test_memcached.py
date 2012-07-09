import unittest
import pylibmc
from zope.component import getMultiAdapter, getUtility
from collective.memcached.testing import MEMCACHED_INTEGRATION_TESTING
from collective.memcached.interfaces import IMemcachedClient
from collective.memcached.utility import MemcachedClient
from plone.app.testing import setRoles, TEST_USER_ID


class MemcachedTest(unittest.TestCase):
    layer = MEMCACHED_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_memcached_utility_exists(self):
        memcached_utility = getUtility(IMemcachedClient)
        self.assertIsInstance(memcached_utility, MemcachedClient)

    def test_memcached_connection(self):
        memcached_utility = getUtility(IMemcachedClient)
        client = memcached_utility()
        self.assertIsInstance(client, pylibmc.Client)

    def test_memcached_setget(self):
        memcached_utility = getUtility(IMemcachedClient)
        client = memcached_utility()
        client.set('memcached_test', 'it works')
        self.assertEqual(client.get('memcached_test'), 'it works')

    def test_controlpanel_exists(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name=u"memcached-settings")
        view = view.__of__(self.portal)
        self.assertTrue(view)
