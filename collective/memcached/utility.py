import pylibmc
import logging

from threading import local
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.memcached.interfaces import IMemcachedControlPanel


logger = logging.getLogger("Plone")


class MemcachedClient(object):
    """Memcached client."""

    _v_thread_local = local()

    def __call__(self):
        """Return memcached client"""
        return self.getClient()

    def getClient(self):
        """Return thread local connection to memcached."""
        connection = getattr(self._v_thread_local, 'connection', None)

        if connection is None:
            settings = self.getSettings()
            logger.info("Creating new memcache connection")
            connection = pylibmc.Client(settings.memcached_hosts)
            self._v_thread_local.connection = connection

        return connection

    def getSettings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(IMemcachedControlPanel)
