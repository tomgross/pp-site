__author__ = 'tom'

from Products.Five import BrowserView
from plone import api

class UpgradeIt(BrowserView):

    def __call__(self):
        portal_setup = api.portal.get_tool(name='portal_setup')
        portal_setup.runImportStepFromProfile(
            'profile-plonetheme.sunburst:default', 'cssregistry', run_dependencies=False)
        portal_skins = api.portal.get_tool(name='portal_skins')
        custom = portal_skins['custom']
        for oid in ['main_template', 'base_properties', 'ploneCustom.css']:
            if oid in custom:
                api.content.delete(obj=custom[oid])
        return "DONE"