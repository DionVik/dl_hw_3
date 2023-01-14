# Generated by Django 4.1.3 on 2023-01-07 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0004_alter_message_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bulletin_board.category'),
        ),
    ]