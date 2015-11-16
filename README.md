## django-descriptive-id

>We're not the `id` you don't know what to do with, we're the other one.

django-descriptive-id adds a field to django for automatically generated human-readable identifiers.

### About

The ```DescriptiveIDField``` field added by django-descriptive-id requires a single parameter `prefix`, which will be used as the prefix for a unique human-readable character string.

### Installation

```pip install descriptive-id```

Add `descriptive_id` to your `installed_apps`:

```
INSTALLED_APPS = (
    ...
    'descriptive_id',
    ...
)
```

### Usage

Add a `DescriptiveIDField` to any model:

```
number = DescriptiveIDField(prefix='my_prefix')
```

```django-descriptive-id``` will append a random (but human-readable) string to the given prefix and store the result in the field.
