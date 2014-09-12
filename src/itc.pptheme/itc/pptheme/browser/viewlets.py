from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import LogoViewlet as LogoViewletBase
from plone.app.layout.viewlets.common import ViewletBase

from plone.app.portlets.portlets.navigation import Renderer as BaseNavRenderer

class LogoViewlet(LogoViewletBase):
    index = ViewPageTemplateFile('logo.pt')

class BelowTitleSeperator(ViewletBase):

    index = ViewPageTemplateFile('seperator.pt')


class AfterTitleSeperator(BelowTitleSeperator):
    """ """

class NavigationRenderer(BaseNavRenderer):

    recurse = ViewPageTemplateFile('navigation_recurse.pt')
