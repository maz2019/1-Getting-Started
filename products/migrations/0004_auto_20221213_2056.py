# Generated by Django 3.1.4 on 2022-12-13 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221213_2024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProdCategory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Pcategory',
            new_name='category',
        ),
    ]
