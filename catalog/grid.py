# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.utils import display_for_field
from django.db.models.fields import FieldDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.admin.views.main import EMPTY_CHANGELIST_VALUE
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from django.template.defaultfilters import linebreaksbr
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.db import models


class GridRow(object):

    EDITABLE_FIELDS = [
        'CharField',
        'IntegerField',
        'PositiveIntegerField',
        'BooleanField'
    ]

    def __init__(self, obj, fields, admin_cls):
        self.obj = obj
        self.fields = fields
        self.admin_cls = admin_cls

    def json_data(self):
        link = reverse('admin:{0}_{1}_change'.
                       format(self.obj.__class__._meta.app_label,
                              self.obj.__class__.__name__.lower()),
                       args=(self.obj.id,))
        data = {'id': self.obj.tree.get().id, 'link': link}
        for field_name in self.fields:
            editable = True
            try:
                field = self.obj._meta.get_field(field_name)
                if field.get_internal_type() not in self.EDITABLE_FIELDS or \
                        field_name not in self.admin_cls.list_editable:
                        editable = False
            except FieldDoesNotExist:
                editable = False

            value = ''
            field_type = 'text'
            modelfield = None
            if field_name in self.admin_cls.list_display:
                try:
                    modelfield, attr, val = \
                        admin.utils.lookup_field(field_name, self.obj,
                                                 self.admin_cls)
                except (AttributeError, ValueError, ObjectDoesNotExist):
                    result_repr = EMPTY_CHANGELIST_VALUE
                else:
                    if modelfield is None:
                        boolean = getattr(attr, "boolean", False)
                        if boolean:
                            result_repr = 't' if val else 'f'
                            field_type = 'checkbox'
                        else:
                            result_repr = smart_text(val)
                            if getattr(attr, "allow_tags", False):
                                result_repr = mark_safe(result_repr)
                            else:
                                result_repr = linebreaksbr(result_repr,
                                                           autoescape=True)
                    else:
                        result_repr = display_for_field(val, modelfield)
                value = conditional_escape(result_repr)

            correct_values = None
            if modelfield:
                if isinstance(modelfield, models.BooleanField):
                    field_type = 'checkbox'
                    value = 't' if val else 'f'
                if isinstance(modelfield,
                              (models.IntegerField, models.CharField)) \
                        and modelfield.choices:
                    field_type = 'select'
                    value = val
                    correct_values = dict(modelfield.choices)

            data[field_name] = {
                'type': field_type,
                'value': value,
                'editable': editable,
                'correct_values': correct_values if correct_values else ''
            }
        return data