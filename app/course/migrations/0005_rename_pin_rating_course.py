# Generated by Django 4.0 on 2022-04-16 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_rating_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='pin',
            new_name='course',
        ),
    ]
