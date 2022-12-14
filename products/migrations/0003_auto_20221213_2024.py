# Generated by Django 3.1.4 on 2022-12-13 18:24

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221213_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prodcategory',
            options={},
        ),
        migrations.AddField(
            model_name='prodcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='prodcategory',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prodcategory',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prodcategory',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prodcategory',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='prodcategory',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prodcategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.prodcategory'),
        ),
        migrations.AlterUniqueTogether(
            name='prodcategory',
            unique_together=set(),
        ),
    ]
