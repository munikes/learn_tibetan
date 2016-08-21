from django.apps import AppConfig
from django.utils.translation import ugettext as _


class TranslatorConfig(AppConfig):
    name = _('translator')
    verbose_name = _('Translator')
