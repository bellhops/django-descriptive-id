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
from descriptive_id.fields import DescriptiveIDField


number = DescriptiveIDField(prefix='my_prefix')
```

```django-descriptive-id``` will append a random (but human-readable) string to the given prefix and store the result in the field when an instance is added.

For the above example that might look something like:

```
'my_prefix_HLxGPQoemYERpN'
```

### Development

If you need to do development over this library, you can make use of the example application to test your developments.

Create a new virtual environment using virtualenv, and install the requirements from the example app into the virtual environment:

```
pip install -r example/requirements.txt
```

When you have made changes to the library, install the library into your virtual environment directly:

```
python setup.py install
```

The example app can then be initialized with migrations that make use of the field with your copy of the code installed.
