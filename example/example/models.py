# -*- coding: utf-8 -*-

from descriptive_id import DescriptiveIDMixin


class MyModel(DescriptiveIDMixin):

    class DIDMeta:
        prepend = 'mdl'
