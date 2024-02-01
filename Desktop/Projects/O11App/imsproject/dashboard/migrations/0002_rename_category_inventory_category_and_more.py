# Generated by Django 4.1.7 on 2023-03-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='quantity',
            new_name='Quantity',
        ),
        migrations.AddField(
            model_name='inventory',
            name='SN',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='Vendor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
