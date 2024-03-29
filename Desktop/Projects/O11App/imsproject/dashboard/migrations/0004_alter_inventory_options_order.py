# Generated by Django 4.1.7 on 2023-03-13 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_alter_inventory_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Inventory', 'verbose_name_plural': 'Inventory'},
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.PositiveBigIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('Inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.inventory')),
                ('Staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
