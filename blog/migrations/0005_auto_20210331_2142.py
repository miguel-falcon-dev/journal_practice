# Generated by Django 3.1.7 on 2021-04-01 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210330_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='photo',
            field=models.ImageField(height_field=200, null=True, upload_to='photos', verbose_name='photo', width_field=300),
        ),
    ]