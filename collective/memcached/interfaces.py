from zope.interface import Interface
from zope import schema
from collective.memcached import _


class IMemcachedControlPanel(Interface):
    """Memcached utility control panel"""

    memcached_hosts = schema.List(
        title=_(u"Memcached server hosts & ports"),
        description=_(u"eg. localhost:11211"),
        value_type=schema.TextLine(title=u"host"))


class IMemcachedClient(Interface):
    """Marker interface for memcached global utility"""
