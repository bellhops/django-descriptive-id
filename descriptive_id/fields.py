# -*- coding: utf-8 -*-
import string
import random

from django import forms
from django.db.models import CharField


class DescriptiveIDField(CharField):

    def __init__(self, prefix=None, auto=True, *args, **kwargs):
        if not prefix:
            raise ValueError("The 'prefix=' argument is a required keyword argument.")
        else:
            self.prefix = prefix
        self.auto = auto

        kwargs['max_length'] = len(self.prefix) + 15

        if auto:
            # Do not let the user edit UUIDs if they are auto-assigned.
            kwargs['editable'] = False
            kwargs['blank'] = True
            kwargs['unique'] = True
        super(DescriptiveIDField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(DescriptiveIDField, self).deconstruct()

        kwargs['prefix'] = self.prefix
        kwargs['auto'] = self.auto

        if self.auto:
            kwargs.pop('editable')
            kwargs.pop('blank')
            kwargs.pop('unique')
            kwargs['auto'] = True

        return name, path, args, kwargs

    def _generate_descriptive_id(self):
        return '{prefix}_'.format(prefix=self.prefix) + ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(14))

    def pre_save(self, model_instance, add):
        """
        This is used to ensure that we auto-set values if required.
        See CharField.pre_save
        """
        descriptive_id = getattr(model_instance, self.attname, None)
        if self.auto and add and not descriptive_id:
            # Assign a new value for this attribute if required.
            descriptive_id = self._generate_descriptive_id()
            setattr(model_instance, self.attname, descriptive_id)
        return descriptive_id

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.CharField,
            'max_length': self.max_length,
        }
        defaults.update(kwargs)
        return super(DescriptiveIDField, self).formfield(**defaults)
