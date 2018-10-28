from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
from plone.portlet.static.static import AddForm as BaseAddForm
from plone.portlet.static.static import Assignment as BaseAssignment
from plone.portlet.static.static import EditForm as BaseEditForm
from plone.portlet.static.static import IStaticPortlet
from plone.portlet.static.static import Renderer as BaseRenderer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope import schema
from zope.formlib import form
from zope.interface import implementer
from zope.schema.vocabulary import SimpleVocabulary


effects = SimpleVocabulary.fromValues([
    "bounce",
    "flash",
    "pulse",
    "rubberBand",
    "shake",
    "swing",
    "tada",
    "wobble",
    "jello",
    "bounceIn",
    "bounceInDown",
    "bounceInLeft",
    "bounceInRight",
    "bounceInUp",
    "bounceOut",
    "bounceOutDown",
    "bounceOutLeft",
    "bounceOutRight",
    "bounceOutUp",
    "fadeIn",
    "fadeInDown",
    "fadeInDownBig",
    "fadeInLeft",
    "fadeInLeftBig",
    "fadeInRight",
    "fadeInRightBig",
    "fadeInUp",
    "fadeInUpBig",
    "fadeOut",
    "fadeOutDown",
    "fadeOutDownBig",
    "fadeOutLeft",
    "fadeOutLeftBig",
    "fadeOutRight",
    "fadeOutRightBig",
    "fadeOutUp",
    "fadeOutUpBig",
    "flip",
    "flipInX",
    "flipInY",
    "flipOutX",
    "flipOutY",
    "lightSpeedIn",
    "lightSpeedOut",
    "rotateIn",
    "rotateInDownLeft",
    "rotateInDownRight",
    "rotateInUpLeft",
    "rotateInUpRight",
    "rotateOut",
    "rotateOutDownLeft",
    "rotateOutDownRight",
    "rotateOutUpLeft",
    "rotateOutUpRight",
    "slideInUp",
    "slideInDown",
    "slideInLeft",
    "slideInRight",
    "slideOutUp",
    "slideOutDown",
    "slideOutLeft",
    "slideOutRight",
    "zoomIn",
    "zoomInDown",
    "zoomInLeft",
    "zoomInRight",
    "zoomInUp",
    "zoomOut",
    "zoomOutDown",
    "zoomOutLeft",
    "zoomOutRight",
    "zoomOutUp",
    "hinge",
    "jackInTheBox",
    "rollIn",
    "rollOut"
])


_ = unicode

class IAnimateStaticPortlet(IStaticPortlet):
    """A portlet which renders predefined static HTML.

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    effect = schema.Choice(
        title=_(u"Animation effect"),
        description=_(u"Type of animation effect used. See https://daneden.github.io/animate.css/"),
        vocabulary=effects,
        required=False)


@implementer(IAnimateStaticPortlet)
class Assignment(BaseAssignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    effect = u''

    def __init__(self, header=u"", text=u"", omit_border=False, footer=u"",
                 more_url='', effect=u''):
        self.effect = effect

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave or
        static string if title not defined.
        """
        return self.header or _(u'Animation Portlet')


class Renderer(BaseRenderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('static.pt')

    def css_class(self):
        css_class = super(Renderer, self).css_class()
        return css_class + ' ' + self.data.effect

class AddForm(BaseAddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """

    form_fields = form.Fields(IAnimateStaticPortlet)
    form_fields['text'].custom_widget = WYSIWYGWidget

    def create(self, data):
        return Assignment(**data)


class EditForm(BaseEditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """

    form_fields = form.Fields(IAnimateStaticPortlet)
    form_fields['text'].custom_widget = WYSIWYGWidget

