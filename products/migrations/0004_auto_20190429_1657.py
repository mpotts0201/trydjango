# Generated by Django 2.0.7 on 2019-04-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190429_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(),
        ),
    ]