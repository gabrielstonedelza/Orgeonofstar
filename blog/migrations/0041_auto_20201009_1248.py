# Generated by Django 3.1.1 on 2020-10-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_userscheckedin_check_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscheckedin',
            name='check_date',
            field=models.DateField(),
        ),
    ]
