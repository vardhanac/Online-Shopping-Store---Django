# Generated by Django 2.2.1 on 2019-06-27 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190626_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]