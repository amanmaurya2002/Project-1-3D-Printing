# Generated by Django 3.2.3 on 2021-08-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('give_print', '0002_rename_prniting_technology_printer_printing_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colour',
            name='colour',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='printer',
            name='make',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='printer',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
