# Generated by Django 3.1.7 on 2021-04-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210331_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='photo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
