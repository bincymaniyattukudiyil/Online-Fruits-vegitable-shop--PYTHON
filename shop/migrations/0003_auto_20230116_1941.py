# Generated by Django 3.2.16 on 2023-01-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Item_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='items',
            name='available',
            field=models.BooleanField(),
        ),
    ]
