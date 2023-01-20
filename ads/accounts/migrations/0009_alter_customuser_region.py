# Generated by Django 4.1.3 on 2023-01-20 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='region',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.region'),
        ),
    ]
