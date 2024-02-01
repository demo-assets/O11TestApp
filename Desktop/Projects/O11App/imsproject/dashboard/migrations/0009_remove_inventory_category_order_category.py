# Generated by Django 4.1.7 on 2023-03-17 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_inventory_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='Category',
        ),
        migrations.AddField(
            model_name='order',
            name='Category',
            field=models.CharField(choices=[('category', 'Quote'), ('category', 'Approved Orders')], max_length=20, null=True),
        ),
    ]