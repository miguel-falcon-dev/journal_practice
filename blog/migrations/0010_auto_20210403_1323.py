# Generated by Django 3.1.7 on 2021-04-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210402_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='photo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
