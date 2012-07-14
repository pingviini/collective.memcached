Introduction
============

Collective.memcached is simple memcached utility for Plone. This package
doesn't do anything fancy in itself - it is mainly intended to be used in
other packages.

Requirements
------------

Collective.memcached uses either pylibmc_ or python-memcached_ library for
memcached_ connection. Pylibmc_ is faster but it has following requirements:

* Python 2.5 or later
* libmemcached 0.32 or later (last test with 0.51)
* zlib (required for compression support)
* libsasl2 (required for authentication support)

Python-memcached_ on the other hand is pure Python memcached client and should
work without other dependencies.

Usage
-----

#. Add collective.memcached to your buildout eggs list. You must also pick
   the connector library as package extras. Choices are pylibmc_ and
   python-memcached_. Your eggs list should look something like this::
    eggs = 
        Plone
        ...
        collective.memcached['pylibmc']
#. Run buildout, start your plone instance and activate collective.memcached
   (this enables collective.memcached controlpanel and registers
   MemcachedClient as local utility).
#. Go to memcached control panel and set memcached servers (defaults to
   localhost:11211).
#. Use it in your code::

    >>> from collective.memcached.interfaces import IMemcachedClient
    >>> from zope.component import getUtility
    >>> mc_client = getUtility(IMemcachedClient)()
    >>> mc_client.set('foo', 'bar')
    >>> True
    >>> mc_client.get('foo')
    >>> 'bar'

.. _memcached: http://memcached.org/
.. _pylibmc: http://pypi.python.org/pypi/pylibmc/
.. _python-memcached: http://pypi.python.org/pypi/python-memcached/
