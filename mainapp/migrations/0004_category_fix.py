# Generated by Django 2.2.3 on 2020-02-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_fill_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='категория активна'),
        ),
    ]
