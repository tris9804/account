# Generated by Django 3.0.1 on 2019-12-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_merge_20191221_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='未分類', max_length=255),
        ),
    ]
