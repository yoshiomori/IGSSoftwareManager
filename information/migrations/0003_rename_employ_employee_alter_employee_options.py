# Generated by Django 4.0.6 on 2022-07-20 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_rename_departament_department_alter_employ_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employ',
            new_name='Employee',
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
    ]
