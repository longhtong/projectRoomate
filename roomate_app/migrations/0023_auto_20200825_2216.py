# Generated by Django 3.1 on 2020-08-25 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomate_app', '0022_auto_20200825_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='token',
            field=models.CharField(default='c43390a871fe6d0de9453962467bdbc149438521', max_length=100),
        ),
    ]
