# -*- coding: utf-8 -*-
from django.db import models

from descriptive_id.fields import DescriptiveIDField


class MyModel(models.Model):
    number = DescriptiveIDField(prefix='mdl')
