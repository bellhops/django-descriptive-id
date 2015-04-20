# -*- coding: utf-8 -*-
import string
import random

from django.db import models


class DescriptiveIDMixin(models.Model):

    def _generate_number(self):
        try:
            prepend = self.DIDMeta.prepend
        except AttributeError:
            pass
        else:
            return '{prepend}_'.format(prepend=prepend) + ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(14))

    number = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk or not self.number:
            self.number = self._generate_number()
        super().save(*args, **kwargs)
