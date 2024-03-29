# Generated by Django 3.2.5 on 2021-07-26 05:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('give_print', '0002_rename_prniting_technology_printer_printing_technology'),
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printspecification',
            name='colour',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='give_print.colour'),
        ),
        migrations.AlterField(
            model_name='printspecification',
            name='infill',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='printspecification',
            name='material',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='give_print.material'),
        ),
        migrations.AlterField(
            model_name='printspecification',
            name='technology',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='give_print.technology'),
        ),
    ]
