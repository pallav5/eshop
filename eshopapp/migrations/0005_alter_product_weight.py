# Generated by Django 3.2.19 on 2023-05-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopapp', '0004_auto_20230529_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
