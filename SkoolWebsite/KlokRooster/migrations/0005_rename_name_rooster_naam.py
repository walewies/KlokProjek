# Generated by Django 3.2.7 on 2021-12-09 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KlokRooster', '0004_rename_rooster_name_rooster_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooster',
            old_name='name',
            new_name='naam',
        ),
    ]