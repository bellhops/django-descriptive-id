## django-descriptive-id

```We're not the id you don't know what to do with, we're the other one```

django-descriptive-id is an abstract model that you can use as a mixin to give your models a human-readable identifier.

### About

The ```number``` field added by django-descriptive-id has ```null=True``` because, as of Django 1.8, you can not add a unique constraint to a field that already has a table in the DB.

### Usage

```pip install descriptive-id```

Add ```DescriptiveIDMixin``` to a model as a mixin:

```
from descriptive_id import DescriptiveIDMixin

class MyModel(DescriptiveIDMixin):
    pass
```

```django-descriptive-id``` prepends a random string with a short identifier string that is set on the model as a class, ```DIDMeta```:

```
from descriptive_id import DescriptiveIDMixin

class MyModel(DescriptiveIDMixin):

    class DIDMeta:
        prepend = 'mdl'
```

Now migrations need to be generated and for the new field:

```
python manage.py makemigrations
python manage.py migrate
```

Your model now has a field ```number``` that is human-readable:
```
>>> my_model = MyModel()
>>> my_model.number
'mdl_1d28s3h3nm79o'
```

If you are adding this mixing to a pre-existing model that exists in your db, you will need to add a migration that iterates through all of your objects and saves them. It should look something like this:
```
from django.db import migrations


def add_number_field_to_model(apps, schema_editor):
    YourModel = apps.get_model("your_app", "YourModel")
    for object in YourModel.objects.all().iterator():
        object.save()


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0000_last_dependency'),
    ]

    operations = [
        migrations.RunPython(add_number_field_to_model),
    ]
```
