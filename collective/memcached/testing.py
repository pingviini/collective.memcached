# from plone.testing import z2
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting # , FunctionalTesting


class MemcachedTestFixture(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.memcached
        self.loadZCML(name='configure.zcml', package=collective.memcached)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'collective.memcached:default')


MEMCACHED_FIXTURE = MemcachedTestFixture()
MEMCACHED_INTEGRATION_TESTING = IntegrationTesting(bases=(MEMCACHED_FIXTURE,),
                                                 name="memcached:Integration")
