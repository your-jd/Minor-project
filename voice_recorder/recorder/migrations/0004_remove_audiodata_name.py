# Generated by Django 5.0 on 2024-01-21 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recorder', '0003_remove_audiodata_last_modified_remove_audiodata_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiodata',
            name='name',
        ),
    ]
