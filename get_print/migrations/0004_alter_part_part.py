# Generated by Django 3.2.5 on 2021-07-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_print', '0003_alter_part_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part',
            field=models.FileField(upload_to='uploads'),
        ),
    ]