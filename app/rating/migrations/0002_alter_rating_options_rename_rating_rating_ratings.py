# Generated by Django 4.0 on 2022-04-16 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={},
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='ratings',
        ),
    ]
