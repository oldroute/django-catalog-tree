from django.db.models import signals
from catalog.utils import get_catalog_models
from catalog.models import TreeItem


def insert_in_tree(sender, instance, **kwargs):

    created = kwargs.pop('created', False)
    if created:
        parent = getattr(instance, 'parent', None)
        if parent is None:
            tree_item = TreeItem(parent=None, content_object=instance)
        else:
            tree_item = TreeItem(parent=parent, content_object=instance)
        tree_item.save()

for model_cls in get_catalog_models():
    signals.post_save.connect(insert_in_tree, sender=model_cls)
