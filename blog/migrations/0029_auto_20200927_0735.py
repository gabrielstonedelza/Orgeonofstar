# Generated by Django 3.1.1 on 2020-09-27 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_userscheckedin_checked_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userscheckedin',
            old_name='checked_date',
            new_name='checked_in_date',
        ),
    ]