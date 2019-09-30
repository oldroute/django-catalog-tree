from __future__ import unicode_literals
from django.apps import AppConfig
from catalog import settings


class CatalogAppConfig(AppConfig):
    name = 'catalog'
    verbose_name = settings.APP_VERBOSE_NAME_NAME


# class for custom catalog models
class CustomCatalogBaseConfig(AppConfig):

    def ready(self):
        from catalog import signals
