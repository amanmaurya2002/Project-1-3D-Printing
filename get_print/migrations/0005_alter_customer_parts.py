# Generated by Django 3.2.5 on 2021-07-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_print', '0004_alter_part_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='parts',
            field=models.ManyToManyField(blank=True, related_name='uploaded_by', to='get_print.Part'),
        ),
    ]
