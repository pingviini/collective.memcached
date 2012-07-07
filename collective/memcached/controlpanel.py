from plone.app.registry.browser import controlpanel
from collective.memcached.interfaces import IMemcachedControlPanel
from collective.memcached import _


class MemcachedControlPanelForm(controlpanel.RegistryEditForm):
    schema = IMemcachedControlPanel
    id = "memcached-settings"
    label = _(u"Memcached utility settings")
    description = _(u"Set memcached servers and ports with below form.")

    def updateFields(self):
        super(MemcachedControlPanelForm, self).updateFields()

    def updateWidgets(self):
        super(MemcachedControlPanelForm, self).updateWidgets()


class MemcachedControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MemcachedControlPanelForm
