# Generated by Django 4.1.3 on 2022-12-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0005_rename_user_profile_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='price',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
