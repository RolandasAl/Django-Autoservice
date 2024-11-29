# Generated by Django 5.1.3 on 2024-11-29 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0006_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='busena',
            options={'verbose_name': 'Būsena', 'verbose_name_plural': 'Būsenos'},
        ),
        migrations.AlterField(
            model_name='uzsakymas',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autoservice.busena', verbose_name='Būsena'),
        ),
    ]