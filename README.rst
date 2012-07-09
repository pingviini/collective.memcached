Introduction
============

Collective.memcached is simple utility for Plone which provides memcached_
connection. This package is intended for integrators to use in their own
packages.

Requirements
------------

collective.memcached uses pylibmc_ library for memcached connection which has
following requirements:

* Python 2.5 or later
* libmemcached 0.32 or later (last test with 0.51)
* zlib (required for compression support)
* libsasl2 (required for authentication support)

Usage
-----

#. Add collective.memcached to your buildout eggs list and run buildout.
#. Start your plone instance and activate collective.memcached (this enables
   collective.memcached controlpanel and registers MemcachedClient as local
   utility).
#. Go to memcached control panel and set memcached servers (defaults to
   localhost:11211).
#. Use it in your code::

    from collective.memcached.interfaces import IMemcachedClient
    from zope.component import getUtility

    mc_client = getUtility(IMemcachedClient)()
    mc_client.set('foo', 'bar')
    mc_client.get('foo')

.. _memcached: http://memcached.org/
.. _pylibmc: http://pypi.python.org/pypi/pylibmc/
