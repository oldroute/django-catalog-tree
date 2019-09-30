from __future__ import unicode_literals
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# for change folder name with you custom catalog templates
TEMPLATES_FOLDER = settings.CATALOG_TEMPLATES_FOLDER_NAME if hasattr(settings, "CATALOG_TEMPLATES_FOLDER_NAME") else "catalog"
# for change app verbose name in the admin interface
APP_VERBOSE_NAME_NAME = settings.CATALOG_APP_VERBOSE_NAME if hasattr(settings, "CATALOG_APP_VERBOSE_NAME") else _('Catalog')
# for change treeitem model verbose names in the admin interface
TREEITEM_VERBOSE_NAME = settings.CATALOG_TREEITEM_VERBOSE_NAME if hasattr(settings, "CATALOG_TREEITEM_VERBOSE_NAME") else _('Catalog structure')
TREEITEM_VERBOSE_NAME_PLURAL = settings.CATALOG_TREEITEM_VERBOSE_NAME_PLURAL if hasattr(settings, "CATALOG_TREEITEM_VERBOSE_NAME_PLURAL") else _('Catalog structure')
# for change treeitem root element name in treeitem change template in the admin interface
TREEITEM_ROOT_ELEMENT_NAME = settings.CATALOG_TREEITEM_ROOT_ELEMENT_NAME if hasattr(settings, "CATALOG_TREEITEM_ROOT_ELEMENT_NAME") else _('Catalog')
