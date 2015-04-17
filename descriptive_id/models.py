# -*- coding: utf-8 -*-
import string
import random

from django.db import models


class DescriptiveIDMixin(models.Model):

    def generate_number(self):
        return '{prepend}_'.format(prepend=self.DIDMeta.prepend) + ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(14))

    number = models.CharField(max_length=25, default=generate_number)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        try:
            pk = self.pk
        except AttributeError:
            pk = None
            super().__init__(*args, **kwargs)
        if not pk:
            self.number = self.generate_number()
