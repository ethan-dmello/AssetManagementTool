# Generated by Django 5.1.3 on 2024-11-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_equipment_category_equipment_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='added_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='asset_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='procured_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='usage_type',
            field=models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Phone', 'Phone'), ('iPad', 'iPad')], max_length=20, null=True),
        ),
    ]
